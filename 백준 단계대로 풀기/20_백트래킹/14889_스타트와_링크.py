n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_value = int(1e9)
team_start = []
def check(team_start):
    team_link = [i for i in range(1,n+1)]
    for i in team_start:
        team_link.remove(i)
    start_score = 0
    link_score = 0
    for i in team_start:
        for j in team_start:
            start_score += s[i-1][j-1]

    for i in team_link:
        for j in team_link:
            link_score += s[i-1][j-1]

    return abs(start_score - link_score)

def dfs(start):
    global min_value
    if len(team_start) == n // 2:
        min_value = min(min_value, check(team_start))
        return

    for i in range(start, n+1):
        team_start.append(i)
        dfs(i+1)
        team_start.pop()

dfs(1)
print(min_value)