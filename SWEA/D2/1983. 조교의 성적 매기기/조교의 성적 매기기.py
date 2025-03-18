T = int(input())

for test_case in range(1, T + 1):
    grade = {0: "A+", 1: "A0", 2: "A-", 3: "B+", 4: "B0", 5: "B-", 6: "C+", 7: "C0", 8: "C-", 9: "D0"}
    n, k = map(int, input().split())
    scale = n // 10
    scores = []

    for i in range(n):
        middle, last, homework = map(int, input().split())
        scores.append(middle * 35 + last * 45 + homework * 20)

    k_score = scores[k - 1]
    scores.sort(reverse=True)

    for idx, score in enumerate(scores):
        if score == k_score:
            print(f"#{test_case} {grade[idx//scale]}")

