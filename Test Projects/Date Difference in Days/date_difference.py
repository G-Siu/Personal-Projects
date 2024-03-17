from datetime import datetime


def days_between_dates(date1, date2):
    # Convert both dates to datetime objects
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference in days as a timedelta object
    diff = date2 - date1

    # Return the number of days in the difference
    return diff.days


first_date = "2021-01-01"
second_date = "2021-03-15"

print(days_between_dates(first_date, second_date))
