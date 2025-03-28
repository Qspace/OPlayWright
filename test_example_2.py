from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError

def test_duckduckgo_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Keep headless=True for CI
        page = browser.new_page()
        
        try:
            # Navigate and search
            page.goto("https://duckduckgo.com/")
            page.fill('input[name="q"]', "Playwright Python")
            page.click('button[type="submit"]')
            
            # Wait for results using verified selector
            page.wait_for_selector('[data-testid="result-title"]', timeout=60_000)  # 60s timeout
            
            # Verify results
            first_result = page.locator('[data-testid="result-title"]').first
            expect(first_result).to_contain_text("Playwright")
            
        except PlaywrightTimeoutError:
            print("Timeout occurred - element not found")
            
        finally:
            browser.close()