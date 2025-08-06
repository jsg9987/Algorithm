from collections import deque

inputF = input

dx = [-1,0,0]
dy = [0,-1,1]
result_x, result_y = 0,0
def bfs(i,j):
    global result_x, result_y
    q = deque([])
    q.append((i,j,0))

    while q:
        x,y,goSide = q.popleft()
        if x == 0:
            result_y = y
            break
        next = []
        flag = 0
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100:
                if arr[nx][ny] == 1:
                    if ny - y == -1:
                        flag = 1
                        next.append((nx, ny, -1))
                    elif ny - y == 1:
                        flag = 1
                        next.append((nx, ny, 1))
                    else:
                        next.append((nx, ny, 0))
        if flag:
            for i in next:
                a,b,c = i[0], i[1], i[2]
                # if len(next) == 2:
                if goSide == c and c != 0:
                    q.append((a,b,c))
                    break
                elif goSide == 0 and (c == 1 or c == -1):
                    q.append((a,b,c))
                    break
                elif (goSide == 1 or goSide == -1) and c == 0:
                    q.append((a,b,c))

        else:
            a,b,c = next[0]
            q.append((a,b,c))

    return None


for tc in range(1, 11):
    T = int(input())
    arr = [list(map(int, inputF().split())) for _ in range(100)]
    x,y = 99,0
    for i in range(0, 100):
        if arr[99][i] == 2:
            y = i

    bfs(x,y)
    print(f"#{T} {result_y}")
