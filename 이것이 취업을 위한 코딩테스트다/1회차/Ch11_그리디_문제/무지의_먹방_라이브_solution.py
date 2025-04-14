import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 우선순위 큐에 남은 시간, 번호 순으로 넣기
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    total_time = 0
    previous = 0
    remain_food = len(q)

    # 가장 적게 걸리는 음식부터 처리하고 빼기
    while total_time + (q[0][0] - previous) * remain_food <= k:
        now = heapq.heappop(q)
        total_time += (now[0] - previous) * remain_food
        remain_food -= 1
        previous = now[0]

    result = sorted(q, key= lambda x: x[1]) # iterable 객체에서 튜플 하나씩 넘겨줌. # 원본 값은 그대로, 정렬한 새로운 리스트
    # print(q[0][1]) # k값을 1까지 낮춘게 아니라 임의의 변수로 처리해왔다. 따라서 k에서 total_time을 빼줘서 남은 k를 구해줘야한다.
    return result[(k - total_time) % remain_food][1]


