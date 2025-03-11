import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    A = list(map(int, inputF().rstrip().split()))
    B = deque(list(map(int, inputF().rstrip().split())))
    m = int(inputF().rstrip())
    C = (map(int, inputF().rstrip().split()))
    # next_B = deque([]) # 다음 B_Q 초기화를 밖에서 해줘서 계속 쌓이고 있다.
    result = []

    for return_num in C:
        for i in range(n):
            if A[i] == 0:
                B.append(return_num)
                return_num = B.popleft()
            elif A[i] == 1:
                B.append(B.popleft())

        result.append(return_num)

    for i in result:
        print(i, end=" ")





