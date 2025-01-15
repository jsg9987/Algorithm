import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())
arr = [None for i in range(n)]
setArr = [None for i in range(n)]
groupCheck = True
count = 0
for i in range(n):
    arr[i] = str(inputF().rstrip())

for i in range(n):
    setArr[i] = set(arr[i])

for i in range(n):
    groupCheck = True
    for j in setArr[i]:
        word = str(arr[i]).lstrip(j)
        if j in word or word=="":
            groupCheck = False
        if groupCheck == True:
            count+=1

print(count)