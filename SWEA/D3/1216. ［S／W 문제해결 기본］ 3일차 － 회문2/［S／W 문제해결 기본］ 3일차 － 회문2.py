# 4/24 23:07 ~

for _ in range(10):
    tc = int(input())
    board = []
    max_len = 0
    for i in range(100):
        row = input()
        for length in range(1,101):
            for j in range(100):
                word = row[j:j+length]
                word_rev = word[::-1]
                if word == word_rev:
                    max_len = max(max_len, len(word))
        board.append(row)

    for i in range(100):
        for length in range(1, 101):
            for j in range(100):
                last_idx = min(100, j+length)
                word = ''.join(str(board[row][i]) for row in range(j, last_idx))
                word_rev = word[::-1]
                if word == word_rev:
                    max_len = max(max_len, len(word))

    print(f"#{tc} {max_len}")