import sys
from collections import deque

if __name__ == '__main__':
    inputF = sys.stdin.readline
    deq = deque([])

    n = int(inputF().rstrip())

    for _ in range(n):
        li = inputF().rstrip().split()
        if int(li[0]) == 1:
            deq.appendleft(li[1])
        elif int(li[0]) == 2:
            deq.append(li[1])
        elif int(li[0]) == 3:
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif int(li[0]) == 4:
            if deq:
                print(deq.pop())
            else:
                print(-1)
        elif int(li[0]) == 5:
            print(len(deq))
        elif int(li[0]) == 6:
            if not deq:
                print(1)
            else:
                print(0)
        elif int(li[0]) == 7:
            if deq:
                print(deq[0])
            else:
                print(-1)
        elif int(li[0]) == 8:
            if deq:
                print(deq[-1])
            else:
                print(-1)
