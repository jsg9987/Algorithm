import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())

for i in range(n):
    m = int(inputF().rstrip())
    maxSum = 0
    arr = list(map(int, inputF().rstrip().split()))
    maxPrice = 0
    
    for val in arr[::-1]:
        if val >= maxPrice:
            maxPrice = val
        else :
            maxSum += maxPrice - val
    print("#", i+1, " ", maxSum, sep="")
