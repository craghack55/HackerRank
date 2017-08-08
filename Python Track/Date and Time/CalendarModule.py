from datetime import date
import calendar

m, d, y = map(int, raw_input().split())
myDate = date(y, m, d)

calendar.day_name[myDate.weekday()].upper()
