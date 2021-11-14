for j in range(int(input())):
    N, K = list(map(int, input().split(" ")))
    S = str(input())
    output = ""

    dictx = {}

    for each in S:
        if each not in dictx.keys():
            dictx[each] = K

        if dictx[each] > 0:
            output += each
            dictx[each] -= 1

    print(output)




"""
2
8 2
ababbca
10 3
abcaacbccb
"""
#ababc
#abcaacbcb
