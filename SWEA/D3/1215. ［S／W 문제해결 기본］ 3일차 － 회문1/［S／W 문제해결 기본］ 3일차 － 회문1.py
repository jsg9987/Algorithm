# 4/24 16:10 ~ 22

for tc in range(1, 11):
    word_len = int(input())
    board = [input() for _ in range(8)]
    result = 0

    for row in board:
        for j in range(8 - word_len + 1):
            word = row[j:j + word_len]
            word_reverse = word[::-1]
            if word == word_reverse: # if word == word[::-1]로 개선 가능
                result += 1

    for i in range(8):
        for j in range(8 - word_len + 1):
            temp = ""
            for offset in range(word_len):
                temp += board[j + offset][i]
            temp_reverse = temp[::-1]
            if temp == temp_reverse:
                result += 1

    print(f"#{tc} {result}")