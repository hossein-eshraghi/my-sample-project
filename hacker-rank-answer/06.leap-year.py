# An extra day is added to the calendar almost every four years as February 29,
# and the day is called a leap day.
# It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun.
# A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.

# This means that in the Gregorian calendar,
# the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap yearsv (False). Source

# Task
# Given a year, determine whether it is a leap year.
# If it is a leap year, return the Boolean True, otherwise return False.
# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function.
# It is only necessary to complete the is_leap function.

# Input Format
# Read , year the year to test.

# Constraints
# 1900 <= year < 10 ^ 5

# Output Format
# The function must return a Boolean value (True/False).
# Output is handled by the provided code stub.

def is_leap(year):
    # Write your logic here
    leap = False
    # not leap year >> FALSE
    x = (1800, 1900, 2100, 2200, 2300 , 2500)

    # leap year >> TRUE
    y = (2000, 2400)

    if 1900 <= year <= 10e5:
        if year in (x):
            return leap

        elif year in (y):
            return not leap

        elif year % 4 == 0:
            return not leap
            if year % 100 == 0:
                return not leap
            elif year % 400 == 0:
                return leap
            else:
                return not leap
        else:
            return leap

year = int(input())
print(is_leap(year))
