import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False, slow_mo=500)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://staging.worksheetzone.org/", wait_until="networkidle")
    await page.locator("div").filter(has_text=re.compile(r"^Introducing Class Management$")).locator("div").click()
    await page.get_by_text("Login").click()
    await page.get_by_role("textbox", name="yourname@gmail.com").fill("user1@abc-elearning.org")
    await page.get_by_role("button", name="Verify").click()
    await page.get_by_role("textbox", name="Enter your code here").click()
    await page.get_by_role("textbox", name="Enter your code here").fill("TESTER-DEV-ABC")
    await page.get_by_role("button", name="Submit").click()
    await page.wait_for_timeout(3000) 
    # storage_state = await context.storage_state(path="state_pro_2.json")
    # storage_state = await context.storage_state(path="state_pro_2.json")
    # storage_state = await context.storage_state(path="state_1.json")
    storage_state = await context.storage_state(path="state_1.json")


    print("Đã lưu trạng thái đăng nhập vào file 'state_1.json'")
    # await page.wait_for_timeout(3000)

    # ---------------------
    await context.close() 
    await browser.close() 


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
