T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr2 = [[0 for _ in range(n)] for _ in range(n)]
    arr3 = [[0 for _ in range(n)] for _ in range(n)]
    arr4 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr2[j][n-i-1] = arr[i][j]

    for i in range(n):
        for j in range(n):
            arr3[j][n-i-1] = arr2[i][j]

    for i in range(n):
        for j in range(n):
            arr4[j][n-i-1] = arr3[i][j]
    
    print(f"#{test_case}")
    
    for i in range(n):
        print(*arr2[i], sep="", end=" ")
        print(*arr3[i], sep="", end=" ")
        print(*arr4[i], sep="")