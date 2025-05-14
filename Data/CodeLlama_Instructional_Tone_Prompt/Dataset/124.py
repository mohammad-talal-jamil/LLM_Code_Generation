import re


def valid_date(date):
    """
    Validates a given date string and returns True if the date is valid, otherwise False.
    The date should be in the format: mm-dd-yyyy.
    """
    month, day, year = date.split('-')
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False
    if int(month) < 1 or int(month) > 12:
        return False
    if int(day) < 1 or int(day) > 31:
        return False
    if int(year) < 0 or len(str(year)) != 4:
        return False
    if int(month) in [4, 6, 9, 11] and int(day) == 31:
        return False
    if int(month) == 2 and int(day) > 28:
        return False
    return True
