# 4/18 17:00~18:25
WALK_LIMIT = 1000
t = int(input())

def dfs(x,y,conv_xy, visited):
    if abs(penta_x - x) + abs(penta_y - y) <= WALK_LIMIT:
        return True

    for cx,cy in conv_xy:
        if abs(cx-x) + abs(cy-y) <= WALK_LIMIT and not visited[(cx,cy)]:
            visited[(cx,cy)] = 1
            possible = dfs(cx,cy,conv_xy,visited)
            if possible:
                return True

for tc in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    conv_xy = []
    visited = dict()
    for _ in range(n):
        x,y = map(int, input().split())
        visited[(x,y)] = 0
        conv_xy.append((x,y))
    penta_x, penta_y = map(int, input().split())
    visited[(hx,hy)] = 0
    possible = dfs(hx,hy,conv_xy,visited)

    if possible:
        print("happy")
    else:
        print("sad")

