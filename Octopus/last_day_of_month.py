import calendar
import datetime


def is_last_day_of_month(date: datetime.date) -> bool:
    """
    Check if a given date is the last day of the month.

    Args:
        date (datetime.date): The date to check.

    Returns:
        bool: True if the date is the last day of the month, False otherwise.
    """
    year = date.year
    month = date.month
    return date.day == calendar.monthrange(year, month)[1]


def main():
    today = datetime.date.today()
    return is_last_day_of_month(today)


if __name__ == "__main__":
    main()
