# 핵심 아이디어: 해당 단계에 머물러 있는 플레이어 수를 == 도달은 했는데 클리어는 못한 사람 수
# 머물러 있는 사람을 전체 인원에서 빼면 된다.
def solution(N, stages):
    answer = []
    length = len(stages) # 인원 수

    # 스테이지 1~N
    for i in range(1, N+1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x: -x[1])

    answer = [i[0] for i in answer]
    return answer

