def is_leapyear(y: int) -> bool:
    """This is a function to determine if a year is a leapyear or not."""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# ----------------------------------------------------------

if __name__ == '__main__':

    year = int(input('Give a year: '))

    if is_leapyear(year):
        print('%d is a leap year' % year)
    else:
        print('%d is not a leap year' % year)
