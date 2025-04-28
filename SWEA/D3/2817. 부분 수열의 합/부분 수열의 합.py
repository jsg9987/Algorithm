# 4/28 11:05 ~


from itertools import combinations
T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    idxes = [i for i in range(n)]
    result = 0

    for i in range(1, n+1):
        candidates = list(combinations(idxes, i))
        for candidate in candidates:
            temp_sum = 0
            for idx in candidate:
                temp_sum += nums[idx]
            if temp_sum == k:
                result += 1

    print(f"#{tc} {result}")