T = int(input())

for test_case in range(1, T+1):
    sdoqu = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        for j in range(1, 10):
            if sdoqu[i].count(j) != 1:
                result = 0
                break
        if result == 0:
            break

    for i in range(9):
        check = [0 for _ in range(10)]
        for j in range(9):
            check[sdoqu[j][i]] += 1
            if check[sdoqu[j][i]] != 1:
                result = 0
                break
        if result == 0:
            break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0 for _ in range(10)]
            for k in range(3):
                for l in range(3):
                    check[sdoqu[i+k][j+l]] += 1
                    if check[sdoqu[i+k][j + l]] != 1:
                        result = 0
                        break
                if result == 0:
                    break

    print(f"#{test_case} {result}")