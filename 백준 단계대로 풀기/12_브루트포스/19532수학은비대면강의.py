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


'''
모든 경우의 수를 찾는 풀이(브루트 포스)

a,b,c,d,e,f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)
'''

'''
근의 공식 사용
a, b, c, d, e, f = map(int, input().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))
'''
