if __name__ == '__main__':
    possible = False
    min5_3 = 5000
    min5 = 5000
    min3 = 5000
    n = int(input())

    # 가능한지 가능하지 않은지를 판단할 때 5로 나눈 나머지를 3으로 나누면 가능한데 불가능하다고 나올 수 있다.
    for i in range(0, 1001):
        for j in range(0, 1667):
            if n == 5*i and i < min5:
                min5 = i
                possible = True
            if n == 3*j and j < min3:
                min3 = j
                possible = True
            if n == 5*i + 3*j and i + j < min5_3:
                min5_3 = i + j
                possible = True

    if possible:
        print(min(min5_3, min5, min3))
    elif not possible:
        print(-1)