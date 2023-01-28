# https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(pos1, speed1, pos2, speed2):
    if speed1 <= speed2:
        return "NO"

    steps1 = (pos2 - pos1) / (speed1 - speed2)
    if steps1 < 0 or steps1 % 1 != 0:
        return "NO"

    return "YES"


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    # first kangaroo, pos1 and speed1
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])

    # second kangaroo, pos2 and speed2
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])

    print(kangaroo(x1, v1, x2, v2))
