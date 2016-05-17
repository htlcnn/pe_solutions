#!/usr/bin/env python3

from datetime import timedelta, date


# weekday() of first_monday is 0 -> sunday is 6th weekday
first_monday = date(1900, 1, 1).weekday()

sundays = 0
start = date(1901, 1, 1)
end = date(2000, 12, 31)
for i in range((end - start).days+1):
    day = start + timedelta(i)
    if day.weekday() == 6 and day.day == 1:
        sundays += 1
        
print(sundays)

# 171