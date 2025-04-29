T = int(input())


def dfs(idx, current_sum):
    global result

    if current_sum > k:
        return
    if idx == n: # 끝 인덱스에 도착했을 때 각 자리의 숫자를 골랐는지, 고르지 않았는지 확인 가능
        if current_sum == k:
            result += 1
        return

    dfs(idx + 1, current_sum + nums[idx])  # 현재 원소를 고르거나
    dfs(idx + 1, current_sum)  # 고르지 않거나


for tc in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    result = 0

    dfs(0,0)
    print(f"#{tc} {result}")