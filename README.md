# RBI Exchange Rate API

A free, lightweight REST API that provides the latest RBI/FBIL Reference Exchange Rates in JSON format.

The project automatically fetches the official FBIL reference exchange rates (used by the Reserve Bank of India) every business day and publishes them through GitHub Pages.

This API is designed for:

- Microsoft Excel / Power Query
- Power BI
- Python
- Java
- JavaScript
- Mobile Apps
- Automation projects

## Features

- ✅ Official FBIL/RBI Reference Rates
- ✅ Daily automatic updates via GitHub Actions
- ✅ JSON API
- ✅ No server required
- ✅ Free forever
- ✅ Historical data support (planned)
- ✅ Easy integration with Excel

## Supported Currencies

- USD / INR
- EUR / INR
- GBP / INR
- JPY / INR
- AED / INR (planned)
- IDR / INR (planned)

## Example Response

```json
{
  "date": "2026-07-26",
  "time": "13:00:00",
  "source": "FBIL",
  "rates": {
    "USD": 96.5425,
    "EUR": 111.3248,
    "GBP": 128.6724,
    "JPY100": 59.1800
  }
}
```

## API Endpoint

```
https://<username>.github.io/rbi-exchange-rate-api/data/latest.json
```

## Data Source

The exchange rates are sourced from **Financial Benchmarks India Pvt. Ltd. (FBIL)**, which has been responsible for computing and publishing the official USD/INR and other reference exchange rates used by the Reserve Bank of India since July 10, 2018. :contentReference[oaicite:0]{index=0}

## Tech Stack

- Python
- GitHub Actions
- GitHub Pages
- JSON
- Excel Power Query
