#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimalOperations' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY words as parameter.
#

def minimalOperations(words):
    counter = []
    for word in words:
        list_word = list(word)
        count = 0
        # j = 0
        len_word = len(word) - 1
        for j in range(len_word):
            if list_word[j] == list_word[j + 1]:
                count += 1
                j += 1
        counter.append(count)
    return counter


if __name__ == '__main__':
    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = minimalOperations(words)
    print(result)
