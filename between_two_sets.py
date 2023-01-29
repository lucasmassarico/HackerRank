import math


# https://www.hackerrank.com/challenges/between-two-sets/problem
def get_total_x(a, b):
    lcm_a = a[0]
    for i in range(1, len(a)):
        lcm_a = math.lcm(lcm_a, a[i])
    gcd_b = b[0]
    for i in range(1, len(b)):
        gcd_b = math.gcd(gcd_b, b[i])
    count = 0
    for i in range(lcm_a, gcd_b+1, lcm_a):
        if gcd_b % i == 0:
            count += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    print(get_total_x(arr, brr))
