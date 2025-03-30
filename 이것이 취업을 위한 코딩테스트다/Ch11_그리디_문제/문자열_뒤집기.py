import sys

inputF = sys.stdin.readline
arr = list(map(int, list(inputF().rstrip())))
result0 = 0
result1 = 0

if arr[0] == 0:
    result0 += 1
else:
    result1 += 1

for i in range(1, len(arr)):
    if arr[i-1] != arr[i] and arr[i] == 0:
        result0 += 1
    elif arr[i-1] != arr[i] and arr[i] == 1:
        result1 += 1
    '''
    # 위와 같은 코드
    if arr[i] != arr[i-1]:
        if s[i] == 0:
            count0 += 1
        else:
            count1 += 1
    '''

print(min(result0, result1))
