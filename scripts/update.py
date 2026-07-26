import json
from datetime import datetime

import requests
from bs4 import BeautifulSoup

URL = "https://www.fbil.org.in/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/137 Safari/537.36"
    )
}


def parse_reference_table(soup):
    """
    Parses the first Reference Rate table.
    """

    rates = {}

    tables = soup.find_all("table")

    for table in tables:

        rows = table.find_all("tr")

        for row in rows:

            cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]

            if len(cols) < 4:
                continue

            pair = cols[2]
            rate = cols[3]

            if "USD" in pair:
                rates["USD"] = float(rate)

            elif "EUR" in pair:
                rates["EUR"] = float(rate)

            elif "GBP" in pair:
                rates["GBP"] = float(rate)

            elif "JPY" in pair:
                rates["JPY100"] = float(rate)

            elif "AED" in pair:
                rates["AED"] = float(rate)

            elif "IDR" in pair:
                rates["IDR10000"] = float(rate)

    return rates


def main():

    print("Downloading FBIL page...")

    r = requests.get(URL, headers=HEADERS, timeout=60)

    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    rates = parse_reference_table(soup)

    if not rates:
        raise Exception("No exchange rates found.")

    output = {
        "source": "FBIL",
        "generatedAt": datetime.utcnow().isoformat() + "Z",
        "rates": rates
    }

    with open("data/latest.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
