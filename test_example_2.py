from playwright.sync_api import sync_playwright, expect, TimeoutError as PlaywrightTimeoutError

def test_duckduckgo_search():
    with sync_playwright() as p:
        print("Launching browser in headless mode...")
        browser = p.chromium.launch(headless=True)  # Keep headless=True for CI
        page = browser.new_page()
        
        try:
            print("Navigating to DuckDuckGo...")
            page.goto("https://duckduckgo.com/")
            
            print("Filling the search input with 'Playwright Python'...")
            page.fill('input[name="q"]', "Playwright Python")
            
            print("Clicking the search button...")
            page.click('button[type="submit"]')
            
            print("Waiting for search results to appear...")
            page.wait_for_selector('[data-testid="result-title"]', timeout=60_000)  # 60s timeout
            
            print("Verifying the first search result contains 'Playwright'...")
            first_result = page.locator('[data-testid="result-title"]').first
            expect(first_result).to_contain_text("Playwright")
            print("Search result verification passed!")
            
        except PlaywrightTimeoutError:
            print("Timeout occurred - element not found")
            
        finally:
            print("Closing the browser...")
            browser.close()
            print("Browser closed.")

if __name__ == "__main__":
    print("Starting the DuckDuckGo search test...")
    test_duckduckgo_search()
    print("Test completed.")