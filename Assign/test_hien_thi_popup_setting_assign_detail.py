import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "state_1.json"
AUTH_FILE_PATH_2 = "state_2.json"

def test_hien_thi_setting_chua_co_hs_join(browser: Browser) -> None:
    
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/678d198ce633858a58ac511d", wait_until="networkidle")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        pass
    page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    start_date = page.get_by_role("button", name="Choose date, selected date is").first
    expect(start_date).to_be_enabled()
    due_date = page.get_by_role("button", name="Choose date, selected date is").nth(1)
    expect(due_date).to_be_enabled()
    timer = page.locator("div").filter(has_text=re.compile(r"^TimerSet a time limit for students to complete their assignment$")).get_by_label("controlled")
    expect(timer).to_be_enabled()
    participant_attempts = page.get_by_role("textbox", name="1")
    expect(participant_attempts).to_be_enabled()
    instant_feedback = page.get_by_role("checkbox", name="controlled").nth(1)
    expect(instant_feedback).to_be_enabled()
    show_feedback_after_submit = page.get_by_role("checkbox", name="controlled").nth(2)
    expect(show_feedback_after_submit).to_be_enabled()
    allow_submit_late = page.get_by_role("checkbox", name="controlled").nth(3)
    expect(allow_submit_late).to_be_enabled()

############
def test_hien_thi_setting_da_co_hs_join(browser: Browser) -> None:
    
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # # Tạo một trang mới từ context đã có trạng thái đăng nhập
    # page = context.new_page()
    # page.goto("https://staging.worksheetzone.org/assign?code=5QZVTE", wait_until="networkidle")
    # page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    # start_date = page.get_by_role("button", name="Choose date, selected date is").first
    # expect(start_date).to_be_disabled()
    # due_date = page.get_by_role("button", name="Choose date, selected date is").nth(1)
    # expect(due_date).to_be_enabled()
    # timer = page.locator("div").filter(has_text=re.compile(r"^TimerSet a time limit for students to complete their assignment$")).get_by_label("controlled")
    # expect(timer).to_be_disabled()
    # participant_attempts = page.get_by_role("textbox", name="1")
    # expect(participant_attempts).to_be_disabled()
    # instant_feedback = page.get_by_role("checkbox", name="controlled").nth(1)
    # expect(instant_feedback).to_be_disabled()
    # show_feedback_after_submit = page.get_by_role("checkbox", name="controlled").nth(2)
    # expect(show_feedback_after_submit).to_be_disabled()
    # allow_submit_late = page.get_by_role("checkbox", name="controlled").nth(3)
    # expect(allow_submit_late).to_be_disabled()
    


    # page1 = context.new_page()