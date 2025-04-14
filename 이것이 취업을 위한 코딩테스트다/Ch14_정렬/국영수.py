import sys

inputF = sys.stdin.readline
n = int(inputF())
scores = [list(inputF().rstrip().split()) for _ in range(n)]

scores.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(scores[i][0])