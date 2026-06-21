Orion - Intelligent Website Automation Agent
By Amitabh Panda, 24BCS 10104
Overview

Orion is a web automation agent developed with Python and Playwright that can interact with websites without manual input.

The agent is capable of:

Launching a browser session
Visiting a specified webpage
Capturing screenshots during execution
Performing scrolling and mouse interactions
Identifying target forms on the page
Locating Bug Title and Description input fields
Automatically entering form data
Submitting forms
Recording all actions through detailed logs
Project Directory Structure
orion-main/
├── agent/
├── tools/
├── utils/
├── screenshots/
├── logs/
├── main.py
└── requirements.txt
Prerequisites

Before running Orion, ensure the following are installed:

Python 3.x
Playwright
Setup Instructions
1. Create a Virtual Environment
python -m venv venv
2. Activate the Environment

Linux/macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate
3. Install Required Packages
pip install -r requirements.txt
4. Install Playwright Browsers
playwright install
Execution

Start the automation agent with:

python main.py

Once executed, Orion will:

Launch a browser instance
Navigate to the configured website
Detect the relevant form
Populate the required fields
Submit the form automatically
Capture screenshots of key steps
Generate execution logs
Generated Outputs
Screenshots

Execution screenshots are stored in:

screenshots/
Logs

Detailed activity logs are available at:

logs/automation.log
Tech Stack
Python
Playwright
Python Logging Framework

Orion demonstrates automated browser interaction by intelligently navigating web pages, identifying form elements, entering information, and tracking every action performed during execution.
