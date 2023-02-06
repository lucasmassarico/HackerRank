# https://www.hackerrank.com/challenges/day-of-the-programmer
def day_of_programmer(year):
    day = 00
    mounth = 00
    if year <= 1918:
        if year == 1918:
            return f'26.09.{year}'
        if year % 4 == 0:
            return f'12.09.{year}'
    elif year % 100 == 0:
        if year % 400 == 0:
            return f'12.09.{year}'
    elif year % 4 == 0:
        return f'12.09.{year}'
    return f'13.09.{year}'


if __name__ == '__main__':
    year_travel = int(input().strip())

    print(day_of_programmer(year_travel))
