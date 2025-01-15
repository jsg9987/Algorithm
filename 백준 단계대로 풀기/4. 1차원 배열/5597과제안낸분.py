import sys

inputF = sys.stdin.readline
fir = 0
sec = 0
k = 0
printArr = [0]*2
arr = [0 for i in range(30)]
for i in range(28):
    n = int(inputF().rstrip())
    arr[n-1] = n
    # if arr[n-1] == 0:
    #     printArr[k] = n
    #     k+=1 -> 이렇게하면 빈 n인덱스의 방에 접근을 못함

for i in range(30):
    if arr[i] == 0:
        printArr[k] = i+1 # arr에서 forEach로 불러와서 i라고 하면 안됨. i의 인덱스 번호를 알 수 없음.
        k+=1

for i in printArr:
    print(i)