# 행을 기준으로 수확 범위 표현 가능

T = int(input())

for tc in range(1,  T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    result = 0

    for i in range(n):
        offset = abs(mid - i)
        result += sum(board[i][offset:n-offset])

    print(f"#{tc} {result}")
