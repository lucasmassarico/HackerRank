# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
def divisible_sum_pairs(length_array, divisor, arr):
    count = 0
    remainder_count = [0] * divisor
    for num in arr:
        remainder = num % divisor
        count += remainder_count[(divisor - remainder) % divisor]
        remainder_count[remainder] += 1
    return count


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    print(divisible_sum_pairs(n, k, ar))
