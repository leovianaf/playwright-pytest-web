from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False, slow_mo=1000)
  page = browser.new_page()
  page.goto("https://bootswatch.com/default/")

  # Mouse actions

  # button = page.get_by_role("button", name="Block button").first

  # button.click()

  # button.dblclick()                            # Double click the button

  # button.dblclick(delay=500)                   # Double click the button with a delay of 500ms

  # # button.click(button="right")                 # Right click the button

  # button.click(button="middle")                # Middle click the button

  # button.click(modifiers=["Shift"])            # Click the button while holding the Shift key

  # button.click(modifiers=["Shift", "Control"]) # Click the button while holding the Shift and Control key

  # # Input functions

  # input = page.get_by_placeholder("Enter email")

  # input.fill("test@email.com")             # Just pass the text to the fill method

  # input.clear()                            # Clear the input field

  # input.type("teste@email.com")            # Type the text in the input field

  # input.clear()

  # input.type("teste@email.com", delay=200) # Type the text in the input field (simulating a human typing with a delay of 200ms)

  # valid_input = page.get_by_label("Valid input").first

  # print(valid_input.input_value())         # Check the value in the input field

  # Checkboxes, Radios and Switches

  checkbox = page.get_by_label("Default checkbox").first

  checkbox.check()                         # Check the checkbox
  checkbox.uncheck()                       # Uncheck the checkbox

  # Selectors

  select = page.get_by_label("Example select")
  select.scroll_into_view_if_needed()       # Scroll to the select field

  select.select_option("1")                 # Select the option with value 1
  select.select_option("2")                 # Select the option with value 2

  multi_select = page.get_by_label("Example multiple select")
  multi_select.highlight()

  multi_select.select_option(["1", "3", "5"]) # Select the options with value 1 and 2

  # Dropdowns
  dropdown = page.locator("button#btnGroupDrop1")
  dropdown.click()                            # Click the dropdown button

  dropdown_link = page.locator("div.dropdown-menu:visible a:text('Dropdown link')").last # Click the Action option in the dropdown
  dropdown_link.highlight()                   # Highlight the Action option in the dropdown
  dropdown_link.click()                       # Click the Action option in the dropdown

  # File upload
  file_input = page.get_by_label("Default file input example")
  file_input.scroll_into_view_if_needed()     # Scroll to the file input field
  file_input.set_input_files("example.txt")   # Upload the file example.txt
