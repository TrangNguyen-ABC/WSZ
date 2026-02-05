import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

load_dotenv()
base_url = os.getenv("BASE_URL")

class TestSubmit:
    def test_submit_khi_chua_hoan_thanh_cau_hoi(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.locator("#id-overview-dialog-v2").get_by_text("Submit").click()

        popup_confirm = page.locator("div.popup-header-text", has_text="It looks like you may have skipped some questions")
        expect(popup_confirm).to_be_visible(timeout=5000)

    def test_hien_thi_popup_congratulations_khi_hoan_thanh_cau_hoi(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()

        page.get_by_text("Kitten").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("ATiger").click()
        page.get_by_text("BackNext").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Cheetah").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Chameleon").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Bamboo").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Kangaroo").click()

        expect(page.get_by_text("Congratulations!", exact=True)).to_be_visible(timeout=5000)

    def test_hien_thi_click_submit_tren_popup_confirm(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.locator("#id-overview-dialog-v2").get_by_text("Submit").click()

        popup_confirm = page.locator("div.popup-header-text", has_text="It looks like you may have skipped some questions")
        expect(popup_confirm).to_be_visible(timeout=5000)

        page.locator("div").filter(has_text=re.compile(r"^Submit$")).nth(2).click()

        header_summary = page.locator("div.header-summary")
        expect(header_summary).to_be_visible(timeout=10000)

    def test_hien_thi_click_submit_tren_popup_congratulations(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()

        page.get_by_text("Kitten").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("ATiger").click()
        page.get_by_text("BackNext").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Cheetah").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Chameleon").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Bamboo").click()
        page.get_by_text("Next").first.click()
        page.get_by_text("Kangaroo").click()

        expect(page.get_by_text("Congratulations!", exact=True)).to_be_visible(timeout=5000)
        page.get_by_role("dialog").get_by_text("Submit", exact=True).click()
        header_summary = page.locator("div.header-summary")
        expect(header_summary).to_be_visible(timeout=10000)

