# Cape Town Local Information Web Scraper

## Project overview

This is a beginner-friendly Python web-scraping project. It uses **Requests** to retrieve the Cape Town Wikipedia webpage and **Beautiful Soup** to parse its HTML and extract useful information.

The program extracts:
1. Introductory paragraphs about Cape Town.
2. Quick facts from the article's information box, when available.
3. Section headings from the article.
4. A selection of links to related articles.

## Technologies used

- Python 3
- Requests
- Beautiful Soup 4
- HTML

## Project files

```text
cape_town_web_scraper/
├── main.py
├── requirements.txt
└── README.md
```

## How to run the project

### 1. Install Python

Install Python 3 if it is not already installed. During installation on Windows, select **Add Python to PATH**.

### 2. Download or clone the repository

If you have cloned the GitHub repository, open a terminal in the project folder.

### 3. Create a virtual environment (recommended)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install the required libraries

```bash
pip install -r requirements.txt
```

### 5. Run the scraper

```bash
python main.py
```

The extracted information will be displayed in the terminal.

## How the program works

1. The `requests` library sends an HTTP request to the webpage.
2. The webpage's HTML is returned to the program.
3. `BeautifulSoup(html, "html.parser")` parses the HTML so that elements can be searched.
4. CSS selectors and HTML tags are used to locate paragraphs, tables, headings and links.
5. The extracted information is printed in a readable format.

## Main functions

| Function | Purpose |
|---|---|
| `get_page()` | Downloads the webpage and handles request errors. |
| `extract_introduction()` | Extracts the first three meaningful paragraphs. |
| `extract_infobox()` | Extracts facts from the article's information box. |
| `extract_headings()` | Collects the article's section headings. |
| `extract_related_links()` | Collects links to related Wikipedia articles. |
| `display_results()` | Displays all extracted information. |
| `main()` | Runs the complete scraping process. |

## Data source

The project uses the Wikipedia article:

https://en.wikipedia.org/wiki/Cape_Town

The page structure may change over time, so some extracted sections may occasionally be empty. The scraper includes basic checks for missing page elements and request errors.

## Responsible scraping

This project is for educational purposes. Before scraping a website, review its terms of use and `robots.txt`, identify any rate limits, and avoid sending excessive requests. This program makes one page request per run.
