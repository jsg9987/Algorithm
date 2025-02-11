if __name__ == '__main__':
    n = int(input())
    min_result = n
    for x in range(1, n):
        arr = list(map(int, str(x)))
        if n == (sum(arr) + x) and x < min_result :
            min_result = x
            
    if min_result == n:
        print(0)
    else:
        print(min_result)
