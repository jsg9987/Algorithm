# 문제: 각 행들에서 가장 작은 값들을 뽑아서 그 중 최대값이 출력되게 전략을 세워라
# 아이디어: 1. 각 행에서 min값들을 리스트에 저장 후
#         2. 그 값들 중 max값을 출력
# 시간복잡도: O(NM)

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]
row_mins = []

for i in range(n):
    row_mins.append(min(cards[i]))

print(max(row_mins))