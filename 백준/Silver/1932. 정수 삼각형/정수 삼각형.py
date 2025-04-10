n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[0][i] = triangle[n - 1][i]

for i in range(1, n):
    for j in range(n - i):
        dp[i][j] = max(dp[i-1][j] + triangle[n - i - 1][j], dp[i-1][j + 1] + triangle[n - i - 1][j])

print(dp[n-1][0])