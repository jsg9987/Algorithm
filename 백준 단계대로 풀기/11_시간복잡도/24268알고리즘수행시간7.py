if __name__ == '__main__':
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())

    if a1 * n0 + a0 <= c * n0 and a1 <= c: # 빅오에서 a1보다 c가 같거나 크면 항상 하한의 값이 존재함.
        print(1)
    else:
        print(0)
