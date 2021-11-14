nums = int(input())

for i in range(nums):

  n=int(input())

  costs = list(map(int, input().split(" ")))

  res=0

  costs=sorted(costs)

  while n>3:

    op1 = costs[0] + 2*costs[1] + costs[n-1]

    op2 = 2*costs[0] + costs[n-2] + costs[n-1]

    res += min(op1, op2)

    n -= 2

  if n==3:

    res+=sum(costs[0:3])

  elif n==2:

    res+=costs[1]

  else:

    res+=costs[0]

  print(res)

"""
3
4
300 400 600 700
2
1321 2450
3
500 123 873
"""
