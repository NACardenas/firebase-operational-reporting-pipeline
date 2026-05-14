from __future__ import annotations
import calendar
from dataclasses import dataclass
from datetime import date, timedelta,datetime

@dataclass(frozen=True)
class ReportPeriod:
    report_type: str
    start_date: str
    end_date: str

class DateRange: 
    DATE_FORMAT = "%Y-%m-%d"
    
    @classmethod
    def build(cls, report_type: str="daily",today:date | None = None) -> ReportPeriod:
        today = today or datetime.now().date()
        report_type=report_type.lower().strip()
        if report_type == "daily":
            target= today - timedelta(days=1)
            start,end = target,target
        elif report_type == "weekly":
            current_monday = today - timedelta(days=today.weekday())
            start=current_monday - timedelta(weeks=1)
            end=current_monday - timedelta(days=1)
        elif report_type == "monthly":
            year,month=today.year,today.month - 1
            if month == 0:
                year -= 1
                month = 12
            start=date(year,month,1)
            end=date(year,month,calendar.monthrange(year,month)[1])
        else:
            raise ValueError(f"Invalid report type: {report_type}")
        return ReportPeriod(
            report_type=report_type,
            start_date=start.strftime(cls.DATE_FORMAT),
            end_date=end.strftime(cls.DATE_FORMAT)
        )


