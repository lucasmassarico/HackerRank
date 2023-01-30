# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
def birthday_cake_candles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))

    print(birthday_cake_candles(candles))
