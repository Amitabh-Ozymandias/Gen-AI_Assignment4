from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger
from tools.open_browser import open_browser
from tools.take_screenshot import take_screenShot
from tools.mouse_events import mouse_events
from tools.close_browser import close_browser
from tools.find_elements import find_elements

class BrowserAgent:
  def run(self, url: str, title: str, description: str):

    with sync_playwright() as playwright:
      logger.info("=" * 60)
      logger.info("Orion is starting...")
      logger.info("=" * 60)

      # ── Step 1: Open browser ───────────────────────────────────
      logger.info("Opening browser...")
      page, browser = open_browser.execute(url, playwright)
      page.wait_for_load_state("networkidle")
      take_screenShot.execute(page, "01_browser_launched")

      # ── Step 2: Smooth scroll down to explore the page ─────────
      logger.info("Auto-scrolling down the page...")
      mouse_events.smooth_scroll(page, total_distance=1000, steps=8)
      take_screenShot.execute(page, "02_after_scroll_down_1")

      mouse_events.smooth_scroll(page, total_distance=1000, steps=8)
      take_screenShot.execute(page, "03_after_scroll_down_2")

      mouse_events.smooth_scroll(page, total_distance=1000, steps=8)
      take_screenShot.execute(page, "04_after_scroll_down_3")

      # ── Step 3: Scroll back up to top ──────────────────────────
      logger.info("Scrolling back to top of page...")
      mouse_events.smooth_scroll(page, total_distance=-3000, steps=12)
      take_screenShot.execute(page, "05_scrolled_back_to_top")

      # ── Step 4: Find the form ───────────────────────────────────
      logger.info("Searching for the form on the page...")
      form = find_elements.form(page, "Bug Title")

      if form is None:
        logger.error("Could not find the form. Aborting automation.")
        close_browser.execute(browser)
        return

      # Scroll form into view
      form.scroll_into_view_if_needed()
      page.wait_for_timeout(800)
      take_screenShot.execute(page, "06_form_found")

      # ── Step 5: Fill Bug Title field ────────────────────────────
      logger.info(f"Filling 'Bug Title' field with: {title}")
      title_field = form.get_by_label("Bug Title")
      title_field.click()
      page.wait_for_timeout(300)
      title_field.fill(title)
      page.wait_for_timeout(500)
      take_screenShot.execute(page, "07_title_filled")

      # ── Step 6: Fill Description field ──────────────────────────
      logger.info(f"Filling 'Description' field with: {description}")
      description_field = form.get_by_label("Description")
      description_field.click()
      page.wait_for_timeout(300)
      description_field.fill(description)
      page.wait_for_timeout(500)
      take_screenShot.execute(page, "08_description_filled")

      # ── Step 7: Screenshot of completed form ────────────────────
      logger.info("Form fully filled. Taking pre-submit screenshot...")
      take_screenShot.execute(page, "09_form_ready_to_submit")

      # ── Step 8: Submit the form ─────────────────────────────────
      logger.info("Submitting the form...")
      page.get_by_role("button", name="Submit").click()
      page.wait_for_timeout(3000)
      take_screenShot.execute(page, "10_form_submitted")

      # ── Step 9: Close browser cleanly ──────────────────────────
      logger.info("Automation complete. Closing browser...")
      close_browser.execute(browser)

      logger.info("=" * 60)
      logger.info("Orion finished successfully!")
      logger.info("Screenshots saved in: ./screenshots/")
      logger.info("Logs saved in:        ./logs/automation.log")
      logger.info("=" * 60)