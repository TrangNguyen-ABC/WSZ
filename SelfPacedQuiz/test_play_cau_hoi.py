import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

# Tải các biến môi trường từ file .env vào chương trình
load_dotenv()
base_url = os.getenv("BASE_URL")

class TestPlayMultipleChoiceInstantFeedback:
    def test_hien_thi_click_mc_1_da_dung(self, page: Page) -> None:
        page.goto(urljoin(base_url, "665597a9b30a26001cc2430b"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("AKitten").click()
        