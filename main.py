#!/usr/bin/env python3
"""Scrape useful local information about Cape Town with Beautiful Soup."""

import sys
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Cape_Town"
HEADERS = {"User-Agent": "CapeTownStudentWebScraper/1.0 (educational project)"}


def get_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        return response.text
    except requests.RequestException as error:
        print(f"Could not retrieve webpage: {error}")
        return None


def extract_introduction(soup, limit=3):
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []
    paragraphs = []
    for paragraph in content.find_all("p", recursive=False):
        value = paragraph.get_text(" ", strip=True)
        if value:
            paragraphs.append(value)
        if len(paragraphs) >= limit:
            break
    return paragraphs


def extract_infobox(soup):
    table = soup.select_one("table.infobox")
    if table is None:
        return {}
    facts = {}
    for row in table.select("tr"):
        heading, value = row.find("th"), row.find("td")
        if heading and value:
            label = heading.get_text(" ", strip=True)
            detail = value.get_text(" ", strip=True)
            if label and detail:
                facts[label] = detail
    return facts


def extract_headings(soup):
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []
    return [
        heading.get_text(" ", strip=True).replace("[edit]", "").strip()
        for heading in content.select("h2")
        if heading.get_text(" ", strip=True)
    ]


def extract_related_links(soup, limit=10):
    content = soup.select_one("div.mw-parser-output")
    if content is None:
        return []
    links, seen = [], set()
    for anchor in content.select("a[href^='/wiki/']"):
        title, href = anchor.get_text(" ", strip=True), anchor.get("href", "")
        if not title or ":" in href:
            continue
        full_url = urljoin(URL, href)
        if full_url not in seen:
            seen.add(full_url)
            links.append((title, full_url))
        if len(links) >= limit:
            break
    return links


def main():
    html = get_page(URL)
    if html is None:
        sys.exit(1)
    soup = BeautifulSoup(html, "html.parser")

    print("\nCAPE TOWN: LOCAL INFORMATION WEB SCRAPER")
    print("=" * 55)

    print("\n1. INTRODUCTION")
    for number, paragraph in enumerate(extract_introduction(soup), 1):
        print(f"{number}. {paragraph}")

    print("\n2. QUICK FACTS")
    for label, detail in list(extract_infobox(soup).items())[:10]:
        print(f"- {label}: {detail}")

    print("\n3. ARTICLE SECTIONS")
    for heading in extract_headings(soup):
        print(f"- {heading}")

    print("\n4. RELATED INFORMATION")
    for title, link in extract_related_links(soup):
        print(f"- {title}: {link}")

    print("\nSource:", URL)
    print("Scraping completed.")


if __name__ == "__main__":
    main()
