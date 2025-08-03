import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "State/state_1.json"
AUTH_FILE_PATH_2 = "State/state_2.json"

#test hien thi popup add co teacher
def test_hien_thi_popup_co_teacher(browser: Browser) -> None:
    
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    #click add coteacher
    page.locator("#content-left-container").get_by_text("Add Co-Teacher").click()
    popup_add_co_teacher = page.get_by_role("dialog").locator("div").filter(has_text="Add Co-Teacher").nth(1)
    expect(popup_add_co_teacher).to_be_visible()

#test hien thi setting mac dinh popup add co teacher
def test_hien_thi_setting_mac_dinh_co_teacher(browser: Browser) -> None:
    
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    #click add coteacher
    page.locator("#content-left-container").get_by_text("Add Co-Teacher").click()
    page.locator(".btn-set").first.click()
    switch_end_assign = page.get_by_role("checkbox").first
    expect(switch_end_assign).not_to_be_checked()
    switch_change_setting = page.get_by_role("checkbox").nth(1)
    expect(switch_change_setting).not_to_be_checked()
    switch_comment = page.get_by_role("checkbox").nth(2)
    expect(switch_comment).to_be_checked()
    switch_edit_question = page.get_by_role("checkbox").nth(3)
    expect(switch_edit_question).not_to_be_checked()

#test trang thai setting student submit to co teacher khi chua cos hs join
def test_student_submit_to_co_teacher_chua_co_hs (browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    #click add coteacher
    page.locator("#content-left-container").get_by_text("Add Co-Teacher").click()
    switch_set_submit = page.get_by_role("checkbox")
    expect(switch_set_submit).not_to_be_checked()

#test invite mail co teacher
def test_invite_mail_co_teacher (browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    #click add coteacher
    page.locator("#content-left-container").get_by_text("Add Co-Teacher").click()
    page.get_by_role("textbox", name="Add people, groups or your").click()
    page.get_by_role("textbox", name="Add people, groups or your").fill("user2@abc-elearning.org")
    page.get_by_role("textbox", name="Add people, groups or your").press("Enter")
    page.get_by_role("button", name="Invite").click()
    row_co_teacher = page.locator("div").filter(has_text=re.compile(r"^user2user2@abc-elearning\.org$")).first
    expect(row_co_teacher).to_be_visible()

#test hien thi man co teacher duoc invite
def test_hien_thi_man_co_teacher (browser: Browser) -> None:
    try:
        context_1 = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context_1.new_page()
    page.goto("https://staging.worksheetzone.org/66068fa6b2412460610a4b10", wait_until="load")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        print("Không có popup 'Worksheet in progress'")
        pass
    #click add coteacher
    page.locator("#content-left-container").get_by_text("Add Co-Teacher").click()
    page.get_by_role("textbox", name="Add people, groups or your").click()
    page.get_by_role("textbox", name="Add people, groups or your").fill("user2@abc-elearning.org")
    page.get_by_role("textbox", name="Add people, groups or your").press("Enter")
    page.get_by_role("button", name="Invite").click()
    url_assign = page.url

    try:
        context_2 = browser.new_context(storage_state=AUTH_FILE_PATH_2)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_2}"
    page = context_2.new_page()
    page.goto(url_assign, wait_until="load")
    button_request = page.get_by_text("Request Access", exact=True)
    expect(button_request).to_be_hidden()
