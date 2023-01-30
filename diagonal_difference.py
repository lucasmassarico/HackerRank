# https://www.hackerrank.com/challenges/diagonal-difference
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
def diagonal_difference(arr):
    d1 = 0
    d2 = 0
    for i in range(arr.__len__()):
        aux = arr[i]
        d1 += aux[i]
        d2 += aux[len(arr)-1-i]
    return abs(d1-d2)


if __name__ == '__main__':
    n = int(input().strip())
    ar = []
    for _ in range(n):
        ar.append(list(map(int, input().rstrip().split())))
    result = diagonal_difference(ar)
    print(result)
