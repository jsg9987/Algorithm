# 5/12 16:20 ~
T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    candies.sort()
    min_diff = int(1e9)

    for i in range(n-k+1):
        diff = candies[i+k-1] - candies[i]
        min_diff = min(min_diff, diff)

    print(f"#{tc} {min_diff}")
