import re
import os
from playwright.sync_api import Page, expect, Browser

# 2. Định nghĩa đường dẫn đến file state và thư mục download
AUTH_FILE_PATH_1 = "state_pro_1.json"
AUTH_FILE_PATH_2 = "state_pro_2.json"
DOWNLOAD_DIR = "Download/downloaded_pro"
# -----------------
def test_navigate_landing_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra chức năng chuyển hướng sang landing print quiz
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        # Thêm một thông báo lỗi thân thiện nếu file auth không tồn tại
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    # --------------------------------

    print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
    # Tạo thư mục download nếu nó chưa tồn tại
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    # Đi đến trang có file cần tải
    page.goto("https://worksheetzone.org/good-or-bad-choices--6646cb7bd37ce56585f87734?pdfId=6589048ce0c742310ac00797", wait_until="networkidle")
    
    page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(4).click()
    with page.expect_download() as download2_info:
        page.locator("div").filter(has_text=re.compile(r"^Worksheet$")).click()
    # download2 = download2_info.value
    page.get_by_role("link", name="Switch question formats").click()
    expect(page).to_have_url("https://worksheetzone.org/print?worksheetId=6646cb7bd37ce56585f87734")
    page.wait_for_timeout(3000)

    context.close()
    # ----------------

def test_navigate_landing_PDF(browser: Browser) -> None:
    """
    Test này kiểm tra chức năng chuyển hướng sang landing download ws PDF
    """
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        # Thêm một thông báo lỗi thân thiện nếu file auth không tồn tại
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo fi" \
        "le này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    # --------------------------------

    print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
    # Tạo thư mục download nếu nó chưa tồn tại
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    # Đi đến trang có file cần tải
    page.goto("https://worksheetzone.org/practice-handwriting-online?worksheetId=6588f117e0c742310abfe02f", wait_until="networkidle")
    
    page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(4).click()
    with page.expect_download() as download2_info:
        page.locator("div").filter(has_text=re.compile(r"^Worksheet$")).click()
    # download2 = download2_info.value
    page.get_by_role("link", name="Switch question formats").click()
    expect(page).to_have_url("https://worksheetzone.org/print?worksheetId=6646cb7bd37ce56585f87734")
    page.wait_for_timeout(3000)

    context.close()
    # ----------------