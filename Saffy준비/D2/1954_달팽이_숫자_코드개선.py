T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]
    num = 1
    row = 0
    col = 0
    seq = 0
    dir_x = x[0]
    dir_y = y[0]
    li = [[0 for _ in range(n)] for _ in range(n)]

    while num <= int(n * n):
        # 그 자리가 값이 0이면 값을 채운다. -> 그냥 값을 채워버려도 된다. 어짜피 잘못된 자리에 값을 채울 일 없을 것 같다. 대신 원래 row, col에 direction값을 더해주는 걸 여기에 추가해줘야함.
        li[row][col] = num
        num += 1
        row += dir_y
        col += dir_x
        # 그 자리가 값이 0이 아니면 방향을 전환한다. 그런데? != 0 조건은 row, col 값을 먼저 변화시킨 다음에 검사해서 확인하고 다시 빼도 될 것 같다
        # 만약 row, col의 값이 범위에서 벗어나면 방향 전환해준다. -> 여기에 이동한 곳이 0이 아닐 때 방향 전환하는 걸 합쳐도 될 것 같다.
        if row > n-1 or col > n-1 or row < 0 or col < 0 or li[row][col] != 0:
            row -= dir_y
            col -= dir_x
            seq = (seq+1) % 4
            dir_x = x[seq]
            dir_y = y[seq]
            row += dir_y
            col += dir_x

    print(f"#{test_case}")
    for i in li:
        print(" ".join(str(x) for x in i))