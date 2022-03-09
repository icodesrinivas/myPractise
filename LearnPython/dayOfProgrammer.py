def dayOfProgrammer(year):
    # Julian calendar
    if year == 1918:
        no_of_days = 231
    else:
        no_of_days = 244

    if (year < 1917 and year % 4 == 0) or (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        remaining_days = "{:02d}".format(256 - no_of_days)
        return f'{remaining_days}.09.{year}'
    else:
        remaining_days = "{:02d}".format(256 - (no_of_days - 1))
        return f'{remaining_days}.09.{year}'
