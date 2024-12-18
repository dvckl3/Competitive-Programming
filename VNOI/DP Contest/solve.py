def fibo_number(n): # Test 
    if n==1:
        return [1]
    f = [0] * n
    f[0] = 1
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f


def frog_A(N,heights): # Bài A
    dp = [0] * N
    dp[0] = 0 # tại hòn đá đầu tiên thì sẽ không tốn chi phí
    if N > 1 :
        dp[1] = abs(heights[1] - heights[0])
    for i in range(2,N):
        dp[i]=min(dp[i-2]+abs(heights[i-2]-heights[i]),dp[i-1]+abs(heights[i-1]-heights[i]))

    return dp[N-1]
def frog_B(N,K,heights): # Bài B
    dp = [float('inf')] * N
    dp[0] = 0
    for i in range(1,N):
         dp[i] = min(dp[j] + abs(heights[i] - heights[j]) for j in range(max(0, i-K), i))
    return dp[N-1]
      
def vacation(N,happy): # Bài C 
    
    


