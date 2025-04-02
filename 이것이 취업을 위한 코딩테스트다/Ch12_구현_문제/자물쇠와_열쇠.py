# 코드 실행 안됨

def move(dir, move_time, key):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    key_next = [[0 for _ in range(len(key))] for _ in range(len(key[0]))]

    for i in range(len(key)):
        for j in range(len(key[0])):
            if i + dr[dir] >= 0 and i + dr[dir] < len(key) and j + dc[dir] >= 0 and j + dc[dir] < len(key):
                key_next[i + dr[dir]][j + dc[dir]] = key[i][j]

    return key_next


def turn(key):
    key_next = [[0 for _ in range(len(key))] for _ in range(len(key[0]))]
    for i in range(len(key)):
        for j in range(len(key[0])):
            key_next[j][len(key) - i - 1] = key[i][j]
    return key_next

def check(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] != 1:
                return False
    return True


# 문제점: 이 방식대로라면 key와 lock을 비교해서 확인해야 하는데, lock이 key보다 클 수 있고 lock에서 일부분이 key와 같을수도 있기 때문에 비교하기 애매하다.
def solution(key, lock):
    answer = False

    # 회전 횟수, 이동 횟수
    turn_time, move_time = 0, 0
    # 이동 방향
    dir = 0

    # 이동
    for i in range(4):
        dir = i
        for j in range(1,len(key)+1):
            move_time = j
            move(dir, move_time, key)
            for _ in range(4):
                temp_key = turn(key)
                for k in range(len(lock) - len(key)):
                    for l in range(len(lock[0]) - len(key)):
                        for m in range(len(key)):
                            for n in range(len(key)):
                                if temp_key[m][n] == 1:
                                    lock[k+m][l+n] += 1
                        if check(lock):
                            return True
                        for m in range(len(key)):
                            for n in range(len(key)):
                                if temp_key[m][n] == 1:
                                    lock[k+m][l+n] -= 1
    return False
