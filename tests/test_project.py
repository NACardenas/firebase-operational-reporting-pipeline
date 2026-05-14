import sys
from datetime import date
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from date_range import DateRange
from firebase_client import FirebaseClient


def test_date_range_daily():
    today = date(2024, 1, 10)
    period = DateRange.build("daily", today=today)
    assert period.start_date == "2024-01-09"
    assert period.end_date == "2024-01-09"


def test_build_date_query_equal():
    query = FirebaseClient.build_date_query("fecharaw", "2024-01-10", "2024-01-10")
    assert query == {
        "orderBy": '"fecharaw"',
        "equalTo": '"2024-01-10"'
    }
