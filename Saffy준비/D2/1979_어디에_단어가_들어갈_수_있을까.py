T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        word_len = 0

        for j in range(n):
            # 가로
            if puzzle[i][j] == 1:
                word_len += 1
            if puzzle[i][j] == 0 or j == n - 1:
                if word_len == k:
                    result += 1
                word_len = 0

        for j in range(n):
            # 세로
            if puzzle[j][i] == 1:
                word_len += 1
            if puzzle[j][i] == 0 or j == n - 1:
                if word_len == k:
                    result += 1
                word_len = 0

    print(f"#{test_case} {result}")