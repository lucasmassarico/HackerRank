#
# The problem is related to counting the number of apples and oranges that fall within a range of a house
def count_apples_and_oranges(start_house, end_house, tree_apple, tree_orange, apples_pos, oranges_pos):
    count_apples = 0
    count_oranges = 0
    for apple in apples_pos:
        if start_house <= tree_apple + apple <= end_house:
            count_apples += 1
    for orange in oranges_pos:
        if start_house <= tree_orange + orange <= end_house:
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
