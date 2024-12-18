def knapsack_1(N,W,items): # Bài D
    dp=[[0] * (W+1) for _ in range(N+1)]
    w = [item[0] for item in items]
    v = [item[1] for item in items]
    for i in range(1,N+1):
        for j in range(1,W+1):
            if j >= w[i-1]:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[N][W]
  
N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]  
print(knapsack_1(N, W, items))
