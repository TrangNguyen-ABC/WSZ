import os
import re
from dotenv import load_dotenv
from urllib.parse import urljoin # Thư viện chuẩn để nối URL một cách an toàn
from playwright.sync_api import Page, expect

# Tải các biến môi trường từ file .env vào chương trình
load_dotenv()
# Lấy giá trị của biến BASE_URL từ môi trường
# Nếu không tìm thấy, giá trị sẽ là None
base_url = os.getenv("BASE_URL")

class TestDownloadChuaLogin:
    popup_login_selector = ".main-login-container"

    # def test_download_thumbnail(self, page: Page) -> None:
    #     page.goto("https://worksheetzone.org/worksheets")
    #     page.locator("#download-1750580290651").get_by_role("button").click()
    #     popup_login = page.locator(self.popup_login_selector)
    #     expect(popup_login).to_be_visible()

    def test_download_more_option(self, page: Page) -> None:
        page.goto(urljoin(base_url, "worksheets"), wait_until="load")
        page.locator("#dropdown-trigger-650914a3efe5de5722941721").get_by_role("button").click()
        page.locator("div").filter(has_text=re.compile(r"^Download worksheet$")).nth(3).click()
        page.get_by_text("Log in to your account").click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_download_more_option_answer_key(self, page: Page) -> None:
        page.goto(urljoin(base_url, "worksheets"), wait_until="load")
        page.locator("#dropdown-trigger-624a9507fb1abe3256a67f34 > .dropdown-trigger-wrapper > .action-item").click()
        page.locator("div").filter(has_text=re.compile(r"^Download with answer key$")).nth(3).click()
        page.get_by_text("Log in to your account").click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_preview_PDF(self, page: Page) -> None:
        page.goto(urljoin(base_url, "worksheets"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^All$")).click() #open dropdown type
        page.locator("[id=\"browsing\\.nonInteractive\"]").click() #select option non interactive
        page.get_by_role("link", name="Discover Similar Improve").click() #click thumbnail ws, open preview
        page.locator("#information-worksheet-top div").filter(has_text="Download").nth(4).click() #click button download
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_preview_interactive(self, page: Page) -> None:
        page.goto(urljoin(base_url, "worksheets"), wait_until="load")
        page.get_by_role("link", name="Discover Similar 2 pages The").click()
        page.locator("#information-worksheet-top div").filter(has_text="Download").nth(4).click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_detail_interactive(self, page: Page) -> None:
        page.goto(urljoin(base_url,"624a986cfb1abe3256a780ad"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(4).click()
        page.locator("div").filter(has_text=re.compile(r"^Worksheet$")).click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_detail_PDF(self, page: Page) -> None:
        page.goto(urljoin(base_url,"6588f117e0c742310abfe02f"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_download_self_paced_PDF(self, page: Page) -> None:
        page.goto(urljoin(base_url,"6588f117e0c742310abfe02f"), wait_until="load")
        page.locator("#download-btn").get_by_role("img").click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()