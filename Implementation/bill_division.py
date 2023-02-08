# https://www.hackerrank.com/challenges/bon-appetit
def bon_appetit(bill_array, item_not_consumed, anna_payout):
    """
    Calculates Anna's contribution for the dinner bill at a restaurant and checks if she paid the correct amount.

    :param bill_array: List with the value of each item on the bill.
    :param item_not_consumed: Index of the item on the bill that was not consumed.
    :param anna_payout: Amount paid by Anna.

    :return:
    str: "Bon Appetit" if Anna paid the correct amount.
    int: The difference between the correct amount and the amount paid by Anna, otherwise.
    """
    total_bill = sum(bill_array)
    anna_contribution = int((total_bill - bill_array[item_not_consumed]) / 2)

    if anna_contribution == anna_payout:
        return "Bon Appetit"
    else:
        return anna_payout - anna_contribution


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    num_array = int(first_multiple_input[0])

    anna = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    contributed = int(input().strip())

    print(bon_appetit(bill, anna, contributed))
