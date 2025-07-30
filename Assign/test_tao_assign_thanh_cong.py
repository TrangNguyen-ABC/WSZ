import re
import os
from playwright.sync_api import Page, expect, Browser

AUTH_FILE_PATH_1 = "state_1.json"
AUTH_FILE_PATH_2 = "state_2.json"

#Check assign từ popup share - pdf + Quiz
def test_create_assign_success_from_popup_share_pdf_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ popup share pdf + quiz 
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/6392ed9571041f05f65d9f5f", wait_until="networkidle")
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
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL
        pass
    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()

#Check assign từ button Assign - Quiz
def test_create_assign_success_from_button_assign_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ button assign quiz 
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/678d198ce633858a58ac511d", wait_until="networkidle")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button share trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL
        pass
    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()

#Check assign từ button Assign - non quiz
def test_create_assign_success_from_button_assign_non_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ button assign non quiz 
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="networkidle")
    page.get_by_text("Assign").click() #click button Assign
    page.get_by_role("dialog").locator("div").filter(has_text=re.compile(r"^Assign$")).click() #click button Assign trên popup setting
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL
        pass
    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()

#Check tạo assign từ button Start Teaching Activities - Quiz 
def test_create_assign_success_from_landing_teaching_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ button assign quiz 
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/678d198ce633858a58ac511d", wait_until="networkidle")
    page.locator("div").filter(has_text=re.compile(r"^Start Teaching Activities$")).nth(1).click() #click button Start teaching
    page.locator("#select-game-screen").get_by_text("Assign Homework").click() #select activity assign
    page.get_by_text("Start", exact=True).click() #click button Start bên khối info phải
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL
        pass
    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()

#Check tạo assign từ button Start Teaching Activities - non Quiz 
def test_create_assign_success_from_landing_teaching_non_quiz(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ landing teaching non quiz
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/624a986cfb1abe3256a780ad", wait_until="networkidle")
    page.locator("div").filter(has_text=re.compile(r"^Start Teaching Activities$")).nth(1).click() #click button Start teaching
    page.locator("#select-game-screen").get_by_text("Assign Homework").click() #select activity assign
    page.get_by_text("Start", exact=True).click() #click button Start bên khối info phải
    print("Đang kiểm tra xem có popup 'Worksheet in progress' không...")
    create_button = page.get_by_text("Create New", exact=True)
    try:
        expect(create_button).to_be_visible(timeout=3000)
        print("phát hiện popup worksheet in progress")
        create_button.click()
    except AssertionError:
        # Nếu không tìm thấy nút "Create New" sau 3 giây, có nghĩa là ta đang ở Luồng 1
        print("Không có popup 'Worksheet in progress'")
        # Không cần làm gì cả, chỉ cần đi tiếp đến bước xác nhận URL
        pass
    # 6. BƯỚC CUỐI: Xác nhận URL cuối cùng
    print("Đang xác nhận URL cuối cùng...")
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()

#Check tạo assign từ tool 
def test_create_assign_success_from_tool(browser: Browser) -> None:
    """
    Test này kiểm tra tạo assign thành công từ tool
    """
    print(f"1. Đang nạp trạng thái đăng nhập từ: {AUTH_FILE_PATH_1}")
    # 4. Tạo một context mới và nạp trạng thái từ file auth.json
    try:
        context = browser.new_context(storage_state=AUTH_FILE_PATH_1)
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file state '{AUTH_FILE_PATH_1}'.")
        print("Vui lòng chạy script setup_auth.py để tạo file này trước.")
        assert False, f"File not found: {AUTH_FILE_PATH_1}"
        
    # Tạo một trang mới từ context đã có trạng thái đăng nhập
    page = context.new_page()
    page.goto("https://staging.worksheetzone.org/addition-worksheet-generator-create")
    page.get_by_text("Save").click()
    page.get_by_role("textbox", name="Enter title here...").click()
    page.get_by_role("textbox", name="Enter title here...").fill("1")
    page.get_by_role("textbox", name="Grade").click()
    page.get_by_text("Early Childhood").click()
    page.get_by_role("textbox", name="Tag").click()
    page.get_by_text("Behavior Worksheets").click()
    page.get_by_role("img", name="button-share").click()
    page.get_by_text("Assign", exact=True).click()
    page.get_by_role("dialog").get_by_text("Assign", exact=True).click()
    
    # expect().to_have_url() sẽ tự động chờ cho URL thay đổi
    # Sử dụng regex để khớp với bất kỳ mã code nào
    final_url_pattern = re.compile(r".*/assign\?code=")
    expect(page).to_have_url(final_url_pattern, timeout=10000) # Tăng timeout nếu chuyển trang chậm

    print(f"Thành công! URL cuối cùng là: {page.url}")
    assert "/assign?code=" in page.url
    context.close()