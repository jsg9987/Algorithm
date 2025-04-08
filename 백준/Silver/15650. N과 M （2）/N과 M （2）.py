n,m = map(int, input().split())
s = []
visited = [False for _ in range(n+1)]

def dfs():
    # 정답이라면 출력
    if len(s) == m:
        check = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                check = False
        if check:
            print(' '.join(map(str, s)))
        return
    # 정답이 아니라면
    # 모든 자식노드에 대해
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

dfs()