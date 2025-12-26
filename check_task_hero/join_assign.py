import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Mở trình duyệt một lần duy nhất
    browser = playwright.chromium.launch(headless=False)
    
    # Chạy vòng lặp từ 1 đến 5
    for i in range(1, 5):
        print(f"Đang thực hiện lần chạy thứ: {i}")
        
        # Tạo context và page mới cho mỗi lần chạy để đảm bảo dữ liệu sạch
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://worksheetzone.org/join/assign?code=G2D423&utm_source=link")
        
        # # Nhập Code
        # page.get_by_role("textbox", name="Enter Code").click()
        # page.get_by_role("textbox", name="Enter Code").fill("N5S0C9")
        # page.locator(".button-submit-value").click()
        
        # Nhập số thứ tự (chuyển i thành string)
        # Sử dụng f-string hoặc str(i)
        page.get_by_role("textbox", name="input").fill(str(i))
        
        # Nhấn Start
        page.get_by_text("Start", exact=True).click()
        
        # Đợi một chút để quan sát kết quả (tùy chọn)
        page.wait_for_timeout(4000) 
        
        # Đóng page/context sau khi xong một lượt
        context.close()
        print(f"Hoàn thành lần chạy thứ: {i}")

    # Đóng trình duyệt sau khi chạy xong 5 lần
    browser.close()

with sync_playwright() as playwright:
    run(playwright)