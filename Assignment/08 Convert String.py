"""
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

def solve(X, Y):

  N, M = len(X), len(Y)

  DP = [[ None for _ in range(M+1)] for _ in range(N+1)]

   

  # Initialization

  for i in range(M+1):

    DP[0][i] = False

  DP[0][0] = True

  for i in range(1, N+1):

    if X[i-1].islower():

      DP[i][0] = DP[i-1][0]

    else:

      DP[i][0] = False

   

   

  for i in range(1, N+1):

    for j in range(1, M+1):

      if X[i-1].isupper() and X[i-1] == Y[j-1]:

        DP[i][j] = DP[i-1][j-1]

      elif X[i-1].isupper():

        DP[i][j] = False 

      elif X[i-1].islower() and ((X[i-1] == Y[j-1]) or (X[i-1].upper() == Y[j-1])):

        DP[i][j] = DP[i-1][j-1] | DP[i-1][j]

      elif X[i-1].islower():

        DP[i][j] = DP[i-1][j]

   

  return DP[N][M]

   

if __name__ == "__main__":

  Q = int(input())

  for _ in range(Q):

    X,Y = input(), input()

    if solve(X,Y):

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
