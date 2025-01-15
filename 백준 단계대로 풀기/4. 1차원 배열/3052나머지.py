import sys

inputF = sys.stdin.readline

arr = [0 for i in range(42)]
k = 0
for i in range(10):
    num = int(inputF().rstrip())
    arr[num%42]+=1

for i in arr:
    if i != 0:
        k+=1

print(k)

