import sys
import math

if __name__ == '__main__':
    inputF = sys.stdin.readline
    num = 123456 * 2 + 1
    num_list = [1] * num

    for i in range(1, num):
        if i == 1:
            continue
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                num_list[i] = 0
                break

    while True:
        cnt = 0
        n = int(inputF().rstrip())
        if n == 0:
            break

        for i in range(n + 1, 2 * n + 1):
            cnt += num_list[i]
        print(cnt)
