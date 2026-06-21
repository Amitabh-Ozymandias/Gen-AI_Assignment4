import os
import asyncio
from dotenv import load_dotenv
load_dotenv()

from agent.browserAgent import BrowserAgent

async def main():
    url = os.getenv("TARGET_URL", "https://ui.shadcn.com/docs/forms/react-hook-form")
    title = os.getenv("BUG_TITLE", "Testing out Bug Title")
    description = os.getenv("BUG_DESCRIPTION", "This is the description for the bug")

    browserAgent = BrowserAgent()
    await browserAgent.run(url, title, description)

if __name__ == "__main__":
    asyncio.run(main())