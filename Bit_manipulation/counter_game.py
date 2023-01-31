import math


# https://www.hackerrank.com/challenges/three-month-preparation-kit-counter-game/
# Louise and Richard have developed a numbers game. They pick a number and check to see if it is a power of 2.
# If it is, they divide it by 2. If not, they reduce it by the next lower number which is a power of 2.
# Whoever reduces the number to 1 wins the game. Louise always starts.
#
# Given an initial value, determine who wins the game.
# Example: Input: 1 /n 132. Output: Louise

def log2(number):
    return math.log10(number) / math.log10(2)


def is_power_of_two(number):
    return math.ceil(log2(number)) == math.floor(log2(number))


def define_2pow(number, count):
    aux_pow = 0
    while not is_power_of_two(number):
        aux_pow += 1
        if number - int(math.pow(2, aux_pow)) < 0:
            number = number - math.pow(2, aux_pow - 1)
            count += 1
            aux_pow = 0
    return number, count


def counter_game(number):
    count = 0
    number, count = define_2pow(number, count)

    while number != 1:
        number = int(number/2)
        count += 1

    if count % 2 == 0:
        return "Richard"
    else:
        return "Louise"


if __name__ == '__main__':
    attempts = int(input().strip())

    for attempts_itr in range(attempts):
        numbers = int(input().strip())
        print(counter_game(numbers))
