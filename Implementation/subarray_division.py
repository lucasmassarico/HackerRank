# https://www.hackerrank.com/challenges/the-birthday-bar
def birthday(chocolate_bar, day, mounth):
    count = 0
    for square in range(len(chocolate_bar) - mounth + 1):
        if sum(chocolate_bar[square:square + mounth]) == day:
            count += 1
    return count


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)
