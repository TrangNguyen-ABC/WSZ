import re
from playwright.sync_api import Page, expect

class TestAssignChuaLogin:
    popup_login_selector = ".main-login-container"

    def test_click_assign_popup_share(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/66068fa6b2412460610a4b10")
        
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_click_button_assign(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/66068fa6b2412460610a4b10")
        
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_start_trong_landing_teaching(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/select-teaching-activities?worksheetId=624a986cfb1abe3256a780ad")
        
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()