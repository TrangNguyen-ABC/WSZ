import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

load_dotenv()
base_url = os.getenv("BASE_URL")

class TestCheckSettingsQuestions:
    def test_hien_thi_so_cau_hoi_mac_dinh(self, page: Page) -> None:
        page.goto(urljoin(base_url, "665597a9b30a26001cc2430b"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        #lấy value trong ô input Questions

        input_selector = "input.input-value.input-text"
        input_element = page.locator(input_selector)
        value_str = input_element.input_value()
        print(f"Giá trị trong ô input (value_str): {value_str}") # Để debug
        
        # So sánh value_str với 19
        expected_value = 19

        try:
            actual_value_int = int(value_str) # Chuyển đổi chuỗi thành số nguyên
            print(f"Giá trị trong ô input sau khi chuyển đổi (actual_value_int): {actual_value_int}")
            expect(input_element).to_have_value(str(expected_value)) # expect.to_have_value() mong đợi một chuỗi

        except ValueError:
            print(f"Lỗi: Không thể chuyển đổi '{value_str}' thành số nguyên.")
            assert False, f"Giá trị input '{value_str}' không phải là số hợp lệ."


class TestCheckSettingsTimer:
    def test_hien_thi_mac_dinh_timer(self, page: Page) -> None:
        page.goto(urljoin(base_url, "665597a9b30a26001cc2430b"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        text_container_selector = "div.input-value.input-text"
        text_element = page.locator(text_container_selector)
        text_content = text_element.text_content()

        print(f"Nội dung text trong phần tử là: '{text_content}'")
class TestCheckConvertQuestions:
    def test_hien_thi_mac_dinh_tuy_chon(self, page: Page) -> None:
        page.goto(urljoin(base_url, "665597a9b30a26001cc2430b"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        multiple_choice = page.get_by_role("checkbox").first
        matching = page.get_by_role("checkbox").nth(1)
        true_false = page.get_by_role("checkbox").nth(2)
        expect(multiple_choice).to_be_checked()
        expect(matching).not_to_be_checked()
        expect(true_false).not_to_be_checked()
    
    def test_hien_thi_quiz_multiple_choice(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9cd8d86868e001c063c5c"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        multiple_choice = page.get_by_role("checkbox").first
        matching = page.get_by_role("checkbox").nth(1)
        true_false = page.get_by_role("checkbox").nth(2)
        expect(multiple_choice).to_be_enabled()
        expect(matching).to_be_enabled()
        expect(true_false).to_be_enabled()

    def test_hien_thi_quiz_1_multiple_choice(self, page: Page) -> None:
        page.goto(urljoin(base_url, "690077b9228086001c7b6f06"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        multiple_choice = page.get_by_role("checkbox").first
        matching = page.get_by_role("checkbox").nth(1)
        true_false = page.get_by_role("checkbox").nth(2)
        expect(multiple_choice).to_be_enabled()
        expect(matching).to_be_disabled()
        expect(true_false).to_be_enabled()
    
    def test_hien_thi_quiz_open_response(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9dd5b86868e001c070e35"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        multiple_choice = page.get_by_role("checkbox").first
        matching = page.get_by_role("checkbox").nth(1)
        true_false = page.get_by_role("checkbox").nth(2)
        expect(multiple_choice).to_be_checked()
        expect(matching).to_be_disabled()
        expect(true_false).to_be_disabled()

    def test_hien_thi_quiz_fill_in_the_blank(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        multiple_choice = page.get_by_role("checkbox").first
        matching = page.get_by_role("checkbox").nth(1)
        true_false = page.get_by_role("checkbox").nth(2)
        expect(multiple_choice).to_be_checked()
        expect(matching).to_be_disabled()
        expect(true_false).to_be_disabled()

class TestCheckInstantFeedback:
    def test_hien_thi_mac_dinh_quiz_multiple_choice(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9cd8d86868e001c063c5c"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        instant_feedback = page.get_by_role("checkbox").nth(3)
        expect(instant_feedback).to_be_checked()

    def test_hien_thi_mac_dinh_quiz_open_response(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9dd5b86868e001c070e35"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        instant_feedback = page.get_by_role("checkbox").nth(3)
        expect(instant_feedback).to_be_disabled()

    def test_hien_thi_mac_dinh_quiz_fill_in_the_blank(self, page: Page) -> None:
        page.goto(urljoin(base_url, "68f9da8586868e001c070043"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        instant_feedback = page.get_by_role("checkbox").nth(3)
        expect(instant_feedback).to_be_checked()

    def test_hien_thi_mac_dinh_quiz_3_dang_cau(self, page: Page) -> None:
        page.goto(urljoin(base_url, "69008158228086001c7b924e"), wait_until="load")
        page.locator("div").filter(has_text=re.compile(r"^Self-test$")).nth(1).click()
        instant_feedback = page.get_by_role("checkbox").nth(3)
        expect(instant_feedback).to_be_checked()
