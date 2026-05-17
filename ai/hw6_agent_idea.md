# Django-агент для Code Review и отладки

## Идея

Разработчик тратит значительную часть рабочего времени на однотипные задачи: найти ошибку в трейсбеке, проверить сериализатор на уязвимости, убедиться что миграция не сломает данные. Агент **DjangoDev Assistant** берёт эти задачи на себя — он не просто отвечает на вопросы, а самостоятельно анализирует файлы, запускает проверки и возвращает конкретный отчёт с приоритизированными правками.

Ключевое отличие от обычного чат-бота: агент **сам решает, какие инструменты вызывать** в зависимости от входных данных (файл, трейсбек, вопрос), и продолжает работу до получения финального ответа.

---

## Что агент умеет решать

- Разбор трейсбека Django (`500 Internal Server Error`, `IntegrityError`, `circular import`) → точная строка, причина, правка
- Проверка сериализатора DRF на типичные ошибки: отсутствие валидации, `UniqueConstraint`, незащищённые поля
- Анализ файла миграций — есть ли `RunPython` без `reverse_code`, опасный `DROP COLUMN`, конфликт зависимостей
- Проверка `settings.py` на секреты в открытом виде (`SECRET_KEY`, `DEBUG=True` в продакшене)
- Ответы на вопросы по коду с привязкой к конкретным строкам файла

---

## Архитектура агента

```
Пользователь
    │
    ▼
┌───────────────────────────────────┐
│           AgentExecutor            │   ← LangChain ReAct Agent
│   "Думает → Выбирает Tool → Запускает → Анализирует результат → Повторяет"
└──────────────┬────────────────────┘
               │
       ┌───────┴──────────┐
       │   Tools (6 шт.)  │
       └──────────────────┘
           │  │  │  │  │  │
           ▼  ▼  ▼  ▼  ▼  ▼
```

### Инструменты агента

| № | Инструмент | Что делает |
|---|---|---|
| 1 | `read_file` | Читает `.py`-файл из проекта по пути |
| 2 | `parse_traceback` | Извлекает тип ошибки, файл и номер строки из трейсбека |
| 3 | `run_flake8` | Запускает `flake8` на файле, возвращает список нарушений |
| 4 | `check_migrations` | Парсит файл миграции, ищет опасные операции |
| 5 | `search_django_docs` | Ищет по документации Django/DRF через API |
| 6 | `suggest_fix` | Генерирует исправленный фрагмент кода с объяснением |

---

## Как работает: пример сессии

**Вход от пользователя:**
```
Traceback (most recent call last):
  File "my_app/serializers/bookings.py", line 6, in <module>
    from my_app.serializers.properties import PropertySerializer
ImportError: cannot import name 'BookingSerializer' from 'my_app.serializers.bookings'
```

**Внутренний цикл агента (ReAct loop):**

```
Thought: Это circular import. Нужно прочитать оба файла и найти кольцо зависимостей.
Action: read_file("my_app/serializers/bookings.py")
Observation: [содержимое файла]

Thought: bookings.py импортирует из properties.py на строке 6.
Action: read_file("my_app/serializers/properties.py")
Observation: properties.py импортирует BookingSerializer из bookings.py → кольцо!

Thought: Нужно показать правку. Решение — ленивый импорт внутри метода или реструктуризация.
Action: suggest_fix(description="circular import", files=[...])
Observation: [готовый патч]

Final Answer: ...
```

**Вывод:**
```
🔴 Circular Import: bookings.py ↔ properties.py

Причина: оба файла импортируют друг друга на верхнем уровне.

Решение — перенести импорт внутрь метода:

# bookings.py, строка 6 — БЫЛО:
from my_app.serializers.properties import PropertySerializer

# СТАЛО (внутри класса):
def to_representation(self, instance):
    from my_app.serializers.properties import PropertySerializer
    ...

Приоритет: 🔴 Критично (блокирует запуск сервера)
```

---

## Технический стек

```python
# Основные зависимости
langchain>=0.2
langchain-openai          # или langchain-community + Ollama
langchain-community
flake8                    # статический анализ Python
ast                       # стандартная библиотека — парсинг Python AST
```

### Структура кода

```
django_agent/
├── agent.py              # AgentExecutor + системный промпт
├── tools/
│   ├── file_reader.py    # read_file: открывает .py по пути
│   ├── traceback_parser.py  # parse_traceback: regex + ast
│   ├── linter.py         # run_flake8: subprocess + парсинг вывода
│   ├── migration_checker.py  # check_migrations: ast.parse
│   ├── docs_search.py    # search_django_docs: requests + DuckDuckGo
│   └── fix_suggester.py  # suggest_fix: LLM sub-chain
└── prompts.py            # системный промпт агента
```

### Ключевой фрагмент — регистрация инструментов

```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
import subprocess, ast

@tool
def run_flake8(file_path: str) -> str:
    """Запускает flake8 на Python-файле и возвращает список нарушений."""
    result = subprocess.run(
        ["flake8", "--max-line-length=120", file_path],
        capture_output=True, text=True
    )
    return result.stdout or "✅ Нарушений не найдено"

@tool
def check_migrations(file_path: str) -> str:
    """Анализирует файл миграции Django на опасные операции."""
    with open(file_path) as f:
        tree = ast.parse(f.read())
    # ... поиск RunPython без reverse_code, DeleteModel, RemoveField
    ...

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [read_file, parse_traceback, run_flake8,
         check_migrations, search_django_docs, suggest_fix]

agent = create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=8)
```

---

## Системный промпт

```
Ты — опытный Django/DRF разработчик и ментор.
Твоя задача: находить ошибки и предлагать точные исправления.

Правила:
1. Всегда читай файл перед тем как давать совет
2. Указывай номер строки для каждой правки
3. Расставляй приоритеты: 🔴 Критично / 🟡 Предупреждение / 🟢 Стиль
4. Если не уверен — используй search_django_docs перед ответом
5. Никогда не выдумывай трейсбеки или код которого не видел
```

---

## Почему этот агент полезен

Три ситуации, где он экономит больше всего времени:

**1. Circular import при запуске сервера** — вместо 10 минут ручного поиска по `__init__.py` и импортам агент находит кольцо за 3 вызова инструментов.

**2. Проверка сериализатора перед PR** — агент запускает `flake8`, проверяет `UniqueConstraint`, ищет незащищённые поля (`write_only=False` для пароля) и выдаёт чеклист.

**3. Анализ миграции перед деплоем** — агент проверяет есть ли `RunPython` без `reverse_code`, есть ли `RemoveField` у обязательных полей, безопасен ли порядок зависимостей.

---

## Расширения на будущее

- **Git-интеграция**: агент сам читает `git diff` перед коммитом и проверяет изменённые файлы
- **Postman-совместимость**: принимает `.json`-коллекцию Postman и проверяет покрытие эндпоинтов тестами
- **Локальный режим через Ollama**: полностью офлайн, без отправки кода на внешние серверы — важно для проектов с чувствительными данными
