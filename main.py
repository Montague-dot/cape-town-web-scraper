"""
Cape Town Local Information Web Scraper
---------------------------------------
A beginner-friendly example of web scraping with Requests and Beautiful Soup.

The script retrieves the Cape Town Wikipedia page and extracts:
- introductory paragraphs
- selected facts from the infobox (when available)
- section headings
- links to related Wikipedia articles

Use this as a learning example. Check a website's terms and robots.txt before
scraping it, keep requests modest, and do not use scraped content commercially
without checking its licensing.
"""

import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Cape_Town"
HEADERS = {
    "User-Agent": "CapeTownStudentWebScraper/1.0 (educational project)"
}


def get_page(url):
    """Download a webpage and return its HTML."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Could not retrieve the webpage: {error}")
        return None


def extract_introduction(soup, limit=3):
    """Collect the first few meaningful paragraphs from the article."""
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []

    paragraphs = []
    for paragraph in content.find_all("p", recursive=False):
        text = paragraph.get_text(" ", strip=True)
        if text:
            paragraphs.append(text)
        if len(paragraphs) >= limit:
            break
    return paragraphs


def extract_infobox(soup):
    """Collect label/value pairs from the article infobox, if present."""
    infobox = soup.select_one("table.infobox")
    if infobox is None:
        return {}

    facts = {}
    for row in infobox.select("tr"):
        heading = row.find("th")
        value = row.find("td")
        if heading and value:
            label = heading.get_text(" ", strip=True)
            detail = value.get_text(" ", strip=True)
            if label and detail:
                facts[label] = detail
    return facts


def extract_headings(soup):
    """Return article section headings."""
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []

    headings = []
    for heading in content.select("h2"):
        title = heading.get_text(" ", strip=True)
        title = title.replace("[edit]", "").strip()
        if title:
            headings.append(title)
    return headings


def extract_related_links(soup, limit=10):
    """Return a small selection of links to related Wikipedia articles."""
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []

    links = []
    seen_urls = set()

    for anchor in content.select("a[href^='/wiki/']"):
        title = anchor.get_text(" ", strip=True)
        href = anchor.get("href", "")

        # Skip empty links and links to files or special Wikipedia pages.
        if not title or ":" in href:
            continue

        full_url = urljoin(URL, href)
        if full_url not in seen_urls:
            seen_urls.add(full_url)
            links.append((title, full_url))

        if len(links) >= limit:
            break

    return links


def display_results(soup):
    """Print the extracted local information in a readable format."""
    print("\n" + "=" * 65)
    print("CAPE TOWN: LOCAL INFORMATION WEB SCRAPER")
    print("=" * 65)

    print("\n1. INTRODUCTION")
    introduction = extract_introduction(soup)
    if introduction:
        for number, paragraph in enumerate(introduction, start=1):
            print(f"\n{number}. {paragraph}")
    else:
        print("No introductory paragraphs were found.")

    print("\n\n2. QUICK FACTS")
    facts = extract_infobox(soup)
    if facts:
        for label, detail in list(facts.items())[:10]:
            print(f"- {label}: {detail}")
    else:
        print("No infobox facts were found on the page.")

    print("\n\n3. ARTICLE SECTIONS")
    headings = extract_headings(soup)
    if headings:
        for heading in headings:
            print(f"- {heading}")
    else:
        print("No section headings were found.")

    print("\n\n4. RELATED INFORMATION")
    links = extract_related_links(soup)
    if links:
        for title, link in links:
            print(f"- {title}: {link}")
    else:
        print("No related links were found.")

    print("\n" + "=" * 65)
    print("Source:", URL)
    print("Scraping completed.")
    print("=" * 65)


def main():
    html = get_page(URL)
    if html is None:
        sys.exit(1)

    soup = BeautifulSoup(html, "html.parser")
    display_results(soup)


if __name__ == "__main__":
    main()
