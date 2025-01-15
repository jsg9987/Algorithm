import sys

inputF = sys.stdin.readline

num1, num2 = map(str, inputF().rstrip().split())

num1 = int(num1[::-1])
num2 = int(num2[::-1])
if num1>num2:
    result= num1
    print(result)
else:
    result= num2
    print(result)

