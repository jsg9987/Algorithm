# 4/24 16:38 ~ 58
# dfs로 놓은 퀸 좌표들, 행 번호 전달

T = int(input())


def possible(coordinates, row, col):
    for x, y in coordinates:
        if y == col:
            return False
        if abs(x-row) == abs(y-col):
            return False
    return True


def dfs(coordinates, row):
    global result
    if row == n:
        result += 1
        return
    for i in range(n):
        if possible(coordinates, row, i): # 지금까지 추가한 좌표와 비교
            coordinates.append((row, i))
            dfs(coordinates, row + 1)
            coordinates.pop()


for tc in range(1, T + 1):
    n = int(input())
    result = 0
    dfs([], 0)
    print(f"#{tc} {result}")
