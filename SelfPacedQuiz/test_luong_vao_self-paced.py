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

class JoinSelfPacedPage:
        
    def test_join_self_paced_pdf_quiz(self, page: Page) -> None:
        page.goto(urljoin(base_url, "65091415efe5de572294162e"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Play As A Quiz$")).nth(1).click()
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        expect(page).to_have_url(urljoin(base_url,"learning?worksheetid=6655a5f88b106c1a25c99949"))
        page.wait_for_timeout(3000)
    
    def test_join_self_paced_quiz_btn_self_paced(self, page: Page) -> None:
        page.goto(urljoin(base_url, "660a2dcfb241246061113681"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        expect(page).to_have_url(urljoin(base_url,"learning?worksheetid=660a2dcfb241246061113681"))
        page.wait_for_timeout(3000)

    def test_join_self_paced_quiz_btn_view_as_student(self, page: Page) -> None:
        page.goto(urljoin(base_url, "660a2dcfb241246061113681"), wait_until="load")
        page.get_by_text("View as a student").click()
        expect(page).to_have_url(urljoin(base_url,"#practice"))
        page.wait_for_timeout(3000)