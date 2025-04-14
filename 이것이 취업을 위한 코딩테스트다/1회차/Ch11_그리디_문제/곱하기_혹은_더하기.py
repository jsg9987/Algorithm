import sys

inputF = sys.stdin.readline
li = list(map(int, list(inputF().rstrip())))
result = li[0]

for i in range(1,len(li)):
    plus = result + li[i]
    mul = result * li[i]

    result = max(plus, mul)

print(result)
