from playwright.sync_api import sync_playwright
from time import perf_counter

def on_dialog(dialog):
  print(f"Dialog message: {dialog.message}")
  dialog.accept()  # Accept the dialog
  # dialog.dismiss()  # Dismiss the dialog
  # dialog.message()  # Get the message of the dialog

with sync_playwright() as playwright:
  browser = playwright.chromium.launch(headless=False, slow_mo=1000)

  page = browser.new_page()

  # Custom waiting
  page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

  link = page.get_by_role("link", name="2015")
  link.click()

  print("Loading oscars for 2015...")
  start = perf_counter()

  first_td = page.locator("td.film-title").first
  first_td.wait_for(timeout=20000)  # Wait for the first td element to be visible

  time_taken = perf_counter() - start
  print(f"...movies are loaded, in {round(time_taken, 2)}s!")

  # Dialog events
  page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

  page.on("dialog", on_dialog)

  page.get_by_text("Show confirm box").click()

  # Download files
  page.goto("https://unsplash.com/pt-br/fotografias/um-carro-toyota-amarelo-esportivo-e-visto-T6yHP1JoMH8")

  btnDownload = page.get_by_role("link", name="Baixar gratuitamente")

  with page.expect_download() as download_info:
    btnDownload.click()

  download = download_info.value
  download.save_as("carro.jpg")  # Save the file with the name carro.jpg

  browser.close()
