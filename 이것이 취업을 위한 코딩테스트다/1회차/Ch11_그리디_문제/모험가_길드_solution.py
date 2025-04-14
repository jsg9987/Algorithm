# 필요한 건 그룹 인원수와 현재 보고 있는 모험가의 공포도
# 그렇다면 list가 아니라 그냥 변수로도 가능하다.

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)