T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    puzzle2 = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            puzzle2[i][j] = puzzle[j][i]

    for i in range(n):
        if puzzle[i].count(1) == k: # 반례가 있다. 2 길이가 2개 있을 수도 있기 때문 -> 수정 필ㅇ
            li = list(filter(lambda x: puzzle[i][x] == 1, range(len(puzzle[i]))))
            for j in range(len(li)-1):
                if li[j] + 1 != li[j+1]:
                    break
                cnt += 1

        if puzzle2[i].count(1) == k:
            li = list(filter(lambda x: puzzle[i][x] == 1, range(len(puzzle[i]))))
            for j in range(len(li) - 1):
                if li[j] + 1 != li[j + 1]:
                    break
                cnt += 1

    print(f"#{test_case} {cnt}")

