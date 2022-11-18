# A atividade consiste em conferir se duas palavras são Anagramas, caso não forem, existe algumas possibilidades:
# 1) Se forem de tamanhos diferentes, retorna -1
# 2) Se tiverem letras diferentes, deve informar a quantidade de letras diferentes na palavra
# 3) Se forem iguais, retorna 0
# função recebe como parâmetro duas listas e deve retornar um array

def getMinimumDifference(a, b):
    count = []
    for word1, word2 in zip(a, b):
        word1 = list(word1)
        word2 = list(word2)
        if len(word1) != len(word2):
            count.append(-1)
        else:
            aux_word1 = 0
            aux_word2 = len(word2) - 1
            count_diff = 0
            while aux_word1 < len(word1):
                if word1[aux_word1] != word2[aux_word2]:
                    count_diff += 1
                aux_word1 += 1
                aux_word2 -= 1
            count.append(count_diff)
    return count


if __name__ == '__main__':
    a_count = int(input().strip())
    a = []

    for _ in range(a_count):
        a_item = input()
        a.append(a_item)
    b_count = int(input().strip())
    b = []

    for _ in range(b_count):
        b_item = input()
        b.append(b_item)

    result = getMinimumDifference(a, b)
    print(result)
