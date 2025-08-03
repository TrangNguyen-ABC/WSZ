import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "State/state_1.json"
AUTH_FILE_PATH_PRO_1 = "State/state_pro_1.json"

#test hien thi popup add user share
def test_hien_thi_popup_share_assign(browser: Browser) -> None:
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_PRO_1}")
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/assign?code=4ZADI7", wait_until="load")
    page.get_by_text("Report options").click()
    page.locator("div").filter(has_text=re.compile(r"^Share report$")).first.click()
    popup_share_assign = page.get_by_role("dialog").locator("div").filter(has_text="Share Assignment").nth(1)
    expect(popup_share_assign).to_be_visible()

#test click button copy link 
def test_link_copy_clipboard(browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/assign?code=4ZADI7", wait_until="load")
    page.get_by_text("Report options").click()
    page.locator("div").filter(has_text=re.compile(r"^Share report$")).first.click()
    page.get_by_text("Copy link").click()
    expected_link = "https://staging.worksheetzone.org/assign?code=4ZADI7&shared-report=true"
    clipboard_content = page.evaluate("navigator.clipboard.readText()")
    assert clipboard_content == expected_link

#test truy cap link share assign - chua login
def test_paste_link_report_user_chua_login (page: Page) -> None:
    page.goto("https://worksheetzone.org/assign?code=4ZADI7&shared-report=true", wait_until="load")
    expected_url = "https://worksheetzone.org/login"
    expect(page).to_have_url(expected_url)

#test truy cap link share assign - da login tk khac teacher, khac user duoc share
def test_paste_link_report_user_login_tk_khac (browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/assign?code=4ZADI7", wait_until="load")
    button_request = page.get_by_text("Request Access", exact=True)
    expect(button_request).to_be_visible()

#test add mail user duoc share
def test_add_mail_user_duoc_share(browser: Browser) -> None:
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_PRO_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
    page = context.new_page()    
    page.goto("https://staging.worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button Assign trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass

    page.get_by_text("Report options").click()
    page.locator("div").filter(has_text=re.compile(r"^Share report$")).first.click()
    page.get_by_role("textbox", name="Add people, groups or your").click()
    page.get_by_role("textbox", name="Add people, groups or your").fill("user1@abc-elearning.org")
    page.get_by_role("textbox", name="Add people, groups or your").press("Enter")
    page.get_by_role("button", name="Invite").click()
    row_user_invite = page.locator("div").filter(has_text=re.compile(r"^user1user1@abc-elearning\.org$")).first
    expect(row_user_invite).to_be_visible()

#test truy cap link share assign - user duoc share
def test_hien_thi_assign_user_duoc_share(browser: Browser) -> None:
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_PRO_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context_1 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
    page = context_1.new_page()    
    page.goto("https://staging.worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button Assign trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass

    page.get_by_text("Report options").click()
    page.locator("div").filter(has_text=re.compile(r"^Share report$")).first.click()
    #invite user
    page.get_by_role("textbox", name="Add people, groups or your").click()
    page.get_by_role("textbox", name="Add people, groups or your").fill("user1@abc-elearning.org")
    page.get_by_role("textbox", name="Add people, groups or your").press("Enter")
    page.get_by_role("button", name="Invite").click()
    #copylink share 
    page.get_by_text("Copy link").click()
    clipboard_content = page.evaluate("navigator.clipboard.readText()")

    context_1.close()
    #mở context user duoc share
    try:
        context_2 = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
    page = context_2.new_page()    
    page.goto(clipboard_content, wait_until="load")
    button_request = page.get_by_text("Request Access", exact=True)
    expect(button_request).to_be_hidden()