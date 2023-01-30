# https://www.hackerrank.com/challenges/the-great-xor
def the_great_xor(xor):
    count = 0
    for interactions in range(xor):
        # Verificando se o resultado da operação XOR é maior que x
        if interactions ^ xor > xor:
            # Se sim, incrementando o contador
            count += 1
    return count


if __name__ == '__main__':
    rounds = int(input().strip())

    for rounds_itr in range(rounds):
        number = int(input().strip())
        print(the_great_xor(number))
