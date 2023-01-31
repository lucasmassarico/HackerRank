# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breaking_records(scores):
    min_score = scores[0]
    max_score = scores[0]
    min_breaks = 0
    max_breaks = 0
    for score in scores:
        if score > max_score:
            max_score = score
            max_breaks += 1
        elif score < min_score:
            min_score = score
            min_breaks += 1
    return max_breaks, min_breaks


if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    print(breaking_records(scores))
