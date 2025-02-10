
# Web Scraping Project

This repository contains web scraping scripts for various e-commerce and product comparison websites.

## Projects

### 1. Smartprix Mobile Phones Scraper
A Python script that scrapes mobile phone data from Smartprix.com. The script uses Selenium WebDriver to handle dynamic content loading and infinite scrolling.

#### Features:
- Automated scrolling and content loading
- Handles dynamic "Load More" button clicks
- Extracts phone names and prices
- Saves data in both HTML and CSV formats
- Built-in retry mechanism for robust scraping
- Error handling for network issues

#### Requirements:
- Python 3.x
- Selenium WebDriver
- Chrome WebDriver
- BeautifulSoup4

#### Installation:
```bash
pip install selenium beautifulsoup4
```

You'll also need to download ChromeDriver that matches your Chrome browser version from: https://sites.google.com/chromium.org/driver/
