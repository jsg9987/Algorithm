def is_palindrome(s):
    return s == s[::-1]


for _ in range(10):
    tc = int(input())
    board = [input().strip() for _ in range(100)]
    max_len = 0

    for l in range(100, 0, -1):
        found = False
        for i in range(100):
            for j in range(100 - l + 1):
                # 가로 회문 체크
                row_slice = board[i][j:j + l]
                if is_palindrome(row_slice):
                    max_len = l
                    found = True
                    break

                # 세로 회문 체크
                col_slice = ''.join(board[j+k][i] for k in range(l))
                if is_palindrome(col_slice):
                    max_len = l
                    found = True
                    break
            if found:
                break
        if found:
            break

    print(f"#{tc} {max_len}")
