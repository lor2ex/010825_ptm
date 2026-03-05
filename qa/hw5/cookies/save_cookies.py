import json
from pathlib import Path
from selenium import webdriver

HERE = Path(__file__).resolve().parent
COOKIES_FILE = HERE / "globalsqa_cookies.json"

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
input("Примите/закройте баннер вручную один раз и нажмите Enter...")

with COOKIES_FILE.open("w", encoding="utf-8") as f:
    json.dump(driver.get_cookies(), f, ensure_ascii=False, indent=2)

driver.quit()
print("Saved to:", COOKIES_FILE)