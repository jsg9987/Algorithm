T = int(input())

for test_case in range(1, T + 1):
    scores = list(map(int, input().split()))
    avg = round(sum(scores) / 10)

    print(f"#{test_case} {avg}")