import os
from playwright.sync_api import Browser, sync_playwright, expect

AUTH_FILE_PATH_1 = "state_1.json"
# Khai báo một User-Agent cố định
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

def test_create_assign_success_from_popup_share_quiz(browser: Browser) -> None:
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    
    try:
        # QUAN TRỌNG: Thêm user_agent vào đây
        context = browser.new_context(
            storage_state=AUTH_FILE_PATH_1,
            user_agent=USER_AGENT 
        )
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    page = context.new_page()
    
    # Chạy ở chế độ Non-headless để xem chuyện gì xảy ra
    # Bạn sẽ thấy nó có bị chuyển hướng về trang login hay không
    print("2. Đang truy cập vào trang quiz...")
    page.goto("https://staging.worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
    # Thêm một bước kiểm tra để xác nhận
    # Ví dụ: kiểm tra xem avatar người dùng có xuất hiện không
    try:
        # Giả sử có một element định danh cho người dùng đã đăng nhập, ví dụ: 'div.user-avatar'
        expect(page.locator('div.user-avatar')).to_be_visible(timeout=5000)
        print("Xác nhận: Đăng nhập thành công, thấy avatar người dùng.")
    except Exception:
        print("Xác nhận: ĐĂNG NHẬP THẤT BẠI. Không tìm thấy avatar người dùng.")
        page.screenshot(path="login_failed.png")
        assert False, "Không thể duy trì phiên đăng nhập bằng state file."