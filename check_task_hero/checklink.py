import pandas as pd
from playwright.sync_api import sync_playwright
import time

def check_worksheet_links(input_file, output_file):
    # 1. Đọc file Excel
    # header=None vì file của bạn dường như không có tiêu đề cột ở dòng 1
    try:
        df = pd.read_excel(input_file, header=None)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_file}'")
        return

    # Link mục tiêu để so sánh
    removed_url = "https://worksheetzone.org/removed-resource"
    base_url = "https://worksheetzone.org/"

    results = [] # Danh sách lưu kết quả

    # 2. Khởi động Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # 3. Duyệt qua từng dòng trong file Excel
        for index, row in df.iterrows():
            slug = str(row[0]).strip() # Lấy giá trị cột A và xóa khoảng trắng thừa
            
            # Bỏ qua nếu ô trống
            if not slug or slug == 'nan':
                results.append("Empty")
                continue

            target_link = base_url + slug
            print(f"Đang kiểm tra ({index+1}): {target_link}")

            try:
                # Truy cập link và đợi load xong
                page.goto(target_link, timeout=30000) # Timeout 30s
                
                # Đợi một chút để đảm bảo redirect hoàn tất (nếu cần)
                page.wait_for_load_state("networkidle")

                # Lấy URL hiện tại sau khi truy cập
                current_url = page.url

                # So sánh với link removed
                if current_url == removed_url:
                    status = "REMOVED"
                else:
                    # Có thể link sống hoặc chuyển hướng sang trang khác
                    status = f"Alive (Redirected to: {current_url})"
            
            except Exception as e:
                status = f"Error: {str(e)}"
            
            results.append(status)

        browser.close()

    # 4. Ghi kết quả vào file Excel mới
    df['Check Result'] = results # Thêm cột kết quả
    df.to_excel(output_file, index=False, header=False)
    print(f"\nĐã hoàn thành! Kết quả được lưu tại: {output_file}")

# --- CẤU HÌNH ---
# Tên file Excel đầu vào của bạn 
input_excel_name = 'Book2.xlsx' 
# Tên file kết quả đầu ra 
output_excel_name = 'ket_qua_kiem_tra.xlsx'

# Chạy hàm
if __name__ == "__main__":
    check_worksheet_links(input_excel_name, output_excel_name)