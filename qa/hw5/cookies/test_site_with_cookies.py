import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COOKIES_FILE = HERE / "globalsqa_cookies.json"

def load_cookies(driver):
    driver.get("https://www.globalsqa.com/")  # сначала зайти на домен
    with COOKIES_FILE.open(encoding="utf-8") as f:
        cookies = json.load(f)

    for c in cookies:
        c.pop("sameSite", None)
        if "expiry" in c:
            c["expiry"] = int(c["expiry"])
        try:
            driver.add_cookie(c)
        except Exception:
            pass

def test_open_without_banner(driver):
    load_cookies(driver)
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")