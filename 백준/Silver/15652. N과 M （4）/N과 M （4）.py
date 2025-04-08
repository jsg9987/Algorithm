n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        check = True
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                check = False
                return
        if check:
            print(*s)
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()

dfs(1)