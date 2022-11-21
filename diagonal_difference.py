# import os

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d1 = 0
    d2 = 0
    for i in range(arr.__len__()):
        aux = arr[i]
        d1 += aux[i]
        d2 += aux[len(arr)-1-i]
    return abs(d1-d2)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()