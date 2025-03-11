import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
    
listA = list(map(int, sys.stdin.readline().rstrip().split()))
lenA = len(listA)

listB = []
for i in listA:
    if i>= x:
        listB.append(i)

i = 0
while i<len(listB):
    if listB[i] in listA:
        listA.remove(listB[i])
    i +=1

for i in listA:
    print(i, end=" ")