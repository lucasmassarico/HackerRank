# https://www.hackerrank.com/challenges/day-of-the-programmer
def day_of_programmer(year):
    """
    Calcula e retorna a data da comemoração do Dia do Programador.

    :param year: Ano que precisa ser calculado a data.
    :return: Uma string no formato dd.mm.yyyy representando a data.
    """
    if year == 1918:
        return '26.09.1918'

    leap = False
    if year < 1918:
        leap = year % 4 == 0
    elif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        leap = True

    return f'12.09.{year}' if leap else f'13.09.{year}'


if __name__ == '__main__':
    year_travel = int(input().strip())

    print(day_of_programmer(year_travel))
