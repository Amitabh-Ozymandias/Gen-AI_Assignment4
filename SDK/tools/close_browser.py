from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger

class close_browser:

  def execute(browser):
    logger.info("Closing browser...")
    browser.close()
    