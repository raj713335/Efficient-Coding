def maxProb(index, pts):

   if(pts > w):

       pts = w

   if(visited[index][pts] == 1):

       return dp[index][pts]

   visited[index][pts] = 1

   if(index == n):

       if(pts == w):

           dp[index][pts] = 1.0

       else:

           dp[index][pts] = 0.0

       return dp[index][pts]

   ans1 = p1*maxProb(index+1, pts+x) + (1-p1)*maxProb(index+1, pts)

   ans2 = p2*maxProb(index+1, pts+y) + (1-p2)*maxProb(index+1, pts)

   dp[index][pts] = max(ans1,ans2)

   return dp[index][pts]



for _ in range(int(input())):

   x,y,n,w,p1,p2 = [int(x) for x in input().split()]

   p1 = float(p1/100)

   p2 = float(p2/100)

   visited = [[0 for i in range(w+1)] for j in range(n+1)]

   dp = [[0 for i in range(w+1)] for j in range(n+1)]

   print("{:.6f}".format(maxProb(0,0)*100))
