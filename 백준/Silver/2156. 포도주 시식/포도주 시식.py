import sys

inputF = sys.stdin.readline
n = int(input())
li = [int(inputF()) for _ in range(n)]
dp = [0] * 10001
dp[0], dp[1], = 0, li[0]
if n == 2:
    dp[2] = li[0] + li[1]
if n == 3:
    dp[3] = max(li[0] + li[1], li[0] + li[2], li[1] + li[2])
if n >= 4:
    dp[2], dp[3] = li[0] + li[1], max(li[0] + li[1], li[0] + li[2], li[1] + li[2])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + li[i - 2] + li[i - 1], dp[i - 2] + li[i - 1], dp[i-1])
print(max(dp))


