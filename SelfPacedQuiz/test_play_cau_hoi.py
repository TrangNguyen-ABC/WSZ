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
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("AKitten").click()
        element = page.locator('.cheer-answer.Correct')
        expect(element).to_be_visible()

    def test_hien_thi_click_mc_2_da_dung(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d16b86868e001c064efb"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("A7").click()
        cheer_answer = page.locator('.cheer-answer.Incorrect')
        expect(cheer_answer).to_be_hidden()
        page.get_by_text("C9").click()
        expect(cheer_answer).to_be_visible()

    def test_hien_thi_answer_explanation(self, page: Page) -> None:
        page.goto("https://worksheetzone.org/abcws-68f9d0e386868e001c064977")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("CHà Nội").click()
        explanation = page.locator('.summary-explanation-container.ex-question')
        expect(explanation).to_be_visible()

class TestPlayMultipleChoiceKhongInstantFeedback:
    def test_hien_thi_click_mc_1_da_dung(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
         # Thử uncheck và kiểm tra
        checkbox_locator = page.get_by_role("checkbox").nth(3)
        max_attempts = 5 # Số lần thử lại tối đa
        attempt = 0
        while checkbox_locator.is_checked() and attempt < max_attempts:
            print(f"Attempt {attempt + 1}: Checkbox is still checked, trying to uncheck...")
            checkbox_locator.uncheck()
            # Có thể thêm một khoảng chờ ngắn để UI cập nhật
            page.wait_for_timeout(500) # Chờ 0.5 giây
            attempt += 1
        
        # Kiểm tra cuối cùng để đảm bảo nó đã được uncheck
        # Nếu sau max_attempts vẫn chưa uncheck, bài test sẽ thất bại
        expect(checkbox_locator).not_to_be_checked(timeout=5000)
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("AKitten").click()
        element = page.locator('.cheer-answer.Correct')
        expect(element).to_be_hidden()

    def test_hien_thi_click_mc_2_da_dung(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d16b86868e001c064efb"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        checkbox_locator = page.get_by_role("checkbox").nth(3)
        
        # Thử uncheck và kiểm tra
        max_attempts = 5 # Số lần thử lại tối đa
        attempt = 0
        while checkbox_locator.is_checked() and attempt < max_attempts:
            print(f"Attempt {attempt + 1}: Checkbox is still checked, trying to uncheck...")
            checkbox_locator.uncheck()
            # Có thể thêm một khoảng chờ ngắn để UI cập nhật
            page.wait_for_timeout(500) # Chờ 0.5 giây
            attempt += 1
        
        # Kiểm tra cuối cùng để đảm bảo nó đã được uncheck
        # Nếu sau max_attempts vẫn chưa uncheck, bài test sẽ thất bại
        expect(checkbox_locator).not_to_be_checked(timeout=5000)
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("A7").click()
        cheer_answer = page.locator('.cheer-answer.Incorrect')
        expect(cheer_answer).to_be_hidden()
        page.get_by_text("C9").click()
        expect(cheer_answer).to_be_hidden()

    def test_hien_thi_thay_doi_da_mc_1_da_dung(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()

        checkbox_locator = page.get_by_role("checkbox").nth(3)
        max_attempts = 5 # Số lần thử lại tối đa
        attempt = 0
        while checkbox_locator.is_checked() and attempt < max_attempts:
            print(f"Attempt {attempt + 1}: Checkbox is still checked, trying to uncheck...")
            checkbox_locator.uncheck()
            # Có thể thêm một khoảng chờ ngắn để UI cập nhật
            page.wait_for_timeout(500) # Chờ 0.5 giây
            attempt += 1
        
        # Kiểm tra cuối cùng để đảm bảo nó đã được uncheck
        # Nếu sau max_attempts vẫn chưa uncheck, bài test sẽ thất bại
        expect(checkbox_locator).not_to_be_checked(timeout=5000)
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("AKitten").click()
        page.get_by_text("CCub").click()
        element = page.locator('.cheer-answer.Correct')
        expect(element).to_be_hidden()

class TestPlayFitb:
    def test_hien_thi_input_text_vao_blank(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        blank_1 = page.locator("#wordBlank-0")
        blank_1.fill("123")
        expect(blank_1).to_have_value("123")
        
    def test_hien_thi_click_text_trong_wb(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("What").click()
        blank_1 = page.locator("#wordBlank-0")
        expect(blank_1).to_have_value("What")

    def test_hien_thi_fitb_instant_feedback(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("What").click()
        page.locator("#wordBlank-0").press("Enter")
        correct_element = page.locator(".correct")
        expect(correct_element).to_be_visible()

    def test_hien_thi_fitb_khong_instant_feedback(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        checkbox_locator = page.get_by_role("checkbox").nth(3)
        max_attempts = 5 # Số lần thử lại tối đa
        attempt = 0
        while checkbox_locator.is_checked() and attempt < max_attempts:
            print(f"Attempt {attempt + 1}: Checkbox is still checked, trying to uncheck...")
            checkbox_locator.uncheck()
            # Có thể thêm một khoảng chờ ngắn để UI cập nhật
            page.wait_for_timeout(500) # Chờ 0.5 giây
            attempt += 1
        
        # Kiểm tra cuối cùng để đảm bảo nó đã được uncheck
        # Nếu sau max_attempts vẫn chưa uncheck, bài test sẽ thất bại
        expect(checkbox_locator).not_to_be_checked(timeout=5000)
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("What").click()
        page.locator("#wordBlank-0").press("Enter")
        correct_element = page.locator(".correct")
        expect(correct_element).to_be_hidden()

class TestPlayOpenResponse:
    def test_hien_thi_input_text_open_response_(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9dd5b86868e001c070e35"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        input_box = page.get_by_role("textbox", name="Type the answer")
        input_box.fill("123")
        expect(input_box).to_have_value("123")

    def test_hien_thi_thay_doi_input_text_open_response(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9dd5b86868e001c070e35"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()
        input_box_old = page.get_by_role("textbox", name="Type the answer")
        input_box_old.fill("123")
        expect(input_box_old).to_have_value("123")
        page.get_by_text("Question List123456Answer Sheet1 of 6What is the largest land animal?Your").click()
        input_box_new = page.get_by_role("textbox", name="Type the answer")
        input_box_new.fill("678")
        expect(input_box_new).to_have_value("678")

class TestPlayTrueFalse:
    def test_hien_thi_tick_da_instant_feedback(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_role("checkbox").nth(2).check()
        page.get_by_role("checkbox").first.uncheck()
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("Atrue").click()
        
        incorrect_selector = ".cheer-answer.Incorrect"
        correct_selector = ".cheer-answer.Correct"

        expect(page.locator(incorrect_selector)).to_be_visible(timeout=5000)
        expect(page.locator(correct_selector)).to_be_visible(timeout=5000)
        
    def test_hien_thi_tick_da_khong_instant_feedback(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_role("checkbox").nth(2).check()
        page.get_by_role("checkbox").first.uncheck()
        checkbox_locator = page.get_by_role("checkbox").nth(3)
        max_attempts = 5 # Số lần thử lại tối đa
        attempt = 0
        while checkbox_locator.is_checked() and attempt < max_attempts:
            print(f"Attempt {attempt + 1}: Checkbox is still checked, trying to uncheck...")
            checkbox_locator.uncheck()
            # Có thể thêm một khoảng chờ ngắn để UI cập nhật
            page.wait_for_timeout(500) # Chờ 0.5 giây
            attempt += 1
        # Kiểm tra cuối cùng để đảm bảo nó đã được uncheck
        # Nếu sau max_attempts vẫn chưa uncheck, bài test sẽ thất bại
        expect(checkbox_locator).not_to_be_checked(timeout=5000)
        page.get_by_text("Start", exact=True).click()
        page.get_by_text("Atrue").click()
        
        incorrect_selector = ".cheer-answer.Incorrect"
        correct_selector = ".cheer-answer.Correct"

        expect(page.locator(incorrect_selector)).not_to_be_visible(timeout=5000)
        expect(page.locator(correct_selector)).not_to_be_visible(timeout=5000)

# class TestPlayMatching:

class Testbacknext:
    def test_next_cau_hoi(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9d05086868e001c0644de"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-paced learning$")).nth(1).click()
        page.get_by_text("Start", exact=True).click()

        progress_locator_1 = page.locator("div.progress")
        expect(progress_locator_1).to_have_text("1 of 6")

        page.locator("div").filter(has_text=re.compile(r"^Next$")).first.click()

        progress_locator_2 = page.locator("div.progress")
        expect(progress_locator_2).to_have_text("2 of 6")