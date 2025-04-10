dp = [0] * 1000001
dp[1], dp[2], dp[3] = 0, 1, 1
n = int(input())
for i in range(4, n + 1):  # 3가지 케이스에서 최소가 되는 값으로 업데이트 해야함. -> 3가지 경우 모두 따져봐야함.
    dp[i] = dp[i - 1] + 1 # 항상 처리됨.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0: # 조건식 안에 들어갈 수도 있고, 안 들어갈 수도 있음.
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])
