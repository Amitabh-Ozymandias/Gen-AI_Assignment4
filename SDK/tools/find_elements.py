from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger
class find_elements:
  def form(page, name):
    forms = page.locator("form")

    for i in range(forms.count()):
      form = forms.nth(i)

      form_text = form.inner_text()

      if name in form_text:
        logger.info(f"Found the form with the title : {name}")
        return form

    logger.error(f"Did not find the form with the title : {name}")
    return None