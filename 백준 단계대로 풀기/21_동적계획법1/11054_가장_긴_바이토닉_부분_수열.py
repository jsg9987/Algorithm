n = int(input())
dp = [1] * 1000
A = list(map(int, input().split()))
A_reverse = A[::-1]
dp_reverse = [1] * 1000
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:  # 증가 dp
            dp[i] = max(dp[i], dp[j] + 1)
        if A_reverse[i] > A_reverse[j]:  # 감소 dp 역순으로
            dp_reverse[i] = max(dp_reverse[i], dp_reverse[j] + 1)

result = [0] * 1000
for i in range(n):
    result[i] = dp[i] + dp_reverse[n - 1 - i] - 1

print(max(result))
