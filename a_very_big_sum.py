# It must return the sum of all array elements.
def aVeryBigSum(arr):
    return sum(arr)


if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)
