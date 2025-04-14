# 4/14 22:00~08
# 아이디어: 각 행에서 가장 작은 수를 리스트에 저장 후, 마지막에 그 중 가장 큰 값을 return
# 1 <= N,M <= 100

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
min_values = []

for i in range(n):
    min_values.append(min(li[i]))

print(max(min_values))