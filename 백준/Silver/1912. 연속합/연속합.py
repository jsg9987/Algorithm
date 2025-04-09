n = int(input())
li = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = li[0]

for i in range(1,n):
    dp[i] = max(li[i], dp[i-1] + li[i]) # 해당 칸에서 최대 구간합은 자신칸 또는 그 앞 연속합 + 자신칸 중 큰 값이다.

print(max(dp))