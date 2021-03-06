import math

# The year can be evenly divided by 4, is a leap year, unless:
    # The year can be evenly divided by 100, it is NOT a leap year, unless:
        # The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or year % 400 == 0:
        return True
    else:
        return False

# true
print(is_leap(1992))
print(is_leap(2020))
# true
print(is_leap(2000))
print(is_leap(2400))

# false
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2200))
print(is_leap(2300))
print(is_leap(2500))