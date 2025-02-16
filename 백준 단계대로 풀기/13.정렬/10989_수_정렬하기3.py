import sys
if __name__ == '__main__':
    inputF = sys.stdin.readline

    n = int(input())
    arr = [0] * 10001

    for _ in range(n):
        arr[int(inputF().rstrip())] += 1

    for i in range(len(arr)):
        if i != 0:
            for _ in range(arr[i]):
                print(i)

