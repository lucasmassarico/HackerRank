# https://www.hackerrank.com/challenges/lonely-integer
# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonely_integer(array):
    result = 0
    for element in array:
        if array.count(element) <= 1:
            result = element
    return result


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    print(lonely_integer(a))
