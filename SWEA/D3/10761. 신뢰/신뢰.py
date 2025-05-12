# 5/12 18:01 ~35
from collections import deque

T = int(input())

for tc in range(1, T+1):
    queue = deque(input().split())
    n = queue.popleft()
    b = []
    o = []
    sequence = []
    b_location = 1
    o_location = 1
    second = 0

    while queue:
        robot = queue.popleft()
        if robot == 'B':
            sequence.append(robot)
            b.append(int(queue.popleft()))
        elif robot == 'O':
            sequence.append(robot)
            o.append(int(queue.popleft()))

    while True:
        next_b = -1
        next_o = -1
        push_turn = ''
        if sequence:
            push_turn = sequence[0]
        if b:
            next_b = b[0]
        if o:
            next_o = o[0]

        if b and next_b == b_location and push_turn == 'B':
            b.pop(0)
            sequence.pop(0)
        elif next_b < b_location:
            b_location -= 1
        elif next_b > b_location:
            b_location += 1

        if o and next_o == o_location and push_turn == 'O':
            o.pop(0)
            sequence.pop(0)
        elif next_o < o_location:
            o_location -= 1
        elif next_o > o_location:
            o_location += 1

        second += 1
        if not o and not b:
            break

    print(f"#{tc} {second}")





