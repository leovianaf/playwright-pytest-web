from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  # Launch the browser
  browser = playwright.chromium.launch(headless=False, slow_mo=500)

  # Create a new page
  page = browser.new_page()

  # Navigate to the page
  page.goto("https://playwright.dev/python")

  # Locate a link element with text "Docs"
  # docs_button = page.locator("text=Docs")
  docs_button = page.get_by_role("link", name="Docs")
  docs_button.click()

  # Get the url of the current page
  print("Docs page:", page.url)

  # Close the browser
  browser.close()