import sys

inputF = sys.stdin.readline
n = int(input())
li = [0] * 10001
for i in range(n):
    li[i] = int(inputF())
dp = [0] * 10001
dp[0], dp[1], = 0, li[0]
dp[2] = li[0] + li[1]
dp[3] = max(li[0] + li[1], li[0] + li[2], li[1] + li[2])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 3] + li[i - 2] + li[i - 1], dp[i - 2] + li[i - 1], dp[i-1])
print(dp[n])


