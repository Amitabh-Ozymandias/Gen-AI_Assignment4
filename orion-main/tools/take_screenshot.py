from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger
from datetime import datetime

class take_screenShot:
  def execute(page, name):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = (
      f"screenshots/{name}_{timestamp}.png"
    )

    logger.info(f"Taking screenshot and saving to {screenshot_path}")
    page.screenshot(path=screenshot_path)

    logger.info("Screenshot is saved...")

