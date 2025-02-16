import sys

if __name__ == '__main__':
    n = int(input())
    inputF = sys.stdin.readline
    arr = []
    for _ in range(n):
        arr.append(int(inputF().rstrip()))

    arr.sort()
    for i in arr:
        print(i)