import calendar
import datetime


def last_day_of_month():
    year = datetime.date.today().year
    month = datetime.date.today().month
    if datetime.date.today().day == calendar.monthrange(year, month)[1]:
        return True
