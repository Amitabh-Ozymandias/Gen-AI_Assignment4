import os
import json
import asyncio
from playwright.async_api import async_playwright
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

class BrowserAgent:
    async def run(self, url: str, title: str, description: str):
        print("=" * 60)
        print("Orion AI is starting custom Playwright agent...")
        print("=" * 60)

        github_token = os.environ.get("GITHUB_TOKEN")
        if not github_token or github_token == "your_github_model_api_key_here":
            print("ERROR: GITHUB_TOKEN environment variable is not set correctly in .env")
            return

        llm = ChatOpenAI(
            model="gpt-4o",
            api_key=github_token,
            base_url="https://models.inference.ai.azure.com",
            max_tokens=2000,
            model_kwargs={"response_format": {"type": "json_object"}}
        )

        print("Launching browser...")
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            
            print(f"Navigating to {url}...")
            await page.goto(url)
            await page.wait_for_load_state('networkidle')
            
            print("Scrolling down to reveal form...")
            await page.evaluate("window.scrollBy(0, 500)")
            await asyncio.sleep(1) # wait for any lazy loading
            
            print("Extracting page inputs and buttons...")
            # Extract basic interactive elements to send to the AI
            elements_script = """
            () => {
                const elements = [];
                // Prioritize main content area to avoid giant sidebars
                const scope = document.querySelector('main') || document.body;
                scope.querySelectorAll('input, textarea, button').forEach((el, index) => {
                    const rect = el.getBoundingClientRect();
                    // Skip tiny/hidden elements and limit total items
                    if (rect.width > 10 && rect.height > 10 && elements.length < 30) {
                        elements.push({
                            tag: el.tagName.toLowerCase(),
                            type: el.type || '',
                            id: el.id || '',
                            name: el.name || '',
                            placeholder: el.placeholder || '',
                            text: (el.innerText || el.value || '').substring(0, 50).trim(),
                        });
                    }
                });
                return elements;
            }
            """
            elements_data = await page.evaluate(elements_script)
            
            print("Asking AI to identify correct selectors...")
            prompt = f"""
            You are an AI browser agent. I have extracted all visible inputs and buttons from the page: {url}.
            Your task is to identify the CSS selectors needed to:
            1. Fill in the "Bug Title" field.
            2. Fill in the "Description" field (or textarea).
            3. Click the "Submit" button.

            Here are the interactive elements on the page:
            {json.dumps(elements_data, indent=2)}

            Output a valid JSON object with the following exact keys:
            - "title_selector": (a valid css selector to target the Bug Title input)
            - "description_selector": (a valid css selector to target the Description textarea/input)
            - "submit_selector": (a valid playwright css selector to target the Submit button, e.g. "button:has-text('Submit')" or "button[type='submit']". DO NOT use jQuery pseudo-classes like :contains!)
            
            Do not include any other text, only the JSON.
            """
            
            response = await llm.ainvoke([
                SystemMessage(content="You return strictly JSON. Do not include markdown formatting or backticks around the json."),
                HumanMessage(content=prompt)
            ])
            
            # Parse AI response
            try:
                # Clean up potential markdown formatting
                response_text = response.content.strip()
                if response_text.startswith("```json"):
                    response_text = response_text[7:-3]
                elif response_text.startswith("```"):
                    response_text = response_text[3:-3]
                
                selectors = json.loads(response_text)
                title_sel = selectors.get("title_selector")
                desc_sel = selectors.get("description_selector")
                submit_sel = selectors.get("submit_selector")
                
                print(f"AI identified selectors:\\n  Title: {title_sel}\\n  Description: {desc_sel}\\n  Submit: {submit_sel}")
                
                print(f"Filling Bug Title with: {title}")
                await page.fill(title_sel, title)
                await asyncio.sleep(0.5)
                
                print(f"Filling Description with: {description}")
                await page.fill(desc_sel, description)
                await asyncio.sleep(0.5)
                
                print("Taking pre-submit screenshot...")
                await page.screenshot(path="screenshot_pre_submit.png")
                
                print("Clicking Submit...")
                await page.click(submit_sel)
                await asyncio.sleep(2)
                
                print("Taking post-submit screenshot...")
                await page.screenshot(path="screenshot_post_submit.png")
                
                print("Actions completed successfully!")
                
            except Exception as e:
                print("Failed to execute AI instructions:", str(e))
                print("AI Response was:", response.content)
            
            finally:
                print("Closing browser...")
                await browser.close()
                
        print("=" * 60)
        print("Orion AI finished successfully!")
        print("=" * 60)
