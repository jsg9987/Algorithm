import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())
arr = list(map(int, inputF().rstrip().split()))
ansArr = [0 for i in range(n)]
stack = []

for i in range(n):
    while stack and arr[stack[-1]]<arr[i]:
        # 변수명 자체로 true, false 반환 가능
        ansArr[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    ansArr[stack.pop()] = -1

for i in ansArr:
    print(i, end=" ")