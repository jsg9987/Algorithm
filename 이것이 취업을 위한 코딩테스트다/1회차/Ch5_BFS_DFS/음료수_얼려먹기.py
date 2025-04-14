def dfs(x, y):
    if x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 2
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
ice = [list(map(int, input())) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)