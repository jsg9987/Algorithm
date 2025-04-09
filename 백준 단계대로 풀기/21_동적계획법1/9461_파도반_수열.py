dp = [0 for _ in range(100+1)]
dp[1], dp[2], dp[3] = 1,1,1
T = int(input())
for i in range(T):
    n = int(input())
    for j in range(4,n+1):
        dp[j] = dp[j-2] + dp[j-3] # or dp[j] = dp[i-1] + dp[i-5]
    print(dp[n])