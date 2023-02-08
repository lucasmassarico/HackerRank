# https://www.hackerrank.com/challenges/sock-merchant
import collections


def sock_merchant(num, socks):
    """
    Given an integer 'num' and a list of integers 'socks', counts the number of matching sock pairs in the list.

    :param num: The number of socks in the list.
    :param socks: The list of integers, where each integer represents the color of a sock.

    :return:
    int: The number of matching sock pairs in the list.

    """
    count_sock_pile = 0
    socks = collections.Counter(socks)
    for sock in socks:
        count_sock_pile += socks[sock] // 2
    return count_sock_pile


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))

    print(sock_merchant(n, ar))
