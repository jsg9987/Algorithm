def rotate(key,M):
    """ 시계 방향으로 90도 회전 """
    return [[key[M - 1 - j][i] for j in range(len(key))] for i in range(len(key))]


def can_unlock(key, lock, start_x, start_y):
    """ key를 특정 위치에 놓았을 때 lock을 열 수 있는지 확인 """
    N, M = len(lock), len(key)

    temp_lock = [row[:] for row in lock]  # 원본 lock을 복사하여 temp_lock 사용

    # 열쇠를 자물쇠에 적용
    for i in range(M):
        for j in range(M):
            x, y = start_x + i, start_y + j
            if 0 <= x < N and 0 <= y < N:  # lock 범위 내에서만 적용
                temp_lock[x][y] += key[i][j]

    # lock의 모든 값이 1인지 확인
    return all(all(cell == 1 for cell in row) for row in temp_lock)


def solution(key, lock):
    N, M = len(lock), len(key)

    # 4가지 회전 경우 확인
    for _ in range(4):
        key = rotate(key,M)  # 열쇠를 회전

        # 자물쇠를 덮을 수 있는 모든 위치 시도
        for x in range(-M + 1, N):
            for y in range(-M + 1, N):
                if can_unlock(key, lock, x, y):
                    return True

    return False
