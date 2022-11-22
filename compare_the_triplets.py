# Compare the triplets(x > y) and return array is [x, y] with Alice's score first and Bob's second.
def compareTriplets(rate_alice, rate_bob):
    cont_a = 0
    cont_b = 0
    for j in range(3):
        if rate_alice[j] > rate_bob[j]:
            cont_a += 1
        elif rate_alice[j] < rate_bob[j]:
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