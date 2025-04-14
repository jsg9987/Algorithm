# 90도 회전
def rotate(key):
    n = len(key)
    m = len(key[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = key[i][j]
    return result


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # key를 넣을 수 있는 모든 경우를 위해 lock 크기를 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 중앙 부분에 lock 정보 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향 확인
    for rotation in range(4):
        key = rotate(key)
        for x in range(2 * n):
            for y in range(2 * n):
                # key 범위
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 맞는지 검사
                if check(new_lock):
                    return True
                # 틀렸으면 다시 열쇠값 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False
