import re
from playwright.sync_api import Page, expect

class TestWSKhaDung:
    button_assign_popup_share = "Assign"

    def test_ws_PDF(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/6588f117e0c742310abfe02f", wait_until="networkidle")
        button_assign = page.get_by_text("Assign")
        expect(button_assign).to_be_hidden()

    def test_ws_PDF_Quiz(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
        page.locator("div").filter(has_text=re.compile(r"^Share$")).click()
        button_assign_popup_share = page.get_by_text(self.button_assign_popup_share, exact=True)
        expect(button_assign_popup_share).to_be_enabled()

    def test_ws_Quiz(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/66068fa6b2412460610a4b10", wait_until="networkidle")
        button_assign = page.get_by_text("Assign")
        expect(button_assign).to_be_visible()

    def test_ws_interactive(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="networkidle")
        button_assign = page.get_by_text("Assign")
        expect(button_assign).to_be_visible()
        
