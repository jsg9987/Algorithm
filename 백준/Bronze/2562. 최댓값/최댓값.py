import sys

inputF = sys.stdin.readline
maxNum = 0
listA = []
index = 0

for i in range(9):
    a = int(inputF().rstrip())
    listA.append(a)
    if a > maxNum:
        maxNum = a
    index = listA.index(maxNum) + 1

print(maxNum)
print(index)