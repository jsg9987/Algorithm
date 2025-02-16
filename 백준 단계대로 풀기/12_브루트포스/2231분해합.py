if __name__ == '__main__':
    n = int(input())
    min_result = n
    for x in range(1, n+1):
        arr = list(map(int, str(x)))
        if n == (sum(arr) + x) and x < min_result : # and 조건을 빼고 최소를 찾으면 break하는 것도 가능
            min_result = x

    if min_result == n:
        print(0)
    else:
        print(min_result)
