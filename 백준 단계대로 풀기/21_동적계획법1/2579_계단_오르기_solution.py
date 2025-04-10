import sys

inputF = sys.stdin.readline
n = int(input())
s = [int(inputF().rstrip()) for _ in range(n)]
dp = [0] * n
if len(s) <= 2:
    print(sum(s))
else:
    dp[0], dp[1] = s[0], s[0] + s[1]
    for i in range(2,n):
