def sum_xor(n):
    # count the number of 0 bits in the binary representation of n
    count = 0
    while n:
        if n % 2 == 0:
            count += 1
        n //= 2
    return 2 ** count


if __name__ == '__main__':
    n = int(input().strip())

    print(sum_xor(n))
