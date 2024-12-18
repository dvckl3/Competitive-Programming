def frog_B(N,K,heights): # Bài B
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(1,N):
         dp[i] = min(dp[j] + abs(heights[i] - heights[j]) for j in range(max(0, i-K), i))
    return dp[N-1]
