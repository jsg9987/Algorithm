# 4/20 20:38
# 맨 앞자리부터 숫자가 제일 커지게 교환, 더 이상 교환이 불가하다면 맨 뒤에 2개를 가능한 교환

T = int(input())

def dfs(num, change):
    global result
    value = int(''.join(num))
    if change == 0:
        if value > result:
            result = value
        return

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            next_num = int(''.join(num))
            if (next_num,change-1) not in visited:
                visited.append((next_num, change-1))
                dfs(num, change - 1)
            num[i], num[j] = num[j], num[i]


for tc in range(1, T + 1):
    num, change = input().split()
    num = list(num)
    change = int(change)
    visited = []
    result = 0
    dfs(num, change)

    print(f"#{tc} {result}")
