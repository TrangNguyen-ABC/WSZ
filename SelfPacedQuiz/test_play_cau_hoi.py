import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

# Tải các biến môi trường từ file .env vào chương trình
load_dotenv()
base_url = os.getenv("BASE_URL")

class TestPlayMultipleChoiceInstantFeedback:
    # def test_hien_thi_click_mc_1_da_dung(self, page: Page) -> None:
    #     page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
    #     page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
    #     page.get_by_text("Start", exact=True).click()
    #     page.get_by_text("AKitten").click()
    #     element = page.locator('.cheer-answer.Correct')
    #     expect(element).to_be_visible()

    # def test_hien_thi_click_mc_2_da_dung(self, page: Page) -> None:
    #     page.goto(urljoin(base_url, "68f9d16b86868e001c064efb"), wait_until="load")
    #     page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
    #     page.get_by_text("Start", exact=True).click()
    #     page.get_by_text("A7").click()
    #     cheer_answer = page.locator('.cheer-answer.Incorrect')
    #     expect(cheer_answer).to_be_hidden()
    #     page.get_by_text("C9").click()
    #     expect(cheer_answer).to_be_visible()

    def test_hien_thi_answer_explanation(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/abcws-68f9d0e386868e001c064977")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("CHà Nội").click()
        explanation = page.locator('.summary-explanation-container.ex-question')
        expect(explanation).to_be_visible()