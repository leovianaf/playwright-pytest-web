from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False, slow_mo=1000)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")

  # Types of get by (Locators)

  # # 1. get_by_role
  # btn = page.get_by_role("button", name="Default button")
  # btn.highlight()
  # btn.click()

  # heading = page.get_by_role("heading", name="Heading 2")
  # heading.highlight()
  # print(heading.text_content())

  # checkbox = page.get_by_role("checkbox", name="Default checkbox")
  # checkbox.highlight()
  # checkbox.check()

  # # 2. get_by_label
  # text_area = page.get_by_label("Example textarea")
  # text_area.highlight()
  # text_area.fill("Testing text area")

  # large_input = page.get_by_label("Large input")
  # large_input.highlight()
  # large_input.fill("big test")

  # # 3. get_by_placeholder
  # email_input = page.get_by_placeholder("Enter email")
  # email_input.highlight()
  # email_input.fill("test@email.com")

  # # 4. get_by_text
  # body_text = page.get_by_text("Example body text")
  # body_text.highlight()

  # btn = page.get_by_text("Small button")
  # btn.highlight()

  # page.get_by_text("fine print").highlight()              # This will get the first element with the text "fine print"
  # page.get_by_text("fine print", exact=True).highlight()  # This will get the element with the exact text "fine print"

  # 5. get_by_alt_text
  # page.goto("https://unsplash.com/pt-br")

  # page.get_by_alt_text("Casal desfruta do pequeno-almoço numa varanda com vista.").highlight()

  # # 6. get_by_title
  # page.get_by_title("attribute").highlight()


  # Using CSS selectors
  page.locator("h1") # This will get the first h1 element

  btn_outline_dark = page.locator("button.btn.btn-outline-dark") # This will get the button with the classes btn and btn-outline-dark
  btn_outline_dark.highlight()

  navbar_div = page.locator("div#navbarColor01") # This will get the div with the id navbarColor01
  navbar_div.highlight()

  btn_secondary_1 = page.locator("button.btn.btn-secondary:nth-of-type(1)") # This will get the first button with the classes btn and btn-secondary
  btn_secondary_1.highlight()
