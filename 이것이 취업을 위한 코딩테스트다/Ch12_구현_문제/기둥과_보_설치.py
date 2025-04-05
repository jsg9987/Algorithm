# 일부 tc만 통과됨.

def solution(n, build_frame):
    pillar = [[0] * (n + 1) for _ in range(n + 1)]
    paper = [[0] * (n + 1) for _ in range(n + 1)]
    pillar_coordinate = []  # 기둥 좌표 저장
    paper_coordinate = []  # 보 좌표 저장
    frame = [[0] * (n + 1) for _ in range(n + 1)]
    for col, row, a, b in build_frame:
        if b == 1:
            if a == 0:
                # 기둥 설치 가능하다면 설치
                if check_possible(col, row, a, frame):
                    frame[row][col] = 1
                    pillar_coordinate.append((col, row))
            elif a == 1:
                # 보 설치 가능하다면 설치
                if check_possible(col, row, a, frame):
                    frame[row][col] = 2
                    paper_coordinate.append((col, row))
        elif b == 0:
            if a == 0:
                frame[row][col] = 0
                pillar_coordinate.remove((col, row))
                for i, j in pillar_coordinate:
                    # 제거 후 조건에 부합하지 않으면 복구
                    if not check_possible(i, j, a, frame):
                        frame[row][col] = 1
                        pillar_coordinate.append((col, row))
                        break
            elif a == 1:
                frame[row][col] = 0
                paper_coordinate.remove((col, row))
                for i, j in paper_coordinate:
                    # 제거 후 조건에 부합하지 않으면 복구
                    if not check_possible(i, j, a, frame):
                        frame[row][col] = 2
                        paper_coordinate.append((col, row))

    result = []
    for x, y in pillar_coordinate:
        result.append([x, y, 0])
    for x, y in paper_coordinate:
        result.append([x, y, 1])

    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return result


def check_possible(col, row, type, frame):
    if type == 0:  # 기둥 설치 가능한 지 판별
        # 바닥인 경우 기둥 설치 가능
        if row < len(frame) - 1:
            if row == 0:
                return True
            if frame[row][col] == 2 or frame[row][col - 1] == 2:  # 보 한쪽 위인 경우
                return True
            if row - 1 >= 0 and frame[row - 1][col] == 1:  # 기둥 위인 경우
                return True
    elif type == 1:  # 보 설치 가능한 지 판별
        if row > 0 and col < len(frame) - 1:
            if row - 1 >= 0 and frame[row - 1][col] == 1:  # 왼쪽 끝이 기둥 위인 경우
                return True
            if row - 1 >= 0 and col + 1 <= len(frame) - 1 and frame[row - 1][col + 1] == 1:  # 오른쪽 끝이 기둥 위인 경우
                return True
            if frame[row][col - 1] == 2 and frame[row][col + 1] == 2:  # 양쪽 끝이 보인 경우
                return True
    return False


if __name__ == '__main__':
    n = 5
    build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
                   [3, 2, 1, 1]]
    result = solution(n, build_frame)
    print(result)
