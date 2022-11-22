# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
# Print the decimal value of each fraction on a new line with  places after the decimal.
# n = 5 / a/y / b/y / c/y
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

    ar = list(map(int, input().rstrip().split()))

    plusMinus(ar)
