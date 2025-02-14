import sys
if __name__ == '__main__':
    inputF = sys.stdin.readline

    n = int(input())
    arr = [0] * 10001

    for _ in range(n):
        arr[int(inputF().rstrip())] += 1

    for i, num in enumerate(arr):
        if num != 0:
            for _ in range(num):
                print(i)

