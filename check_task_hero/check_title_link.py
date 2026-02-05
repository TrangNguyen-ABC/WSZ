import pandas as pd
from playwright.sync_api import sync_playwright
import time

def check_links(input_file, output_file):
    # 1. Đọc file Excel (giả định cột URL là cột đầu tiên)
    df = pd.read_excel(input_file)
    # Lấy danh sách URL từ cột đầu tiên (hoặc tên cột 'URL' nếu có)
    urls = df.iloc[:, 0].tolist()
    
    results = []

    with sync_playwright() as p:
        # Mở trình duyệt (headless=True để chạy ẩn, False nếu muốn xem quá trình)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in urls:
            # Kiểm tra nếu url hợp lệ
            if pd.isna(url) or not str(url).startswith('http'):
                print(f"Bỏ qua URL không hợp lệ: {url}")
                results.append("Fail (Invalid URL)")
                continue

            print(f"Đang kiểm tra: {url}")
            try:
                # Truy cập link, đợi tối đa 30s
                response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
                
                # Lấy Title của trang
                title = page.title()
                
                # Logic so sánh title hoặc Status Code
                # Đôi khi lỗi 410 không hiện title mà trả về status code 410
                status_code = response.status if response else None
                
                if title == "410 Gone" or status_code == 410:
                    results.append("") # Để trống nếu đúng là 410 Gone
                else:
                    results.append("Fail")
                    
            except Exception as e:
                # Nếu không load được trang hoặc bị lỗi kết nối
                print(f"Lỗi khi truy cập {url}: {e}")
                results.append("Fail")

        browser.close()

    # 2. Tạo DataFrame mới cho kết quả
    new_df = pd.DataFrame({
        'URL': urls,
        'Kết quả': results
    })

    # 3. Xuất ra file Excel mới
    new_df.to_excel(output_file, index=False)
    print(f"--- Hoàn thành! Kết quả đã được lưu vào {output_file} ---")

# --- Cấu hình tên file ---
input_excel = "test_1.xlsx"  # Thay bằng tên file thực tế của bạn
output_excel = "ket_qua_check.xlsx"

if __name__ == "__main__":
    check_links(input_excel, output_excel)