# https://www.hackerrank.com/challenges/staircase/problem
# Create staircase with number
def staircase(number):
    # range precisa começar em 1
    for i in range(1, number + 1):
        print(' ' * (number - i) + '#' * i)


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
