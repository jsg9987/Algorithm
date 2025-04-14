# 오답: 아이디어 오류(치킨집에서 전체 집의 거리가 제일 긴 것 순으로 제거하는 것은 맞지않다.)
import sys

inputF = sys.stdin.readline
n, m = map(int, inputF().rstrip().split())
board = [list(map(int, inputF().rstrip().split())) for _ in range(n)]
chicken_coordinate = []
house_coordinate = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken_coordinate.append((i, j))
        elif board[i][j] == 1:
            house_coordinate.append((i, j))

chicken_dist = []
for x1, y1 in chicken_coordinate:
    temp_dist = 0
    for x2, y2 in house_coordinate:
        temp_dist += abs(x1 - x2) + abs(y1 - y2)
    chicken_dist.append((temp_dist, x1, y1))

chicken_dist.sort(key= lambda x: x[0])
# 전체 거리 먼 순으로 제거
while len(chicken_dist) != m:
    chicken_dist.pop()

result = 0
# 남은 치킨집 좌표들만 가지고 각각의 집에서 가장 가까운 치킨 거리를 result에 더한다.
for x1, y1 in house_coordinate:
    min_dist = int(1e9)
    for _, x2, y2 in chicken_dist:
        if abs(x1-x2) + abs(y1-y2) < min_dist:
            min_dist = abs(x1-x2) + abs(y1-y2)
    result += min_dist

print(result)