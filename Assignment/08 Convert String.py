for k in range(0, int(input())):
    X = list((input()))
    Y = list((input()))

    count = 0

    for i in range(0, len(Y)):
        for j in range(0, len(X)):
            print(X,Y)
            if Y[i].upper() == X[j].upper():
                del X[j]
                count += 1
                break

    if count == len(Y):
        print("YES")
    else:
        print("NO")





"""
2
daBcd
ABC
rACCEd
ACED
"""
# YES
# NO
