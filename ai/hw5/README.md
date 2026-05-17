# LangChain Demo — Суммаризация и QA

Два проекта для изучения цепочек LangChain.

---

## Структура

```
langchain_demo/
├── 1_web_summarizer.py   # Суммаризация веб-страницы
├── 2_document_qa.py      # Вопрос-ответ по документу (RAG)
└── README.md
```

---

## Установка

```bash
pip install langchain langchain-openai langchain-community
pip install beautifulsoup4 requests faiss-cpu sentence-transformers
```

### Добавить ключ OpenAI (Linux/macOS)
```bash
export OPENAI_API_KEY="sk-..."
```

### Или использовать Ollama (бесплатно, офлайн)
```bash
# Установить: https://ollama.com
ollama pull llama3
```

---

## 1. Суммаризация веб-страницы

```bash
python 1_web_summarizer.py
```

**Как работает:**
```
URL → WebBaseLoader → RecursiveCharacterTextSplitter → load_summarize_chain (map_reduce) → Резюме
```

| chain_type   | Когда использовать                            |
|--------------|-----------------------------------------------|
| `stuff`      | Короткие тексты (< 4 000 токенов)             |
| `map_reduce` | Длинные тексты, параллельная обработка чанков |
| `refine`     | Максимальное качество, медленнее              |

**Изменить URL** (строка 130 в файле):
```python
TARGET_URL = "https://ru.wikipedia.org/wiki/Python"
```

---

## 2. Вопрос-Ответ по документу (RAG)

```bash
python 2_document_qa.py
```

**Как работает (RAG-pipeline):**
```
Файл → Chunking → FAISS (векторный индекс)
                        ↓
Вопрос → Similarity Search → топ-4 чанка → LLM → Ответ
```

**Использовать свой файл:**
```python
vectorstore = build_vectorstore("my_notes.txt", embeddings)
```

**Задать свой вопрос:**
```python
ask_question(qa_chain, "Что такое SOLID принципы?")
```

---

## Сравнение двух подходов

| Аспект         | Суммаризация           | QA (RAG)                      |
|----------------|------------------------|-------------------------------|
| Задача         | Резюме всего текста    | Ответ на конкретный вопрос    |
| Входные данные | URL или файл           | Файл / база документов        |
| Цепочка        | `load_summarize_chain` | `RetrievalQA`                 |
| Поиск          | Не нужен               | Similarity search (FAISS)     |
| Вывод          | Текстовое резюме       | Ответ + источники             |

---

## Полезные ссылки

- [LangChain документация](https://python.langchain.com/docs/)
- [LangChain Summarization](https://python.langchain.com/docs/use_cases/summarization)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
