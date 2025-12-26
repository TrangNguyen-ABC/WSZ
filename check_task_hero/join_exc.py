import re
from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    # Khởi chạy trình duyệt (headless=False để bạn có thể quan sát)
    browser = playwright.chromium.launch(headless=False)

    # Chạy vòng lặp 10 lần từ 1 đến 10
    for i in range(1, 2):
        email = f"{i}@gmail.com"
        print(f"Đang thực hiện lần thứ {i} với email: {email}")

        # Tạo context mới cho mỗi lần lặp để đảm bảo không bị dính session/cookie cũ
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto("https://staging.worksheetzone.org/join")
            
            page.get_by_role("textbox", name="Enter Code").click()
            page.get_by_role("textbox", name="Enter Code").fill("8KHBME")
            page.wait_for_timeout(2000)
            page.get_by_text("Go").click()

            # Nhập Email thay đổi theo biến i
            page.get_by_role("textbox", name="Enter email...").click()
            page.get_by_role("textbox", name="Enter email...").fill(email)
            page.get_by_role("button", name="Login").click()

            # Nhập OTP (Giữ nguyên theo code cũ của bạn)
            page.get_by_role("textbox", name="OTP Input 1").fill("2")
            page.get_by_role("textbox", name="OTP Input 2").fill("0")
            page.get_by_role("textbox", name="OTP Input 3").fill("2")
            page.get_by_role("textbox", name="OTP Input 4").fill("5")
            page.get_by_role("textbox", name="OTP Input 5").fill("T")
            page.get_by_role("textbox", name="OTP Input 6").fill("1")
            
            page.wait_for_timeout(3000) 
            page.get_by_role("button", name="Verify").click()
            page.wait_for_timeout(3000)

            page.get_by_text("Go").click()
            
            # Đợi một chút để quan sát kết quả trước khi đóng
            page.wait_for_timeout(10000)

        except Exception as e:
            print(f"Có lỗi xảy ra ở lần lặp {i}: {e}")
        
        finally:
            # Đóng context (tab/session) hiện tại để chuẩn bị cho lần lặp sau
            context.close()

    # Đóng trình duyệt sau khi hoàn thành 10 lần
    browser.close()

with sync_playwright() as playwright:
    run(playwright)