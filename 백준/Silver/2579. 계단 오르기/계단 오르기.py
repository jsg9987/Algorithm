import sys

inputF = sys.stdin.readline
n = int(inputF().rstrip())
li = []
for i in range(n):
    li.append(int(inputF().rstrip()))

dp = [0 for _ in range(n)]

if n >= 4:
    dp[0], dp[1], dp[2] = li[0], li[0] + li[1], max(li[0] + li[2], li[1] + li[2])
    for i in range(3, n):
        dp[i] = max(dp[i - 3] + li[i - 1] + li[i], dp[i-2] + li[i])
    print(dp[n - 1])
elif n == 1:
    print(li[0])
elif n == 2:
    print(li[0] + li[1])
elif n == 3:
    print(max(li[0] + li[2], li[1] + li[2]))
