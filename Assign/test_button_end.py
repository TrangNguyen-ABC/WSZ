import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_PRO_1 = "state_pro_1.json"
AUTH_FILE_PATH_PRO_2 = "state_pro_2.json"

#test hien thi button end trong assign moi tao setting mac dinh - teacher
def test_hien_thi_button_end_teacher_moi_tao_assign(browser: Browser) -> None:
    
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
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
    button_end = page.get_by_text("End", exact=True)
    expect(button_end).to_be_enabled()
    
#test hien thi button end - user duoc share
def test_hien_thi_button_end_user_duoc_share(browser: Browser) -> None:
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_PRO_1}")
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
    page.get_by_role("textbox", name="Add people, groups or your").fill("pro2@abc-elearning.org")
    page.get_by_role("textbox", name="Add people, groups or your").press("Enter")
    page.get_by_role("button", name="Invite").click()
    #copylink share 
    page.get_by_text("Copy link").click()
    clipboard_content = page.evaluate("navigator.clipboard.readText()")

    context_1.close()
    #mở context user duoc share
    try:
        context_2 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_2)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_2}"
    page = context_2.new_page()    
    page.goto(clipboard_content, wait_until="load")
    end_button_disable = page.locator(".button-end-assign:has-text('End')")
    expect(end_button_disable).to_be_visible()

#test hien thi button end - co teacher khong duoc set quyen
def test_hien_thi_button_end_man_co_teacher_khong_phan_quyen (browser: Browser) -> None:
    try:
        context_1 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
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
        context_2 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_2)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_2}"
    page = context_2.new_page()
    page.goto(url_assign, wait_until="load")
    end_button_disable = page.locator(".button-end-assign:has-text('End')")
    expect(end_button_disable).to_be_visible()

#Check trạng thái mặc định của button End (assign mới tạo) - co-teacher co quyen
def test_hien_thi_button_end_man_co_teacher_duoc_phan_quyen (browser: Browser) -> None:
    try:
        context_1 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
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
    page.locator(".btn-set").first.click()
    page.get_by_role("checkbox").first.check()
    url_assign = page.url

    try:
        context_2 = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_2)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_2}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_2}"
    page = context_2.new_page()
    page.goto(url_assign, wait_until="load")
    button_end = page.get_by_text("End", exact=True)
    expect(button_end).to_be_enabled()

#Check trạng thái button end sau khi tới due date (không set submit late)
def test_hien_thi_button_end_qua_due_date_khong_submitlate (browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/assign?code=V51QKF", wait_until="load")
    end_button_disable = page.locator(".button-end-assign:has-text('End')")
    expect(end_button_disable).to_be_visible()

#Check trạng thái button end sau khi tới due date (có set submit late)
def test_hien_thi_button_end_qua_due_date_co_submitlate (browser: Browser) -> None:
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/assign?code=EXWAW9", wait_until="load")
    button_end = page.get_by_text("End", exact=True)
    expect(button_end).to_be_enabled()

#Check hiển thị khi click button End (enable)
def test_hien_thi_khi_click_button_end (browser: Browser) -> None:
    
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
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
    page.get_by_text("End", exact=True).click()
    popup_confirm = page.get_by_role("dialog").locator("div").filter(has_text="ConfirmAre you sure you want").nth(1)
    expect(popup_confirm).to_be_visible()

#Check hiển thị button sau khi xác nhận end 
def test_hien_thi_button_end_sau_khi_xac_nhan (browser: Browser) -> None:
    
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_PRO_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_PRO_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_PRO_1}"
        
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
    page.get_by_text("End", exact=True).click()
    page.get_by_text("OK").click()
    end_button_disable = page.locator(".button-end-assign:has-text('End')")
    expect(end_button_disable).to_be_visible()
