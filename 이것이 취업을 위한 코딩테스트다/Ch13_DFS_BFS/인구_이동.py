import sys
from sys import setrecursionlimit
setrecursionlimit(10**6)
# 이 문제를 풀면서 부족했던 점: 변수 초기화를 어디에서 할 것인지 고민하는데 시간 많이 소비함.

# 놓친 점: 인구 이동은 날짜이다. 그날 한번 이상 이동했다면 날짜 += 1
inputF = sys.stdin.readline
n, l, r = map(int, inputF().split())
board = [list(map(int, inputF().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
coordinates = []
countries = []
result = 0


def process(x, y, l, r):
    possible = False
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if visited[x][y] == 0:
        visited[x][y] = 1
        # 연합에 해당하는 좌표들 추가
        countries.append((x, y))
    # 각 칸에 대해서 인구 차이를 확인하고  국경선 열기(가능한 곳 모두 1로 바꾸기, 끝날 때 마다 인구 이동 1 증가)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and visited[nx][ny] == 0:
            if l <= abs(board[x][y] - board[nx][ny]) <= r:
                process(nx, ny, l, r)
                possible = True
    if possible:
        return True
    return False


def move_people(countries):
    population = 0
    # 해당 좌표들에 새로운 인구수 할당(소수점 내림)
    for x, y in countries:
        population += board[x][y]
    new_population = int(population / len(countries))
    for x, y in countries:
        board[x][y] = new_population


while True:
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if process(i, j, l, r):
                    coordinates.append(countries)
                countries = [] # 놓친점: 현재 로직에서 방문한 점 자체를 countries에 넣고 있으므로 다음 점을 검사하기 전에 초기화 필요
    if not coordinates:
        break
    else:
        result += 1

    # 새로운 인구 할당
    for x in coordinates:
        move_people(x)

    # 연합 해체하고, 좌표 초기화, 모든 나라 방문 0으로 복구
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0

    coordinates = []

print(result)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# n, l, r = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# def dfs(x, y, visited, union):
#     visited[x][y] = 1
#     union.append((x, y))
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             diff = abs(board[x][y] - board[nx][ny])
#             if l <= diff <= r:
#                 dfs(nx, ny, visited, union)
#
#
# def move_people(union):
#     total = sum(board[x][y] for x, y in union)
#     new_pop = total // len(union)
#     for x, y in union:
#         board[x][y] = new_pop
#
#
# def reset_visited():
#     return [[0] * n for _ in range(n)]
#
#
# result = 0
#
# while True:
#     visited = reset_visited()
#     moved = False
#
#     for i in range(n):
#         for j in range(n):
#             if not visited[i][j]:
#                 union = []
#                 dfs(i, j, visited, union)
#                 if len(union) > 1:
#                     move_people(union)
#                     moved = True
#
#     if not moved:
#         break
#     result += 1
#
# print(result)
