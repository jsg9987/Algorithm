T = int(input())

for test_case in range(1, T+1):
    scores = list(map(int, input().split()))
    scores.remove(min(scores))
    scores.remove(max(scores))

    print(f"#{test_case} {round(sum(scores) / len(scores))}")