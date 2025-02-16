import sys
from operator import index

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        [age, name] = sys.stdin.readline().rstrip().split()
        arr.append([int(age), name])

    arr.sort(key= lambda x: (x[0]))

    for i in arr:
        print(i[0], i[1])


'''
stable 정렬과 unstable 정렬
stable 정렬: 입력 받은 값들 중 같은 값이 있는 경우 해당 값의 순서를 그대로 유지
파이썬은 기본적으로 stable 정렬!
'''