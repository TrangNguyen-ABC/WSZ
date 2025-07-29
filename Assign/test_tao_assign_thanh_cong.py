import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "state_1.json"
AUTH_FILE_PATH_2 = "state_2.json"

def test_create_assign_success_from_popup_share_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ popup share quiz 
    """
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
    page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
    