import asyncio
import pytest
from playwright.async_api import async_playwright, expect
from playwright_stealth import stealth_async

TARGET_URL = "https://worksheetzone.org/worksheets"

@pytest.mark.asyncio
async def test_bypass_cloudflare_with_stealth():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        # ÁP DỤNG STEALTH
        await stealth_async(context)

        page = await context.new_page()

        try:
            print(f"Đang truy cập vào: {TARGET_URL} với stealth")
            await page.goto(TARGET_URL, timeout=60000)

            print("Đã vào trang, chờ Cloudflare xác minh...")
            await page.wait_for_load_state('domcontentloaded', timeout=30000)
            
            main_content_header = page.locator('h1').first
            await expect(main_content_header).to_be_visible(timeout=20000)
            
            print(f"Thành công! Đã vượt qua Cloudflare. Tiêu đề trang: {await page.title()}")
            print(f"Nội dung H1: {await main_content_header.text_content()}")

        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")
            await page.screenshot(path="cloudflare_stealth_error.png")
            pytest.fail(f"Không thể vượt qua Cloudflare với stealth. Xem ảnh chụp màn hình: cloudflare_stealth_error.png")

        finally:
            await context.close()
            await browser.close()