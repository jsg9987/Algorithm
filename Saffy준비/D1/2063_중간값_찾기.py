n = int(input())
scores = list(map(int, input().split()))
scores.sort()

print(scores[int(len(scores)/2)])