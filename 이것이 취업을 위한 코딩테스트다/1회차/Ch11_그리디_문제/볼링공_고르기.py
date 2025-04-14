import sys

inputF = sys.stdin.readline
n, m = map(int, inputF().rstrip().split())
weights = list(map(int, inputF().rstrip().split()))
result = 0

for i in range(n-1):
    for j in range(i+1, n):
        if weights[i] != weights[j]:
            result += 1

print(result)