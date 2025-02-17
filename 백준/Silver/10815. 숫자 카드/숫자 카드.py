import sys
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(input())
    arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
    dic = {}

    for i in arr:
        dic[i] = 1

    for num in arr2:
        if num in dic:
            print(dic[num], end= " ")
        elif num not in dic:
            print(0, end= " ")