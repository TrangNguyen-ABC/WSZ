import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

# Tải các biến môi trường từ file .env vào chương trình
load_dotenv()
# Lấy giá trị của biến BASE_URL từ môi trường
# Nếu không tìm thấy, giá trị sẽ là None
base_url = os.getenv("BASE_URL")

class CheckSettingsQuestions:
    def test_join_self_paced_pdf_quiz(self, page: Page) -> None:
        page.goto(urljoin(base_url, "65091415efe5de572294162e"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Play As A Quiz$")).nth(1).click()
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        expect(page).to_have_url(urljoin(base_url,"learning?worksheetid=6655a5f88b106c1a25c99949"))
        page.wait_for_timeout(3000)

class CheckSettingsTimer:
    def test_join_self_paced_pdf_quiz(self, page: Page) -> None:
        page.goto(urljoin(base_url, "665597a9b30a26001cc2430b"), wait_until="load")
        count = page.locator('div.header-question').count()
