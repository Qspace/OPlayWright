from playwright.sync_api import sync_playwright, expect

def test_duckduckgo_search():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        
        # Create a new page
        page = browser.new_page()
        
        # Navigate to DuckDuckGo
        page.goto("https://duckduckgo.com/")
        
        # Type into the search box
        page.fill('input[name="q"]', "Playwright Python")
        
        # Click the search button
        page.click('button[type="submit"]')
        
        # Wait for the results page to load
        page.wait_for_selector('.results')
        
        # Check if the first result contains "Playwright"
        first_result = page.locator('.results .result__title').first
        expect(first_result).to_contain_text("Playwright")
        
        # Get the number of search results
        result_stats = page.locator('.results--main').count()
        print(f"Number of search results: {result_stats}")
        
        # Take a screenshot of the results page
        page.screenshot(path="duckduckgo_results.png")
        
        # Close the browser
        browser.close()

if __name__ == "__main__":
    test_duckduckgo_search()
