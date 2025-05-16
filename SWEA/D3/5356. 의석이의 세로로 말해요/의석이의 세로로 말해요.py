# 5/16 16:44 ~
T = int(input())

for tc in range(1, T+1):
    li = []
    for _ in range(5):
        li.append(input())

    max_len = 0
    for i in li:
        max_len = max(max_len, len(i))

    str_arr = [["-1"] * max_len for _ in range(max_len)]
    for i in range(5):
        j = 0
        for alphabet in li[i]:
            str_arr[i][j] = alphabet
            j += 1

    result = ""
    for i in range(max_len):
        for j in range(max_len):
            if str_arr[j][i] != "-1":
                result += str_arr[j][i]

    print(f"#{tc} {result}")
