n = int(input())
visited = [-1] * n
result = 0

def check(row):
    # 세로, 대각에 퀸이 없을 때 정답
    for now_row in range(n): # 그 이전의 행들을 검사
        if visited[now_row] != visited[row] and row - now_row == abs(visited[row] - visited[now_row]):
            return False
    return True


def dfs(row):
    global result
    # 정답
    if row == n:
        result += 1
        return

    # 가능한 모든 자식 노드에 대해
    for col in range(n):
        visited[row] = col
        if check(row):
            dfs(row+1)

dfs(0)
print(result)