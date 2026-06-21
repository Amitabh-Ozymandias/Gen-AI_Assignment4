import os
from dotenv import load_dotenv
load_dotenv()

from agent.browserAgent import BrowserAgent

if __name__ == "__main__":
    url = os.getenv("TARGET_URL", "https://ui.shadcn.com/docs/forms/react-hook-form")
    title = os.getenv("BUG_TITLE", "Testing out Bug Title")
    description = os.getenv("BUG_DESCRIPTION", "This is the description for the bug")

    browserAgent = BrowserAgent()
    browserAgent.run(url, title, description)