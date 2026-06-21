from playwright.sync_api import sync_playwright, Playwright
from utils.logger import logger

class mouse_events:

  def scrollDown(page):
    logger.info("Scrolling down...")
    page.mouse.wheel(0, 500)
    page.wait_for_timeout(1000)

  def scrollUp(page):
    logger.info("Scrolling up...")
    page.mouse.wheel(0, -500)
    page.wait_for_timeout(1000)

  def smooth_scroll(page, total_distance=2000, steps=10):
    """Scroll smoothly in small increments to simulate natural user scrolling."""
    step_size = total_distance // steps
    direction = 1 if total_distance >= 0 else -1
    logger.info(f"Smooth scrolling {'down' if direction > 0 else 'up'} {abs(total_distance)}px over {steps} steps...")
    for i in range(steps):
      page.mouse.wheel(0, step_size)
      page.wait_for_timeout(150)
    page.wait_for_timeout(500)
    logger.info("Smooth scroll complete.")

  def click(page, x, y):
    logger.info(f"Clicking at x={x}, y={y}...")
    page.mouse.click(x, y)
    page.wait_for_timeout(1000)

  def double_click(page, x, y):
    logger.info(f"Double clicking at x={x}, y={y}...")
    page.mouse.dblclick(x, y)
    page.wait_for_timeout(1000)