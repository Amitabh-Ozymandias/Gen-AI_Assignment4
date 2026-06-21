# Orion - Website Automation Agent

## What Orion Does

Orion is a browser automation agent built using Python and Playwright.

The agent:

* Opens a browser
* Navigates to a target website
* Takes screenshots
* Scrolls and performs mouse actions
* Detects the required form on the page
* Finds the Bug Title and Description fields
* Fills the fields automatically
* Submits the form
* Logs all actions performed by the agent

---

## Project Structure

```text
orion-main/
├── agent/
├── tools/
├── utils/
├── screenshots/
├── logs/
├── main.py
└── requirements.txt
```

---

## Requirements

* Python 3
* Playwright

---

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browser:

```bash
playwright install
```

---

## Running Orion

Run:

```bash
python main.py
```

The agent will automatically:

1. Open the browser
2. Navigate to the target page
3. Find the form
4. Fill the fields
5. Submit the form
6. Save screenshots
7. Save execution logs

---

## Output

### Screenshots

All screenshots are saved inside:

```text
screenshots/
```

### Logs

Execution logs are saved inside:

```text
logs/automation.log
```

---

## Technologies Used

* Python
* Playwright
* Logging Module
