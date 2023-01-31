# https://www.hackerrank.com/challenges/mini-max-sum
# Given array, find the min and max values that can be calculated by summing exactly four of the five integers
def mini_max_sum(arr):
    aux = sum(arr)
    print(aux - max(arr), aux - min(arr))


if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))

    mini_max_sum(ar)
