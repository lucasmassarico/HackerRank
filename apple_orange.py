def count_apples_and_oranges(start_house, end_house, tree_apple, tree_orange, apples_pos, oranges_pos):
    count_apples = 0
    count_oranges = 0
    for interactions in apples_pos:
        result = tree_apple + interactions
        if result >= start_house:
            count_apples += 1
    for interactions in oranges_pos:
        result = tree_orange + interactions
        if result <= end_house:
            count_oranges += 1
    print(count_apples)
    print(count_oranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    count_apples_and_oranges(s, t, a, b, apples, oranges)
