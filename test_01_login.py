import re
import os
import pytest
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect

load_dotenv()
base_url = os.getenv("BASE_URL")

# Tạo một list các cấu hình cần test
auth_configs = [
    (os.getenv("EMAIL_PRO_1"), os.getenv("PASSWORD"), "State/state_pro_1.json"),
    (os.getenv("EMAIL_PRO_2"), os.getenv("PASSWORD"), "State/state_pro_2.json"),
    (os.getenv("EMAIL_USER_1"), os.getenv("PASSWORD"), "State/state_1.json"),
    (os.getenv("EMAIL_USER_2"), os.getenv("PASSWORD"), "State/state_2.json")
]

@pytest.mark.parametrize("email, password, state_file", auth_configs)
def test_create_auth_states(page: Page, email, password, state_file):
    """
    Test case này được parametrize để tạo ra nhiều file state
    cho các user khác nhau chỉ với một lần viết code.
    """
    if os.path.exists(state_file):
        os.remove(state_file)
        print(f"Đã xóa file state cũ: '{state_file}'")

    print(f"Bắt đầu quy trình đăng nhập để tạo file state: '{state_file}'")
    
    page.goto(urljoin(base_url,"650914a3efe5de5722941721"), wait_until="load")
    # #scroll để hiển thị popup intro clr 
    # button_explore_ss_2= page.get_by_role("link", name="Explore")
    # button_explore_ss_2.scroll_into_view_if_needed()
    # page.locator("div").filter(has_text=re.compile(r"^Introducing Class Management$")).locator("div").click()
    #login
    page.get_by_text("Login").click()
    page.get_by_role("textbox", name="yourname@gmail.com").fill(email)
    page.get_by_role("button", name="Verify").click()
    page.get_by_role("textbox", name="Enter your code here").fill(password)
    page.get_by_role("button", name="Submit").click()

    page.wait_for_timeout(3000)
    print(f"Đăng nhập thành công với user: {email}")

    page.context.storage_state(path=state_file)
    print(f"Đã lưu trạng thái đăng nhập vào file: '{state_file}'")

    assert os.path.exists(state_file), f"File state '{state_file}' đã không được tạo!"
    print(f"Xác nhận: File '{state_file}' đã tồn tại.")