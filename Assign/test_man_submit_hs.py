import re
import os
from dotenv import load_dotenv
from urllib.parse import urljoin
from playwright.sync_api import Page, expect, Browser

load_dotenv()
base_url = os.getenv("BASE_URL")

AUTH_FILE_PATH_1 = "State/state_1.json"

#assign không set nhiều lần làm bài
def test_man_submit_hs_khong_set_nhieu_lan_lam_bai(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto(urljoin(base_url,"678d198ce633858a58ac511d"), wait_until="load")
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
    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    page_1.locator("#id-overview-dialog-v2").get_by_text("Submit").click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    button_self_paced = page_1.locator("div").filter(has_text=re.compile(r"^Self-paced$")).nth(1)
    expect(button_self_paced).to_be_visible()

#Assign set nhiều lần làm lại - Quiz 
def test_man_submit_hs_set_nhieu_lan_lam_bai_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto(urljoin(base_url,"678d198ce633858a58ac511d"), wait_until="load")
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
    #edit participant attempt
    page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    page.get_by_role("textbox", name="1").click()
    page.get_by_role("textbox", name="1").fill("2")
    page.get_by_role("heading", name="Settings").locator("div").click()

    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    page_1.locator("#id-overview-dialog-v2").get_by_text("Submit").click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    button_reattempt = page_1.get_by_text("Reattempt")
    expect(button_reattempt).to_be_visible()

# #Assign set nhiều lần làm lại - non Quiz 
def test_man_submit_hs_set_nhieu_lan_lam_bai_non_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto(urljoin(base_url,"624a9507fb1abe3256a67f34"), wait_until="load")
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

    page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    page.get_by_role("textbox", name="1").click()
    page.get_by_role("textbox", name="1").fill("2")
    page.get_by_role("heading", name="Settings").locator("div").click()

    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    button_restart = page_1.locator(".btn-bottom-container")
    expect(button_restart).to_be_visible()

#check hiển thị khi Click button Restart 
def test_hien_thi_click_button_reattempt_non_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto(urljoin(base_url,"624a9507fb1abe3256a67f34"), wait_until="load")
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

    page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    page.get_by_role("textbox", name="1").click()
    page.get_by_role("textbox", name="1").fill("2")
    page.get_by_role("heading", name="Settings").locator("div").click()

    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    page_1.locator(".btn-bottom-container").click()
    popup_confirm_restart = page_1.get_by_text("ConfirmAre you sure you want")
    expect(popup_confirm_restart).to_be_visible()

#Check hiển thị khi click button Self-paced - quiz
def test_click_button_self_paced_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    page = context.new_page()
    page.goto(urljoin(base_url,"678d198ce633858a58ac511d"), wait_until="networkidle")
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
    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    page_1.locator("#id-overview-dialog-v2").get_by_text("Submit").click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    page_1.locator("div").filter(has_text=re.compile(r"^Self-paced$")).nth(1).click()
    expected_url = urljoin(base_url,"learning?worksheetid=678d198ce633858a58ac511d")
    expect(page_1).to_have_url(expected_url)

#Check hiển thị khi click button Self-paced - non quiz
def test_click_button_self_paced_non_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto(urljoin(base_url,"624a9507fb1abe3256a67f34"), wait_until="load")
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
    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    submit_button = page_1.locator("#id-overview-dialog-v2").get_by_text("Submit", exact=True)
    expect(submit_button).to_be_visible()
    submit_button.click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    page_1.locator("div").filter(has_text=re.compile(r"^Self-paced$")).nth(1).click()
    expected_url = urljoin(base_url,"adjectives-printable-interactive-624a9507fb1abe3256a67f34#practice")
    expect(page_1).to_have_url(expected_url)

#Check hiển thị khi bật setting Show feedback detail after submit - quiz 
def test_assign_show_feedback_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    page = context.new_page()
    page.goto(urljoin(base_url,"678d198ce633858a58ac511d"), wait_until="load")
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
    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    submit_button = page_1.locator("#id-overview-dialog-v2").get_by_text("Submit", exact=True)
    expect(submit_button).to_be_visible()
    submit_button.click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    des_congratulations = page_1.get_by_text("You have completed your")
    expect(des_congratulations).to_be_visible()

#Check hiển thị khi tắt setting Show feedback detail after submit - quiz 
def test_assign_show_feedback_quiz(browser: Browser) -> None:

    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1, permissions=["clipboard-read", "clipboard-write"])
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    page = context.new_page()
    page.goto(urljoin(base_url,"678d198ce633858a58ac511d"), wait_until="load")
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

    page.locator("div").filter(has_text=re.compile(r"^Settings$")).click()
    page.get_by_role("checkbox", name="controlled").nth(2).uncheck()
    page.get_by_role("heading", name="Settings").locator("div").click()

    khoi_invite_link = page.locator("div.value-invite").first
    link_join = khoi_invite_link.inner_text()
    print(link_join)
    page_1 = context.new_page()
    page_1.goto("https://"+link_join, wait_until="load")

    page_1.get_by_text("Start", exact=True).click()
    submit_button = page_1.locator("#id-overview-dialog-v2").get_by_text("Submit", exact=True)
    expect(submit_button).to_be_visible()
    submit_button.click()
    page_1.locator("div").filter(has_text=re.compile(r"^Still Submit$")).first.click()
    des_congratulations = page_1.get_by_text("You have completed your")
    expect(des_congratulations).to_be_visible()