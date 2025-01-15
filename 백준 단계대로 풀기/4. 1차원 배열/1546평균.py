import sys

inputF = sys.stdin.readline

n = int(inputF().rstrip())
arr = list(map(int,inputF().rstrip().split()))

maxNum = max(arr)
arr = list(map(lambda x:x/maxNum*100, arr))
arrAverage = sum(arr)/n # 3으로 나누면 안된다 병신아. 주어진 개수로 나누어야한다.
print(arrAverage)
