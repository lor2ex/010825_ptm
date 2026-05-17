import os
import time
import logging

from dotenv import load_dotenv
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
    retry_if_exception_type,
    before_sleep_log,
)

from google import genai
from google.genai import types
from requests import ReadTimeout
from google.genai.errors import ClientError

try:
    from google.api_core.exceptions import ResourceExhausted, DeadlineExceeded, ServiceUnavailable
except ImportError:
    ResourceExhausted = DeadlineExceeded = ServiceUnavailable = Exception


load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY не найден в .env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

timeout_seconds = 10

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=timeout_seconds * 1000)
)


@retry(
    retry=retry_if_exception_type((
        ReadTimeout,
        TimeoutError,
        ResourceExhausted,
        DeadlineExceeded,
        ServiceUnavailable,
    )),
    wait=wait_random_exponential(multiplier=1, max=20),
    stop=stop_after_attempt(5),
    reraise=True,
    before_sleep=before_sleep_log(logger, logging.WARNING),
)
def get_gemini_response(prompt: str) -> str:
    time.sleep(0.3)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    if not getattr(response, "text", None):
        raise ValueError("Пустой ответ от Gemini")

    return response.text


if __name__ == "__main__":
    try:
        print(f"GEMINI_API_KEY loaded: {bool(api_key)}")
        print(f"GEMINI_API_KEY prefix: {api_key[:8]}..." if api_key else "No key")

        response = get_gemini_response("What is request timeout?")
        print(response)

    except ClientError as e:
        print(f"Ошибка клиента Gemini: {e}")
    except ResourceExhausted:
        print("Слишком много запросов к API: превышен rate limit.")
    except ReadTimeout:
        print(f"Запрос превысил таймаут ({timeout_seconds} секунд).")
    except DeadlineExceeded:
        print(f"Gemini не успел ответить за {timeout_seconds} секунд.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")