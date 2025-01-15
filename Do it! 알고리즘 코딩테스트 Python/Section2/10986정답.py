import sys

inputF = sys.stdin.readline
n,m = map(int, inputF().rstrip().split())
arr = list(map(int,inputF().rstrip().split()))
sumArr = [0 for i in range(n)]
answer =0
C = [0 for i in range(m)]


for i in range(n): # 구간합배열 저장
    if i==0:
        sumArr[i] = arr[i]
    else:
        sumArr[i] = sumArr[i-1] + arr[i]

for i in range(n): # 구간합배열의 나머지 
    remainer = sumArr[i] % m
    if(remainer ==0): # 구간합 나머지가 0인 구간
        answer+=1
    C[remainer] +=1 # 나머지가 같은 것들이 몇 개 있는지 리스트에 담기

for i in range(m): # 0은 이미 더함.
    if C[i]>1: # 2개 이상일때만 가능함
        answer += (C[i]*(C[i]-1)//2) # 주의! 파이썬에서 실수로 나오므로 // 사용

print(answer)
