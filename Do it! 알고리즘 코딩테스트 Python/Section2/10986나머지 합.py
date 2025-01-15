import sys

inputF = sys.stdin.readline

n,m = map(int, inputF().rstrip().split())
arr = list(map(int,inputF().rstrip().split()))
partSum = [0 for i in range(n)]
answer = 0

for i in range(n):
    for j in range(0,i):
        partSum[i] += arr[i]
        
for i in range(n):
    for j in range(n):
        if j>i:
            if i==0:
                if partSum[j]%m==0:
                    answer+=1
            elif (partSum[j]-partSum[i-1])%m==0:
                answer+=1
        elif j==i:
            if arr[i]%m==0:
                answer+=1

print(answer)
