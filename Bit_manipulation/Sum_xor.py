# https://www.hackerrank.com/challenges/three-month-preparation-kit-sum-vs-xor
def sum_xor(num):
    # count the number of 0 bits in the binary representation of n
    count = 0
    while num:
        if num % 2 == 0:
            count += 1
        num //= 2
    return 2 ** count


if __name__ == '__main__':
    n = int(input().strip())

    print(sum_xor(n))
