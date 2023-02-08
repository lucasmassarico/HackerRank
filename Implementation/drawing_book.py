# https://www.hackerrank.com/challenges/drawing-book


def page_count(pag_total_book, pag_to_see):
    """
    Given the total number of pages in a book and the page to see, returns the
    minimum number of pages that must be turned to reach the page to see.

    :param pag_total_book: Total number of pages in the book.
    :param pag_to_see: The page to be seen.
    :return:
    int: The minimum number of pages that must be turned.
    """

    front_turns = pag_to_see // 2
    back_turns = pag_total_book // 2 - front_turns

    return min(front_turns, back_turns)


if __name__ == '__main__':
    num = int(input().strip())
    pag = int(input().strip())

    print(page_count(num, pag))
