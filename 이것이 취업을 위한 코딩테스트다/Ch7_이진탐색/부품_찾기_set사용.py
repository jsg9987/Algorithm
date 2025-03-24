n = int(input())
array = set(map(int, input().split())) # set에서는 search가 O(1)의 시간복잡도를 가진다.
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')