import sys

inputF = sys.stdin.readline

pSum = 0
n = int(inputF().rstrip())
p = list(map(int, inputF().rstrip().split()))

for i in range(n):
    for j in range(0, i+1):
        if p[i] < p[j]:
            temp = p[i]
            for t in range(i-1, j-1,-1):
                p[t+1] = p[t]
            p[j] = temp

for i in range(n):
    for j in range(i+1):
        pSum += p[j]
        
print(pSum)