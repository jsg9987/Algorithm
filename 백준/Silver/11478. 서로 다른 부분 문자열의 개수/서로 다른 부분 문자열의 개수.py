import sys

if __name__ == '__main__':
    arr = sys.stdin.readline().rstrip()
    n = 0
    s = set()
    while n <= len(arr):
        for i in range(len(arr) - n):
            s.add(arr[i:i + n + 1])
        n += 1

    print(len(s))
