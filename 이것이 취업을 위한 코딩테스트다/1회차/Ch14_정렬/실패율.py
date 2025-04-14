# 4/14 17:28 ~ 18:03
# 실패율 = 스테이지 도달했으나 아직 클리어 x 플레이어 수 / 스테이지 도달 플레이어 수
# 실패율이 높은 스테이지부터 "내림차순"으로 스테이지 번호가 담긴 배열 return
# 1 <= N <= 500, 1 <= stages <= 200,000
# N+1은 마지막 스테이지까지 클리어한 사용자
# 실패율이 같다면 작은 번호가 먼저 오도록
# 스테이지에 도달한 유저가 없을 경우, 해당 스테이지 실패율은 0


def solution(N, stages):
    answer = []
    not_clear = [0] * N
    arrival = [0] * N
    for stage in stages:
        if stage != N + 1:
            not_clear[stage - 1] += 1
        for i in range(stage):
            if i == N:
                break
            arrival[i] += 1

    fail_rate = []
    for i in range(N):
        if arrival[i] == 0:
            fail_rate.append((i, 0))
        else:
            fail_rate.append((i, not_clear[i] / arrival[i]))

    fail_rate.sort(key=lambda x: (-x[1], x[0]))
    for idx, _ in fail_rate:
        answer.append(idx + 1)

    return answer


print(solution(4, [4, 4, 4, 4, 4]))
