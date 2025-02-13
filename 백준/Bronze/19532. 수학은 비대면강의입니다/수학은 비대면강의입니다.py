if __name__ == '__main__':
    # 에러발생 ZeroDivisionError
    x = 0
    y = 0
    a, b, c, d, e, f = map(int, input().split())

    if a == 0:
        y = int(c / b)
        x = int((f - e * y) / d)
    elif b == 0:
        x = int(c / a)
        y = int((f - d * x) / e)
    elif d == 0:
        y = int(f / e)
        x = int((c - b * y) / a)
    elif e == 0:
        x = int(f / d)
        y = int((c - a * x) / b)
    else:
        b *= d
        c *= d
        e *= a
        f *= a
        y = (c - f) / (b - e)
        x = (c - (b * y)) / (a * d)

    print(int(x), int(y))

    