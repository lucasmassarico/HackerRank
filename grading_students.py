#!/bin/python3

import math
import os
import random
import re
import sys

#
#
#
# Complete the 'gradingStudents' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    result = []
    for grade in grades:
        aux = 5-(grade % 5)
        if aux < 3:
            if grade+aux < 40:
                result.append(grade)
            else:
                grade += aux
                result.append(grade)
        else:
            result.append(grade)
    return result


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)