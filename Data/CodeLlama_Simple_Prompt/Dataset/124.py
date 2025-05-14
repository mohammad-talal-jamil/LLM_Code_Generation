def valid_date(date_string):
    """
    Validates a date string in the format 'mm-dd-yyyy'
    """
    # split the date string into three parts: month, day, and year
    month, day, year = date_string.split('-')

    # convert the month, day, and year to integers
    month = int(month)
    day = int(day)
    year = int(year)

    # validate that the month is between 1 and 12
    if not 1 <= month <= 12:
        return False

    # validate that the day is between 1 and 31
    if not 1 <= day <= 31:
        return False

    # validate that the year is between 1 and 9999
    if not 1 <= year <= 9999:
        return False

    # validate that the day is correct for the month and year
    if month in [4, 6, 9, 11] and day == 31:
        return False
    elif month == 2 and (day > 28 or (day == 29 and not year % 4 == 0)):
        return False

    # if all checks pass, return True
    return True
