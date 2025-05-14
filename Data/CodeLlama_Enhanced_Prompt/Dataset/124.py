def valid_date(date):
    """
    Returns True if the date is valid, False otherwise.
    The date is valid if it is in the form of mm-dd-yyyy and the month, day, and year are valid.
    """
    import re

    # Using regex to check if the date is in the correct format
    if not re.match(r'^\d{2}-\d{2}-\d{4}$', date):
        return False

    month, day, year = map(int, date.split('-'))

    # Checking the validity of the month
    if month < 1 or month > 12:
        return False

    # Checking the validity of the day
    if day < 1 or day > 31:
        return False

    # Checking the validity of leap years
    if month == 2 and day > 28:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False

    # Checking the validity of other months
    if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False

    return True
