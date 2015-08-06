"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

def day_of_week(y, m, d):
    # Zeller's congruence
    # DAY_OF_WEEK = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if m == 1 or m == 2:
        m += 12
        y -= 1
    h = (y + y//4 - y//100 + y//400 + (13*m+8)//5 + d) % 7
    return h

def is_leap_year(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            return False
        return True
    return False

DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def main():
    cnt = 0
    for y in range(1901, 2001):
        for m in range(1,13):
            if day_of_week(y,m,1) == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
