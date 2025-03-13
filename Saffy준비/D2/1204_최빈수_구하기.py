T = int(input())

for test_case in range(1, T + 1):
    number = int(input())
    score_li = [0 for i in range(0, 101)]
    stud_score = list(map(int, input().split()))
    max_cnt = 0
    max_idx = 0

    for score in stud_score:
        score_li[score] += 1

    for idx, cnt in enumerate(score_li):
        if cnt >= max_cnt:
            if idx > max_idx:
                max_idx = idx
                max_cnt = cnt

    print(f"#{number} {max_idx}")
