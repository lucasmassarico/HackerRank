# https://www.hackerrank.com/challenges/counting-valleys/
def counting_valleys(amount_steps, path_walked):
    count = 0
    valleys = 0
    for step in path_walked:
        if step == 'D':
            count -= 1
        else:
            count += 1

        if count == 0 and step == 'U':
            valleys += 1

    return valleys


if __name__ == '__main__':
    steps = int(input().strip())
    path = input()

    print(counting_valleys(steps, path))
