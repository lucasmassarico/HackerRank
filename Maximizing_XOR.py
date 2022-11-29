#
# Given two integers, l and r, find the maximal value of a xor b , written a ^(XOR) b,
# where  and  satisfy the following condition:
# 11 ^ 11 = 0
# 11 ^ 12 = 7 // Max Value
# 12 ^ 12 = 0

def maximizingXor(l, r):
    xor = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            aux = i ^ j
            if aux > xor:
                xor = aux
    return xor


if __name__ == '__main__':
    l = int(input())
    r = int(input().strip())
    result = maximizingXor(l, r)
    print(result)