"""
=============================================================
 Цепочка LangChain: Суммаризация текста с веб-страницы
=============================================================

Установка зависимостей:
    pip install langchain langchain-openai langchain-community
    pip install beautifulsoup4 requests

Переменные окружения:
    OPENAI_API_KEY=sk-...

Поддерживаемые LLM (на выбор):
  - OpenAI GPT-4o-mini  (рекомендуется, дёшево)
  - Ollama (локально, бесплатно):  ollama pull llama3
"""

import os
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate

# ── 1. Выбор модели ──────────────────────────────────────────────────────────

def get_llm():
    """Возвращает LLM-объект. Сначала пробует OpenAI, потом Ollama."""
    openai_key = os.getenv("OPENAI_API_KEY")

    if openai_key:
        from langchain_openai import ChatOpenAI
        print("✅ Используем OpenAI GPT-4o-mini")
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,               # 0 = детерминированный вывод
            openai_api_key=openai_key,
        )
    else:
        # Fallback на локальную Ollama (http://localhost:11434)
        from langchain_community.llms import Ollama
        print("✅ Используем локальную модель Ollama (llama3)")
        return Ollama(model="llama3", temperature=0)


# ── 2. Загрузка страницы ─────────────────────────────────────────────────────

def load_webpage(url: str) -> list:
    """
    Загружает HTML-страницу, извлекает чистый текст через BeautifulSoup.
    Возвращает список объектов Document.
    """
    print(f"🌐 Загружаем страницу: {url}")
    loader = WebBaseLoader(url)
    docs = loader.load()
    print(f"   Загружено символов: {sum(len(d.page_content) for d in docs):,}")
    return docs


# ── 3. Разбивка на чанки ─────────────────────────────────────────────────────

def split_documents(docs: list, chunk_size: int = 4000, overlap: int = 200) -> list:
    """
    Делит длинный текст на куски (chunks) для вписывания в контекст LLM.

    chunk_size  – максимальный размер одного куска (символы)
    overlap     – перекрытие между соседними кусками (сохраняет контекст)
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        separators=["\n\n", "\n", " ", ""],  # Приоритет разбиения: абзацы → строки → слова
    )
    chunks = splitter.split_documents(docs)
    print(f"   Разбито на {len(chunks)} фрагментов")
    return chunks


# ── 4. Цепочка суммаризации ──────────────────────────────────────────────────

def build_summarize_chain(llm, chain_type: str = "map_reduce"):
    """
    Строит цепочку суммаризации.

    chain_type варианты:
      "stuff"       – всё в один промпт (только для коротких текстов, <4 000 токенов)
      "map_reduce"  – каждый чанк резюмируется отдельно, затем объединяется (⭐ рекомендуется)
      "refine"      – итеративное уточнение суммари по чанкам (медленнее, точнее)
    """

    # Промпт для шага MAP (суммаризация одного чанка)
    map_prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            "Напиши краткое содержание следующего фрагмента текста на русском языке.\n"
            "Выдели только ключевые факты и идеи.\n\n"
            "Фрагмент:\n{text}\n\n"
            "Краткое содержание:"
        ),
    )

    # Промпт для шага REDUCE (объединение промежуточных суммари)
    reduce_prompt = PromptTemplate(
        input_variables=["text"],
        template=(
            "Ниже приведены краткие содержания нескольких частей одной статьи.\n"
            "Объедини их в единое связное резюме на русском языке (3–5 предложений).\n\n"
            "Фрагменты:\n{text}\n\n"
            "Итоговое резюме:"
        ),
    )

    chain = load_summarize_chain(
        llm=llm,
        chain_type=chain_type,
        map_prompt=map_prompt,
        combine_prompt=reduce_prompt,
        verbose=False,   # Поставь True, чтобы видеть промежуточные шаги
    )
    return chain


# ── 5. Точка входа ───────────────────────────────────────────────────────────

def summarize_url(url: str) -> str:
    """Полный pipeline: URL → загрузка → разбивка → суммаризация → строка."""
    llm    = get_llm()
    docs   = load_webpage(url)
    chunks = split_documents(docs)
    chain  = build_summarize_chain(llm, chain_type="map_reduce")

    print("🤖 Генерируем суммари...")
    result = chain.invoke({"input_documents": chunks})
    return result["output_text"]


# ── 6. Демо-запуск ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    TARGET_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

    print("=" * 60)
    print("  СУММАРИЗАЦИЯ ВЕБ-СТРАНИЦЫ (LangChain)")
    print("=" * 60)

    summary = summarize_url(TARGET_URL)

    print("\n📝 Итоговое резюме:")
    print("-" * 60)
    print(summary)
    print("-" * 60)

# ── Пример вывода ────────────────────────────────────────────────────────────
# ✅ Используем OpenAI GPT-4o-mini
# 🌐 Загружаем страницу: https://en.wikipedia.org/wiki/Python_(programming_language)
#    Загружено символов: 73,412
#    Разбито на 22 фрагментов
# 🤖 Генерируем суммари...
#
# 📝 Итоговое резюме:
# Python — высокоуровневый язык программирования общего назначения, созданный
# Гвидо ван Россумом в 1991 году. Он известен своей простотой синтаксиса и
# широким применением в науке о данных, веб-разработке и автоматизации. ...
