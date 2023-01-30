# https://www.hackerrank.com/challenges/a-very-big-sum?isFullScreen=true
# It must return the sum of all array elements.
def very_big_sum(arr):
    return sum(arr)


if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = very_big_sum(ar)

    print(result)
