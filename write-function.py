def is_leap(year):
    leap = False

    if year % 4:
        leap = False
    elif year % 100:
        leap = True
    elif year % 400:
        leap = False
    else:
        leap = True

    return leap


year = int(input())
print(is_leap(year))