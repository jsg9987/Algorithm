import sys
import math


def is_prime(i):
    if i == 0 or i == 1:
        return False
    elif i == 2:
        return True
    else:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                return False
        return True

if __name__ == '__main__':
    inputF = sys.stdin.readline

    m, n = map(int, inputF().rstrip().split())

    for i in range(m, n + 1):
        if is_prime(i):
            print(i)
