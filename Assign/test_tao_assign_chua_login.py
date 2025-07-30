import re
from playwright.sync_api import Page, expect

class TestAssignChuaLogin:
    popup_login_selector = ".main-login-container"

    def test_click_assign_popup_share(self, page: Page) -> None:
        page.goto("https://staging.worksheetzone.org/6589048ce0c742310ac00797")
        page.locator("div").filter(has_text=re.compile(r"^Share$")).click()
        page.get_by_text("Assign", exact=True).click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_click_button_assign(self, page: Page) -> None:
        page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10")
        page.get_by_text("Assign").click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()

    def test_start_trong_landing_teaching(self, page: Page) -> None:
        page.goto("https://staging.worksheetzone.org/select-teaching-activities?worksheetId=624a986cfb1abe3256a780ad")
        page.locator("#select-game-screen").get_by_text("Assign Homework").click()
        page.get_by_text("Start", exact=True).click()
        popup_login = page.locator(self.popup_login_selector)
        expect(popup_login).to_be_visible()