# 5/2 23:48 ~
T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if li[i] > li[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{tc} {max(dp)}")