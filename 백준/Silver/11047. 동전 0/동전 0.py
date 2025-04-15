n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
result = 0

for i in range(n-1, -1, -1):
    if k // coin[i] > 0:
        result += k // coin[i]
        k -= (k // coin[i]) * coin[i]

print(result)
