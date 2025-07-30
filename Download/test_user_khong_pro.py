import re
import os
from playwright.sync_api import Page, expect, Browser

# 2. Định nghĩa đường dẫn đến file state và thư mục download
AUTH_FILE_PATH_1 = "state_1.json"
AUTH_FILE_PATH_2 = "state_2.json"
DOWNLOAD_DIR = "Download/downloaded_not_pro"
# -----------------
def test_download_file_1_author_wsz(browser: Browser) -> None:
    """
    Test này kiểm tra chức năng download file đầu tiên trong ngày với author là wsz
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
    # --------------------------------
    print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
    # Tạo thư mục download nếu nó chưa tồn tại
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    # Đi đến trang có file cần tải
    page.goto("https://staging.worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
    print("Đang chờ và bắt sự kiện download...")
    with page.expect_download() as download_info:
        # Thực hiện hành động click để bắt đầu tải file
        page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()
    
    download = download_info.value
    
    suggested_filename = download.suggested_filename
    print(f"Tên file gốc được gợi ý: {suggested_filename}")

    save_path = os.path.join(DOWNLOAD_DIR, suggested_filename)

    download.save_as(save_path)
    print(f"File đã được lưu thành công tại: {save_path}")

    assert os.path.exists(save_path)
    print("Xác nhận: File tồn tại trên ổ đĩa.")
    print("Đóng context để dọn dẹp.")
    context.close()
    # ----------------

# def test_download_file_1_author_not_wsz(browser: Browser) -> None:
#     """
#     Test này kiểm tra chức năng download file đầu tiên trong ngày với author không phải là wsz
#     """
#     print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_2}")
#     # 4. Tạo một context mới và nạp trạng thái từ file auth.json
#     try:
#         context = browser.new_context(storage_state=AUTH_FILE_PATH_2)
#     except FileNotFoundError:
#         print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_2}'.")
#         print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
#         assert False, f"File not found: {AUTH_FILE_PATH_2}"
        
#     # Tạo một trang mới từ context đã có trạng thái đăng nhập
#     page = context.new_page()
#     # --------------------------------
#     print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
#     # Tạo thư mục download nếu nó chưa tồn tại
#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#     # Đi đến trang có file cần tải
#     page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
#     print("Đang chờ và bắt sự kiện download...")
#     with page.expect_download() as download_info:
#         # Thực hiện hành động click để bắt đầu tải file
#         page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()
    
#     download = download_info.value
    
#     suggested_filename = download.suggested_filename
#     print(f"Tên file gốc được gợi ý: {suggested_filename}")

#     save_path = os.path.join(DOWNLOAD_DIR, suggested_filename)

#     download.save_as(save_path)
#     print(f"File đã được lưu thành công tại: {save_path}")

#     assert os.path.exists(save_path)
#     print("Xác nhận: File tồn tại trên ổ đĩa.")
#     print("Đóng context để dọn dẹp.")
#     context.close()
#     # ----------------

# def test_download_file_2_author_wsz(browser: Browser) -> None:
#     """
#     Test này kiểm tra chức năng download file thứ 2 trong ngày với author là wsz
#     """
#     print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
#     # 4. Tạo một context mới và nạp trạng thái từ file auth.json
#     try:
#         context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
#     except FileNotFoundError:
#         print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
#         print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
#         assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
#     # Tạo một trang mới từ context đã có trạng thái đăng nhập
#     page = context.new_page()
#     # --------------------------------
#     print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
#     # Tạo thư mục download nếu nó chưa tồn tại
#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#     # Đi đến trang có file cần tải
#     page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
#     print("Đang chờ và bắt sự kiện download...")
#     with page.expect_download() as download_info:
#         # Thực hiện hành động click để bắt đầu tải file
#         page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()

#     popup_premium = page.locator(".popup-preview-download-content-body")
#     expect(popup_premium).to_be_visible()

#     context.close()
#     # ----------------

# def test_download_file_2_author_not_wsz(browser: Browser) -> None:
#     """
#     Test này kiểm tra chức năng download file thứ 2 trong ngày với author không phải là wsz
#     """
#     print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_2}")
#     # 4. Tạo một context mới và nạp trạng thái từ file auth.json
#     try:
#         context = browser.new_context(storage_state=AUTH_FILE_PATH_2)
#     except FileNotFoundError:
#         print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_2}'.")
#         print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
#         assert False, f"File not found: {AUTH_FILE_PATH_2}"
        
#     # Tạo một trang mới từ context đã có trạng thái đăng nhập
#     page = context.new_page()
#     # --------------------------------
#     print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
#     # Tạo thư mục download nếu nó chưa tồn tại
#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#     # Đi đến trang có file cần tải
#     page.goto("https://worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="networkidle")
    
#     print("Đang chờ và bắt sự kiện download...")
#     with page.expect_download() as download_info:
#         # Thực hiện hành động click để bắt đầu tải file
#         page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2).click()

#     download = download_info.value
    
#     suggested_filename = download.suggested_filename
#     print(f"Tên file gốc được gợi ý: {suggested_filename}")

#     save_path = os.path.join(DOWNLOAD_DIR, suggested_filename)

#     download.save_as(save_path)
#     print(f"File đã được lưu thành công tại: {save_path}")

#     assert os.path.exists(save_path)
#     print("Xác nhận: File tồn tại trên ổ đĩa.")
#     print("Đóng context để dọn dẹp.")
#     context.close()
#     # ----------------

# # Check hiển thị button download sau khi download WS đầu tiên trong ngày - WS của WSZ
# def test_UI_button_download_author_wsz(browser: Browser) -> None:
#     """
#     Test này kiểm tra hiển thị button download ws author wsz sau khi download free 1 lần trong ngày 
#     """
#     print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
#     # 4. Tạo một context mới và nạp trạng thái từ file auth.json
#     try:
#         context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
#     except FileNotFoundError:
#         print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
#         print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
#         assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
#     # Tạo một trang mới từ context đã có trạng thái đăng nhập
#     page = context.new_page()
#     # --------------------------------
#     print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
#     # Tạo thư mục download nếu nó chưa tồn tại
#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#     # Đi đến trang có file cần tải
#     page.goto("https://worksheetzone.org/6589048ce0c742310ac00797", wait_until="networkidle")
    
#     print("Đang chờ và bắt sự kiện download...")
#     # with page.expect_download() as download_info:
#     button_download =page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2)
#     expect(button_download).to_have_css("background", "#fff7e6")
#     context.close()

# # Check hiển thị button download sau khi download WS đầu tiên trong ngày - WS của user thường
# def test_UI_button_download_author_wsz(browser: Browser) -> None:
#     """
#     Test này kiểm tra hiển thị button download WS của user thường sau khi download free 1 lần trong ngày 
#     """
#     print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
#     # 4. Tạo một context mới và nạp trạng thái từ file auth.json
#     try:
#         context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
#     except FileNotFoundError:
#         print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
#         print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
#         assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
#     # Tạo một trang mới từ context đã có trạng thái đăng nhập
#     page = context.new_page()
#     # --------------------------------
#     print("Đã có trạng thái đăng nhập. Bắt đầu quy trình download...")
#     # Tạo thư mục download nếu nó chưa tồn tại
#     os.makedirs(DOWNLOAD_DIR, exist_ok=True)
#     # Đi đến trang có file cần tải
#     page.goto("https://staging.worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="networkidle")
    
#     print("Đang chờ và bắt sự kiện download...")
#     # with page.expect_download() as download_info:
#     button_download =page.locator("div").filter(has_text=re.compile(r"^Download$")).nth(2)
#     expect(button_download).to_have_css("background", "#fff")
#     context.close()