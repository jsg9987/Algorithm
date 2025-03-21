# 문제: 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 처음에는 (1,1)에 서있으며 이동 계획서에 적힌대로 이동한다. LRUD 각각의 알파벳에 따라 왼쪽,오른쪽,위,아래로 이동한다.
# 조건: 이때 여행가 A가 N x N 정사각형 공간을 벗어나는 움직임은 무시된다. 최종 좌표를 출력하라.
# 공간을 벗어나는 경우는 1미만, N 초과의 경우가 있다.

# 아이디어: 알파벳에 맞게 이동을 계산해주고, 계산 후 x,y 좌표가 1 미만이 될 경우 좌표를 원상복구하고 다음 계획을 수행한다.

n = int(input())
move_plan = input().split()
move = {'L': -1, 'R': 1, 'U': -1, 'D': 1}
row = 1
col = 1

for i in range(len(move_plan)):
    if move_plan[i] == 'L' or move_plan[i] == 'R':
        col += move[move_plan[i]]
        if col < 1 or col > n:
            col -= move[move_plan[i]]
    elif move_plan[i] == 'U' or move_plan[i] == 'D':
        row += move[move_plan[i]]
        if row < 1 or row > n:
            row -= move[move_plan[i]]

print(f"{row} {col}")
