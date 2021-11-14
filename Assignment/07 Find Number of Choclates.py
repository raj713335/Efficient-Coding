
listx = [0 for i in range(0, 10**5)]

for K in range(0, int(input())):
    X, Y = list(map(int, input().split(" ")))
    listx[X- 1] += 1

    listx[Y] -= 1

max = sum = 0
indi= 0
for i in range(0, len(listx)):
    sum += listx[i]
    if sum > max:
        max = sum
        indi = i

print(indi+1, max)

#     X, Y = list(map(int, input().split(" ")))
#
#     for j in range(X, Y+1):
#         listx[j] += 1
#
# maxi = max(listx)
# indi = listx.index(maxi)
#
# print(indi, maxi)






"""
6
3 6
1 6
7 11
2 15
5 8
1 2
"""
#5 4
