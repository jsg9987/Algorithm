n, m = map(int, input().split())
row, col, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board[row][col] = 2
cnt = 1
turn_time = 0
while True:
    # 1. 현재 방향 기준 왼쪽 방향부터 차례대로 갈 곳을 정한다.
    d = (d + 1) % 4
    next_row = row + dx[3 - d] # 개선점: (3 - d)가 무엇을 의미하는지 알기 힘든 것 같다. 방향 전환에 관련된 함수를 따로 만들어서 direction변수만 넣어주는게 좋을듯
    next_col = col + dy[3 - d]
    turn_time += 1 # 문제점: 조건에서 왼쪽 방향에 갈 수 없을 경우 회전만 수행하고 1단계로 돌아간다 했다. -> 시행 순서 2의 else문에 들어가야함.

    # 2. 캐릭터의 왼쪽 방향에 가보지 않은 칸이 존재한다면, 왼쪽으로 회전하고 전진한다. 그게 아니라면 회전만 하고 1단계로 돌아간다.
    if board[next_row][next_col] == 0:
        row = next_row
        col = next_col
        board[row][col] = 2
        cnt += 1
        turn_time = 0
        # 문제, 개선점: 1단계로 돌아간다했는데, 그에 관한 코드가 없다. 아래 코드가 어짜피 실행은 안되겠지만 continue 사용이 좋아보임.

    # 3. 만약 네 방향 모두 가본 칸 or 바다라면, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 뒤쪽 방향이 바다라면 break
    if turn_time == 4:
        if board[row - dx[3 - d]][col - dy[3 - d]] == 2:
            row = row - dx[3 - d] # 의미상으로 본다면 row도 되돌려줘야 하지만, next_row도 되돌려주는게 맞는건가? 어짜피 재할당해서 코드도 줄이고 필요없는 것인가
            col = col - dy[3 - d]
            turn_time = 0
        elif board[row - dx[3 - d]][col - dy[3 - d]] == 1:
            break
print(cnt)

