def compareTriplets(a, b):
    cont_a = 0
    cont_b = 0
    for j in range(3):
        if a[j] > b[j]:
            cont_a += 1
        elif a[j] < b[j]:
            cont_b += 1
    array = [cont_a, cont_b]
    return array


if __name__ == '__main__':
    a = []
    b = []
    for i in range(3):
        respost = int(input("Digita o a"))
        a.append(respost)

    for i in range(3):
        respost = int(input("b"))
        b.append(respost)

    result = compareTriplets(a, b)
    print(result)