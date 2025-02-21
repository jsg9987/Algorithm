import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    arr = list(map(int, inputF().rstrip().split()))
    dic = {}

    for num in arr:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    m = int(inputF().rstrip())
    arr2 = list(map(int, inputF().rstrip().split()))

    for num in arr2:
        if num in dic:
            print(dic[num], end=" ")
        else:
            print(0, end=" ")
