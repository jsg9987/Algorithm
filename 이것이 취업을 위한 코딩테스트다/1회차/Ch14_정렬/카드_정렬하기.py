import heapq
# 아이디어: 작은 묶음끼리 먼저 합쳤을 때 비교 횟수가 줄어든다.
# 4/14 18:50~
n = int(input())
heap = []
result = 0

# for i in range(len(li) - 1):
#     result += li[i] + li[i+1] # 정렬을 유지하지 않기 때문에 잘못됐다. -> 항상 가장 작은 두 묶음을 선택해야하기 때문
#     li[i+1] = result

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)