def frog_A(N,heights): # Bài A
    dp = [0] * N
    dp[0] = 0 # tại hòn đá đầu tiên thì sẽ không tốn chi phí
    if N > 1 :
        dp[1] = abs(heights[1] - heights[0])
    for i in range(2,N):
        dp[i]=min(dp[i-2]+abs(heights[i-2]-heights[i]),dp[i-1]+abs(heights[i-1]-heights[i]))

    return dp[N-1]

    
    


