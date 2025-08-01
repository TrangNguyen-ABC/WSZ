import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "state_1.json"

#check cach vao man join
def test_cach_vao_man_join(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org", wait_until="load")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Enter Code").click()
    page1 = page1_info.value
    expected_url = "https://staging.worksheetzone.org/join"
    expect(page1).to_have_url(expected_url)

#Input code assign không hợp lệ 
def test_input_code_assign_khong_hop_le(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join", wait_until="load")
    page.get_by_role("textbox", name="Enter Code").click()
    page.get_by_role("textbox", name="Enter Code").fill("12345")
    page.locator(".button-submit-value").click()
    text_canh_bao = page.get_by_text("Please enter the valid code.")
    expect(text_canh_bao).to_be_visible()

#Input code assign đang trong hạn 
def test_input_code_assign_trong_han(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join", wait_until="load")
    page.get_by_role("textbox", name="Enter Code").click()
    page.get_by_role("textbox", name="Enter Code").fill("540910")
    page.locator(".button-submit-value").click()
    text_input_name = page.get_by_text("Your name is")
    expect(text_input_name).to_be_visible()

#Input code assign chưa tới start date 
def test_input_code_assign_chua_toi_startdate(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join", wait_until="load")
    page.get_by_role("textbox", name="Enter Code").click()
    page.get_by_role("textbox", name="Enter Code").fill("115ITL")
    page.locator(".button-submit-value").click()
    text_thong_bao = page.get_by_text("This assignment has not yet")
    expect(text_thong_bao).to_be_visible()

#Input code assign quá due date nhưng set allow submit late 
def test_input_code_assign_qua_due_date_submitlate(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join", wait_until="load")
    page.get_by_role("textbox", name="Enter Code").click()
    page.get_by_role("textbox", name="Enter Code").fill("406578")
    page.locator(".button-submit-value").click()
    text_input_name = page.get_by_text("Your name is")
    expect(text_input_name).to_be_visible()

#Input code assign đã hết hạn
def test_input_code_assign_het_han(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join", wait_until="load")
    page.get_by_role("textbox", name="Enter Code").click()
    page.get_by_role("textbox", name="Enter Code").fill("187414")
    page.locator(".button-submit-value").click()
    text_canh_bao = page.get_by_text("Sorry, this session has")
    expect(text_canh_bao).to_be_visible()

#check hiển thị name khi chưa login 
def test_hien_thi_name_chua_login(page: Page) -> None:

    page.goto("https://staging.worksheetzone.org/join/assign?code=540910", wait_until="load")
    input_name = page.get_by_role("textbox", name="input")
    expect(input_name).to_be_empty()
    page.get_by_text("Start", exact=True).click()
    text_canh_bao_input_name = page.get_by_text("Please write your name")
    expect(text_canh_bao_input_name).to_be_visible()

#Hiển thị name khi đã login 
def test_hien_thi_name_da_login(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/6392ed9571041f05f65d9f5f", wait_until="load")
    page.locator("div").filter(has_text=re.compile(r"^Share$")).click()
    page.get_by_text("Assign", exact=True).click()
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click()
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    input_name = page_1.get_by_role("textbox", name="input")
    expect(input_name).to_have_value("user1")
    page_1.get_by_text("Start", exact=True).click()
    expected_url_pattern = re.compile(r"https://staging.worksheetzone.org/join/assign\?code=\w+&pid=\w+")
    expect(page_1).to_have_url(expected_url_pattern)


