# Cape Town Local Information Web Scraper

A beginner-friendly Python project using Requests and Beautiful Soup to extract information from the Cape Town Wikipedia article.

## What it extracts
- Introductory paragraphs
- Facts from the article infobox (when available)
- Article section headings
- Links to related Wikipedia articles

## Technologies
- Python 3
- Requests
- Beautiful Soup 4

## Files
- `main.py` — web-scraping program
- `requirements.txt` — required Python packages
- `.gitignore` — excludes the virtual environment from Git

## How to run
1. Install Python 3.
2. Open a terminal in this folder.
3. Create a virtual environment: `python -m venv venv`
4. Activate it on Windows: `venv\\Scripts\\activate`
5. Install packages: `pip install -r requirements.txt`
6. Run: `python main.py`

## How it works
Requests downloads the webpage. Beautiful Soup parses its HTML. The program then locates paragraphs, the infobox, headings and article links, and prints the extracted information.

## Data source
https://en.wikipedia.org/wiki/Cape_Town

## Responsible scraping
This project is for educational purposes. Check a website's terms of use and robots.txt, respect rate limits, and avoid excessive requests. This program makes one page request per run.
