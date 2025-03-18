T = int(input())

for test_case in range(1, T+1):
    scores = list(map(int, input().split()))
    scores.remove(min(scores))
    scores.remove(max(scores))

    print(f"#{test_case} {round(sum(scores) / len(scores))}")


'''
# 더 정확한 풀이
# 정렬한 후 맨 앞,뒤를 빼거나 슬라이싱해서 round()
T = int(input())
for test_case in range(1, T+1):
    round(sum(sorted(map(int, input().split()))[1:-1]/8))
'''