import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "state_1.json"
AUTH_FILE_PATH_2 = "state_2.json"

def test_create_assign_success_from_popup_share_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ popup share quiz 
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_2}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_2)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_2}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    page.get_by_role("button", name="Share").click()
    page.get_by_text("Assign", exact=True).click()
    page.get_by_role("dialog").get_by_role("button", name="Assign").click()
    
    try:
        # Chúng ta sẽ cố gắng tìm và click nút "Create New" trong một khoảng thời gian ngắn (vd: 5 giây)
        print("Đang kiểm tra xem có popup 'Worksheet in progress' không (Luồng 2)...")
        create_new_button = page.get_by_role("button", name="Create New")
        
        # .click() đã có cơ chế chờ sẵn. Nếu nút không xuất hiện trong timeout, nó sẽ báo lỗi.
        create_new_button.click(timeout=5000) 
        
        print("Phát hiện Luồng 2: Đã tìm thấy và click nút 'Create New'.")

    except TimeoutError:
        # Nếu không tìm thấy nút "Create New" sau 5 giây, có nghĩa là ta đang ở Luồng 1
        print("Phát hiện Luồng 1: Không có popup 'Worksheet in progress'. Tiếp tục trực tiếp.")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL

    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url