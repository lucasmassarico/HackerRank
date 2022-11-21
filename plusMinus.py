#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    cont_plus = 0
    cont_nega = 0
    cont_zero = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            cont_plus += 1
        elif arr[i] < 0:
            cont_nega += 1
        else:
            cont_zero += 1
    print(round(cont_plus / len(arr), 6))
    print(round(cont_nega / len(arr), 6))
    print(round(cont_zero / len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
