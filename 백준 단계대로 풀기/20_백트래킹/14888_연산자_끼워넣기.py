# 함수 종료 조건: 연산자 모두 사용 후 최대, 최소값 갱신
n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = -int(1e9)
result = nums[0]


def dfs(i, result):
    global min_value, max_value
    global add, sub, mul, div

    if i == n:
        min_value = min(result, min_value)
        max_value = max(result, max_value)
        return

    if add > 0:
        add -= 1
        dfs(i+1, result + nums[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, result - nums[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, result * nums[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(result / nums[i]))
        div += 1


dfs(1, result)
print(max_value)
print(min_value)