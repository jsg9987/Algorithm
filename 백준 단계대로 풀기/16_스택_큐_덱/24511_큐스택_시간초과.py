import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    A = list(map(int, inputF().rstrip().split()))
    B = deque(list(map(int, inputF().rstrip().split())))
    m = int(inputF().rstrip())
    C = deque(list(map(int, inputF().rstrip().split())))
    # next_B = deque([]) # 다음 B_Q 초기화를 밖에서 해줘서 계속 쌓이고 있다.
    result = []
    # deque를 너무 많이 쓰고 복사해서 괜히 연산이 더 많이 됨.

    while C:
        next_B = deque([])
        return_num = C.popleft()
        for i in range(len(A)):
            if A[i] == 0:
                next_B.append(return_num)
                return_num = B[i]
            elif A[i] == 1:
                return_num = return_num
                next_B.append(B[i])

        B = next_B
        result.append(return_num)

    for i in result:
        print(i, end=" ")





