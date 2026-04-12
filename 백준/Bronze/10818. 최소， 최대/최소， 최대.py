import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())

listA = list(map(int, inputF().rstrip().split()))
min = listA[0]
max = listA[0]
for i in listA:
    if i<min:
        min = i
    if i>max:
        max = i
print(min,max)