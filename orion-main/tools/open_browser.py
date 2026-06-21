from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger

class open_browser:

  def execute(url:str, playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch(headless=False)

    page = browser.new_page()
    logger.info(f"Navigating to webpage with url: {url}...")

    
    page.goto(url)

    return page, browser