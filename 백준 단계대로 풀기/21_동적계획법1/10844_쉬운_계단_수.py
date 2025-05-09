dp = [[0] * 10 for _ in range(100)]
dp[0][0] = 0
for i in range(1, 10):
    dp[0][i] = 1
n = int(input())

for i in range(1, 100):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
print(sum(dp[n - 1]) % 1000000000)
