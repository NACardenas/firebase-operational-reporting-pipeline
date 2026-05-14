from __future__ import annotations

import os
from datetime import datetime
from typing import Any
import logging

from dotenv import load_dotenv

from date_range import DateRange
from firebase_client import FirebaseClient
from sources import SOURCES

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def count_records(data: Any) -> int:
    if isinstance(data, dict):
        return len(data)

    if isinstance(data, list):
        return len(data)

    return 0


def main() -> None:
    report_type = os.getenv("REPORT_TYPE", "daily")

    logger.info("Starting firebase pipeline...")
    logger.info(f"Execute datetime: {datetime.now().isoformat(timespec='seconds')}")
    logger.info(f"Report type: {report_type}")

    period = DateRange.build(report_type=report_type)

    logger.info(f"Report period: {period.start_date} to {period.end_date}")

    for source in SOURCES:
        logger.info("-" * 50)
        logger.info(f"Source: {source.name}")
        logger.info(f"Date field: {source.date_field}")

        firebase = FirebaseClient.from_source(source)

        query = FirebaseClient.build_date_query(
            date_field=source.date_field,
            start_date=period.start_date,
            end_date=period.end_date
        )

        data = firebase.get_data(params=query)

        records_count = count_records(data)

        logger.info(f"Records count: {records_count}")


if __name__ == "__main__":
    main()