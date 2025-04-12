n = int(input())
a = [0] * 1000
data = list(map(int, input().split()))
for i in range(len(data)):
    a[i] = data[i]
max_value = a[0]
dp = [1] * 1000 # 부분순열의 최소 길이는 1
dp[0] = 1

for i in range(1,n):
    for j in range(i):
        if a[i] > a[j]: # 만약 앞의 모든 수보다 작다면, a[i]를 포함하는 최대 부분순열 길이는 1
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))