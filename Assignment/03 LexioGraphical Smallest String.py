for k in range(int(input())):
  K, S = list(map(str, input().split(" ")))
  S2 = S+S
  res = S
  N = len(S)
  if K == "1":
    for i in range(N):
      res = min(res, S2[i:i + N])
    print(res)
  else:
    print("".join(sorted(S)))


"""
2
1 cba
2 abab
"""
