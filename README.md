# Firebase Operational Reporting Pipeline

![CI](https://github.com/ohyegimica/pipeline-ptoi/actions/workflows/daily_report.yml/badge.svg)

Automated cloud reporting pipeline built with Python and GitHub Actions to retrieve operational data from multiple Firebase Realtime Database sources using optimized date-based queries.

---

## Overview

This project connects to one or more Firebase Realtime Database nodes, retrieves records for a selected reporting period, and prepares the foundation for automated operational reporting pipelines.

The project was designed as a modular and reusable architecture focused on:

- automated cloud execution
- operational reporting
- scalable data source configuration
- reusable Firebase querying logic
- date-based filtering
- environment-based configuration

---

## Why this project

This repository demonstrates a lightweight ETL reporting pipeline for BI and operational analytics teams using Firebase Realtime Database and GitHub Actions automation.

The project can be used to:

- automate operational data extraction
- validate date-range reporting queries
- demonstrate environment variable and secret integration
- prepare cloud-based operational reporting workflows

---

## Current Features

- Multiple Firebase source support
- Date-based Firebase REST queries
- Daily, weekly and monthly reporting periods
- Modular architecture
- GitHub Actions scheduled execution
- Environment variable / GitHub Secrets configuration
- Optional Firebase authentication token
- Reusable Firebase client
- Dynamic source configuration

---

## Supported Report Periods

| Report Type | Description |
|---|---|
| Daily | Previous day |
| Weekly | Previous complete week |
| Monthly | Previous complete month |

---

## Tech Stack

- Python 3.11
- Firebase Realtime Database
- GitHub Actions
- REST API
- Environment Variables
- GitHub Secrets

---

## Project Structure

```text
pipeline-ptoi/
├── src/
│   ├── main.py
│   ├── date_range.py
│   ├── firebase_client.py
│   └── sources.py
├── .github/
│   └── workflows/
│       └── daily_report.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Architecture Overview

```text
GitHub Actions
        ↓
main.py
        ↓
DateRange.build()
        ↓
SOURCES configuration
        ↓
FirebaseClient
        ↓
Firebase REST API
        ↓
JSON operational data
```

---

## Data Sources

Firebase sources are configured in:

```text
src/sources.py
```

Each source defines:

- source name
- Firebase environment variable
- date field used for filtering

Example:

```python
FirebaseSource(
    name="production",
    url_env="FIREBASE_URL_PRODUCTION",
    date_field="fecharaw",
)
```

---

## Environment Variables

Create a local `.env` file or configure GitHub Secrets.

Example:

```env
FIREBASE_URL_PRODUCTION=https://your-project-default-rtdb.firebaseio.com/production.json
FIREBASE_URL_INPUTS=https://your-project-default-rtdb.firebaseio.com/inputs.json
FIREBASE_AUTH_TOKEN=your_firebase_auth_token
REPORT_TYPE=daily
```

Notes:
- Each Firebase URL should point to a Realtime Database node and usually end in `.json`.
- `FIREBASE_AUTH_TOKEN` is optional but recommended for authenticated databases.
- `REPORT_TYPE` can be `daily`, `weekly`, or `monthly`.

---

## Local Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
python src/main.py
```

---

## GitHub Actions

The pipeline runs automatically every day at:

```text
08:00 AM Peru Time
```

using GitHub Actions scheduled workflows.

It can also be executed manually using:

```text
workflow_dispatch
```

Secrets expected by GitHub Actions:
- `FIREBASE_URL_PRODUCTION`
- `FIREBASE_URL_INPUTS`
- `FIREBASE_AUTH_TOKEN` (optional)

---

## Current Output

The current version prints:

- execution datetime
- report type
- report period
- source name
- date field
- records count

Example:

```text
Starting firebase pipeline...
Execute datetime: 2026-05-14T16:33:26
Report type: daily
Report period: 2026-05-13 to 2026-05-13

--------------------------------------------------
Source: production
Date field: fecharaw
Records count: 10263

--------------------------------------------------
Source: inputs
Date field: fecharaw
Records count: 2860
```

---

## Future Improvements

Planned improvements include:

- pandas transformation layer
- CSV export
- PostgreSQL / Supabase integration
- automated email reporting
- logging system
- retry handling
- Docker support
- unit testing
- data quality validation
- AI-generated operational summaries

---

## Security Notes

Sensitive configuration values are handled through:

- local `.env` files
- GitHub Secrets

The `.env` file is excluded from version control through `.gitignore`.

---

## License

This project is intended for learning, portfolio, and operational reporting automation purposes.