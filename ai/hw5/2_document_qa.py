"""
=============================================================
 Цепочка LangChain: Вопрос-Ответ по документам (RAG)
=============================================================

Установка зависимостей:
    pip install langchain langchain-openai langchain-community
    pip install faiss-cpu           # векторное хранилище (CPU-версия)
    pip install sentence-transformers  # или используй OpenAIEmbeddings

Переменные окружения:
    OPENAI_API_KEY=sk-...  (если не задан — будет использоваться HuggingFace embeddings)

Структура RAG-pipeline:
  ┌──────────────┐    ┌───────────────┐    ┌──────────────────────┐
  │  Текстовый   │───▶│  Разбивка на  │───▶│  Векторное хранилище │
  │  файл / текст│    │    чанки      │    │  (FAISS in-memory)   │
  └──────────────┘    └───────────────┘    └──────────┬───────────┘
                                                        │  similarity_search
                                                   ┌────▼────────────┐
  ┌─────────────┐                                  │  Retriever      │
  │  Вопрос     │─────────────────────────────────▶│  (топ-4 чанка)  │
  └─────────────┘                                  └────┬────────────┘
                                                        │
                                                   ┌────▼────────────┐
                                                   │  LLM + промпт   │
                                                   └────┬────────────┘
                                                        │
                                                   ┌────▼────────────┐
                                                   │  Ответ + источник│
                                                   └─────────────────┘
"""

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document


# ── 1. Текстовый файл-пример (создаётся автоматически) ──────────────────────

SAMPLE_TEXT = """
# Руководство по Django REST Framework (DRF)

## Что такое DRF?
Django REST Framework — мощный и гибкий инструмент для построения Web API на основе Django.
Он предоставляет сериализаторы, аутентификацию, разрешения и browsable API из коробки.

## Сериализаторы
Сериализатор преобразует объекты Python (модели Django) в JSON и обратно.
Класс ModelSerializer автоматически создаёт поля из модели.
Пример:
    class BookSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ['id', 'title', 'author', 'published_date']

## Аутентификация
DRF поддерживает несколько схем аутентификации:
- SessionAuthentication   – стандартные сессии Django (для браузерных клиентов)
- BasicAuthentication     – HTTP Basic Auth (только для разработки/тестов)
- TokenAuthentication     – токен передаётся в заголовке Authorization: Token <key>
- JWTAuthentication       – JSON Web Tokens через пакет djangorestframework-simplejwt

Для JWT необходимо добавить 'rest_framework_simplejwt' в INSTALLED_APPS
и настроить маршруты получения/обновления токена.

## Разрешения (Permissions)
Классы разрешений контролируют доступ к представлениям.
Популярные классы:
- AllowAny                – доступ без аутентификации
- IsAuthenticated         – только авторизованные пользователи
- IsAdminUser             – только администраторы
- IsAuthenticatedOrReadOnly – чтение для всех, изменение — только авторизованным

Пример применения в ViewSet:
    class BookViewSet(viewsets.ModelViewSet):
        permission_classes = [IsAuthenticatedOrReadOnly]

## ViewSets и Routers
ViewSet объединяет CRUD-операции в одном классе.
Router автоматически генерирует URL-маршруты:
    router = DefaultRouter()
    router.register(r'books', BookViewSet)
    urlpatterns += router.urls

Это создаёт маршруты: GET /books/, POST /books/, GET /books/{id}/, PUT /books/{id}/, DELETE /books/{id}/

## Пагинация
DRF поддерживает три вида пагинации:
- PageNumberPagination    – ?page=2&page_size=10
- LimitOffsetPagination   – ?limit=10&offset=20
- CursorPagination        – курсорная, для бесконечных лент

Настройка в settings.py:
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10,
    }

## Фильтрация
Пакет django-filter позволяет фильтровать QuerySet по параметрам URL:
    class BookFilter(django_filters.FilterSet):
        author = django_filters.CharFilter(lookup_expr='icontains')
        class Meta:
            model = Book
            fields = ['author', 'genre']
"""

SAMPLE_FILE = "drf_guide.txt"


def create_sample_file():
    """Создаёт текстовый файл с примерным содержимым."""
    with open(SAMPLE_FILE, "w", encoding="utf-8") as f:
        f.write(SAMPLE_TEXT)
    print(f"📄 Создан тестовый файл: {SAMPLE_FILE}")


# ── 2. Выбор LLM и Embeddings ────────────────────────────────────────────────

def get_llm_and_embeddings():
    """
    Возвращает пару (llm, embeddings).
    При наличии OPENAI_API_KEY использует GPT + OpenAI Embeddings.
    Иначе — Ollama + бесплатные HuggingFace embeddings (работает офлайн).
    """
    openai_key = os.getenv("OPENAI_API_KEY")

    if openai_key:
        from langchain_openai import ChatOpenAI, OpenAIEmbeddings
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, openai_api_key=openai_key)
        embeddings = OpenAIEmbeddings(openai_api_key=openai_key)
        print("✅ LLM: OpenAI GPT-4o-mini | Embeddings: OpenAI text-embedding-3-small")
    else:
        from langchain_community.llms import Ollama
        from langchain_community.embeddings import HuggingFaceEmbeddings
        llm = Ollama(model="llama3", temperature=0)
        # Модель паблично доступна, не требует ключей
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        print("✅ LLM: Ollama llama3 | Embeddings: HuggingFace multilingual")

    return llm, embeddings


# ── 3. Загрузка и индексация документа ──────────────────────────────────────

def build_vectorstore(file_path: str, embeddings) -> FAISS:
    """
    Читает файл, делит на чанки и создаёт FAISS-индекс в памяти.

    FAISS — быстрая библиотека от Meta для similarity search по векторам.
    """
    with open(file_path, encoding="utf-8") as f:
        text = f.read()

    # Разбиваем на чанки с небольшим перекрытием
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks   = splitter.split_text(text)
    docs     = [Document(page_content=c, metadata={"source": file_path}) for c in chunks]

    print(f"   Проиндексировано чанков: {len(docs)}")

    # Создаём векторный индекс (embed + сохраняем в RAM)
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


# ── 4. Цепочка RetrievalQA ───────────────────────────────────────────────────

def build_qa_chain(llm, vectorstore: FAISS) -> RetrievalQA:
    """
    Строит цепочку RetrievalQA:
      1. Retriever извлекает топ-4 похожих чанка по вопросу
      2. LLM получает вопрос + контекст → генерирует ответ
    """
    qa_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "Ты — технический ассистент. Используй ТОЛЬКО предоставленный контекст "
            "для ответа на вопрос. Если ответа в контексте нет — так и скажи.\n\n"
            "Контекст:\n{context}\n\n"
            "Вопрос: {question}\n\n"
            "Ответ:"
        ),
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",               # "stuff" = весь контекст в один промпт
        retriever=vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4},       # Возвращаем 4 наиболее релевантных чанка
        ),
        return_source_documents=True,     # Включаем источники в ответ
        chain_type_kwargs={"prompt": qa_prompt},
    )
    return chain


# ── 5. Вспомогательная функция вывода ───────────────────────────────────────

def ask_question(chain: RetrievalQA, question: str):
    """Задаёт вопрос и выводит ответ + использованные источники."""
    print(f"\n❓ Вопрос: {question}")
    result = chain.invoke({"query": question})

    print(f"💬 Ответ:\n{result['result']}")

    # Показываем, из каких чанков был составлен ответ
    print("\n📚 Использованные фрагменты:")
    for i, doc in enumerate(result["source_documents"], 1):
        preview = doc.page_content[:120].replace("\n", " ")
        print(f"  [{i}] ...{preview}...")


# ── 6. Точка входа ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("  QA ПО ДОКУМЕНТУ (LangChain RAG)")
    print("=" * 60)

    # Создаём тестовый файл
    create_sample_file()

    # Инициализируем LLM + embeddings
    llm, embeddings = get_llm_and_embeddings()

    # Строим векторное хранилище
    print("🔢 Индексируем документ...")
    vectorstore = build_vectorstore(SAMPLE_FILE, embeddings)

    # Строим цепочку QA
    qa_chain = build_qa_chain(llm, vectorstore)

    # Задаём тестовые вопросы
    QUESTIONS = [
        "Как настроить JWT аутентификацию в DRF?",
        "Какие классы разрешений есть в DRF?",
        "Что такое пагинация и какие её виды поддерживает DRF?",
        "Как автоматически создать URL-маршруты для ViewSet?",
    ]

    print("\n" + "=" * 60)
    for question in QUESTIONS:
        ask_question(qa_chain, question)
        print("-" * 60)
