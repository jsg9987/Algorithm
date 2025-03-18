T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    repeat = 0
    long = None
    short = None
    li = None
    result = -float('inf')
    temp = 0

    if n >= m:
        repeat = n - m + 1
        long = list(map(int, input().split()))
        short = list(map(int, input().split()))
        li = [0 for _ in range(len(long))]
    else:
        repeat = m - n + 1
        short = list(map(int, input().split()))
        long = list(map(int, input().split()))
        li = [0 for _ in range(len(long))]

    for i in range(repeat):
        temp = 0 # 루프를 끝내고 초기화시켜야함.
        for j in range(len(short)):
            li[i+j] = short[j]
            temp += long[i+j] * li[i+j]
        if temp > result:
            result = temp
        li = [0 for _ in range(len(long))]  # 다시 계산하기 위한 list 초기화를 안해줬었다. 하지만 어짜피 3칸만 쓸거였기 때문에 초기화 안해도 무방


    print(f"#{test_case} {result}")





