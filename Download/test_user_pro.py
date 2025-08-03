import pytest
import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin # Thư viện chuẩn để nối URL một cách an toàn
from playwright.sync_api import Page, expect, Browser

# Tải các biến môi trường từ file .env vào chương trình
load_dotenv()
# Lấy giá trị của biến BASE_URL từ môi trường
# Nếu không tìm thấy, giá trị sẽ là None
base_url = os.getenv("BASE_URL")

# Định nghĩa đường dẫn đến file state và thư mục download
AUTH_FILE_PATH_1 = "State/state_pro_1.json"
AUTH_FILE_PATH_2 = "State/state_pro_2.json"
DOWNLOAD_DIR = "Download/downloaded_pro"
# -----------------
@pytest.mark.parametrize("run_number", [1, 2])
def test_download_file_1_author_wsz(browser: Browser, run_number: int) -> None:
    """
    Test này kiểm tra chức năng download file đầu tiên, thứ 2 trong ngày với author là wsz
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    
    # --- PHẦN LOGIN SỬ DỤNG STATE ---
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
    page.goto(urljoin(base_url,"6589048ce0c742310ac00797"), wait_until="load")
    
    print("Đang chờ và bắt sự kiện download...")
    with page.expect_download() as download_info:
        # Thực hiện hành động click để bắt đầu tải file
        page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()
    
    download = download_info.value
    
    suggested_filename = download.suggested_filename
    print(f"Tên file gốc được gợi ý: {suggested_filename}")

    base, ext = os.path.splitext(suggested_filename)
    unique_filename = f"{base}-run{run_number}{ext}"
    save_path = os.path.join(DOWNLOAD_DIR, unique_filename)

    # Lưu file vào vị trí mong muốn
    download.save_as(save_path)
    print(f"File đã được lưu thành công tại: {save_path}")

    assert os.path.exists(save_path)
    print("Xác nhận: File tồn tại trên ổ đĩa.")
    # --------------------------------------------

    # 5. Đóng context sau khi đã hoàn thành test
    print("Đóng context để dọn dẹp.")
    context.close()
    # ----------------

@pytest.mark.parametrize("run_number", [1, 2])
def test_download_file_1_author_not_wsz(browser: Browser, run_number: int) -> None:
    """
    Test này kiểm tra chức năng download file đầu tiên, thứ 2 trong ngày với author k phải là wsz
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_2}")
    
    # --- PHẦN LOGIN SỬ DỤNG STATE ---
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_2)
    except FileNotFoundError:
        # Thêm một thông báo lỗi thân thiện nếu file auth không tồn tại
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_2}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    # --------------------------------

    print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
    # Tạo thư mục download nếu nó chưa tồn tại
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    # Đi đến trang có file cần tải
    page.goto(urljoin(base_url,"624a986cfb1abe3256a780ad"), wait_until="load")
    
    print("Đang chờ và bắt sự kiện download...")
    with page.expect_download() as download_info:
        # Thực hiện hành động click để bắt đầu tải file
        page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()
    
    download = download_info.value
    
    suggested_filename = download.suggested_filename
    print(f"Tên file gốc được gợi ý: {suggested_filename}")

    base, ext = os.path.splitext(suggested_filename)
    unique_filename = f"{base}-run{run_number}{ext}"
    save_path = os.path.join(DOWNLOAD_DIR, unique_filename)

    # Lưu file vào vị trí mong muốn
    download.save_as(save_path)
    print(f"File đã được lưu thành công tại: {save_path}")

    assert os.path.exists(save_path)
    print("Xác nhận: File tồn tại trên ổ đĩa.")
    # --------------------------------------------

    # 5. Đóng context sau khi đã hoàn thành test
    print("Đóng context để dọn dẹp.")
    context.close()
    # ----------------