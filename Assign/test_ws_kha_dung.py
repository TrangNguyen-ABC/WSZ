import re
from playwright.sync_api import Page, expect

class TestDownloadChuaLogin:
    def test_download_more_option(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/worksheets", wait_until="networkidle")
        page.locator("#dropdown-trigger-650914a3efe5de5722941721").get_by_role("button").click()
        page.locator("div").filter(has_text=re.compile(r"^Download worksheet$")).nth(3).click()
        page.get_by_text("Log in to your account").click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()