def minimal_operations(lista):
    count = []
    for word in lista:
        word = list(word)
        i = 0
        count_letter = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                count_letter = 1
            i += 1
        count.append(count_letter)
    return count


if __name__ == '__main__':
    n = int(input())
    lista = []
    for _ in range(n):
        lista.append(input(""))
    result = minimal_operations(lista)
    print(result)
