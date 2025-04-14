import heapq


def solution(food_times, k):

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식 개수

    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length # 직접 값을 빼서 갱신할 수 없으므로 두 변수를 이용해서 남은 시간을 표현함.
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 먹는데 걸린 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인해 출력
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]