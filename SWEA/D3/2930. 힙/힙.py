import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    heap = []
    result = []
    for _ in range(n):
        data = input().split()
        if data[0] == "2":
            if heap:
                result.append(-heapq.heappop(heap))
            else:
                result.append(-1)
        else:
            heapq.heappush(heap, -int(data[1]))
    print(f"#{tc} {' '.join(map(str, result))}")
