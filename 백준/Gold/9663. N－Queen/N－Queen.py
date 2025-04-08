n = int(input())
visited = [0] * n
result = 0

def check(now_row):
    # 세로 검사
    # 대각선 검사(지금 행까지 검사)
    for row in range(now_row):
        if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
            return False
    return True


def dfs(row):
    global result
    if row == n:
        result += 1
        return

    for col in range(n):
        # 열의 위치 저장
        visited[row] = col
        if check(row):
            dfs(row+1)

dfs(0)
print(result)