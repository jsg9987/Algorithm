# 4/23 16:01 ~

T = int(input())

for tc in range(1, T + 1):
    n, l = map(int, input().split())
    score_calories = []
    dp = [[0] * (l + 1) for _ in range(n + 1)]
    for _ in range(n):
        t, k = map(int, input().split())
        score_calories.append((t, k))

    score_calories.sort(key=lambda x: x[1])

    for i in range(1, n + 1):
        for j in range(l + 1):
            now_score, now_calories = score_calories[i - 1]
            if j - now_calories <= 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j - now_calories] + now_score, dp[i - 1][j])

    max_score = dp[n][l]
    print(f"#{tc} {max_score}")
