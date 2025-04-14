import sys

inputF = sys.stdin.readline
n = int(inputF())
li = list(map(int, inputF().rstrip().split()))
li.sort()
mid = len(li) // 2
avg = sum(li) / n

if mid % 2 == 0:
    if abs(li[mid-1] - avg):
        print(li[mid-1])
    else:
        print(li[mid])
else:
    print(li[mid])