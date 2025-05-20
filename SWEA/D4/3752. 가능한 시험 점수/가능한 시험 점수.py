T = int(input())

for tc in range(1, T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    dp = [False] * 10001
    dp[0] = True

    for score in scores:
        for i in range(10000, -1, -1):
            if dp[i]:
                if i + score <= 10000:
                    dp[i+score] = True

    print(f"#{tc} {dp.count(True)}")