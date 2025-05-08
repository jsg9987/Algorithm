# 5/8 21:17 ~ 21:48

T = int(input())

for _ in range(T):
    n, p = map(int, input().split())
    max_floor = 0

    for i in range(1,n+1):
        temp_result = 0
        for j in range(i, n+1):
            temp_result += j
            if temp_result == p:
                break
        else:
            max_floor = temp_result
            break

    print(max_floor)