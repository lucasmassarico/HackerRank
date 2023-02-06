# https://www.hackerrank.com/challenges/migratory-birds
import collections


def migratory_birds(birds):
    count = collections.Counter(birds)
    max_count = max(count.values())
    for bird in sorted(count.keys()):
        if count[bird] == max_count:
            return bird


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print(migratory_birds(arr))
