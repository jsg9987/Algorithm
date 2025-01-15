import sys

inputF = sys.stdin.readline

arr = [[1 for _ in range(100)] for _ in range(100)]
sums = 0
n = int(inputF().rstrip())

for i in range(n):
    a,b = map(int, inputF().rstrip().split())
    
    for j in range(a, a+10): # 인덱스 0부터 시작하므로 a+1할 필요가 없었다. a가 곧 색종이 시작 지점임
        for k in range(90-b,100-b):
            arr[j][k] = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] == 0:
            sums += 1

print(sums)