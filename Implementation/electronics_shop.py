# https://www.hackerrank.com/challenges/electronics-shop
def get_money_spent(keyboards_prices, drives_prices, money):
    keyboards_prices.sort()
    drives_prices.sort()
    max_spending = -1
    i = 0
    j = len(drives_prices) - 1
    while i < len(keyboards_prices) and j >= 0:
        total_price = keyboards_prices[i] + drives_prices[j]
        if total_price <= money:
            max_spending = max(max_spending, total_price)
            i += 1
        else:
            j -= 1
    return max_spending


if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    print(get_money_spent(keyboards, drives, b))
