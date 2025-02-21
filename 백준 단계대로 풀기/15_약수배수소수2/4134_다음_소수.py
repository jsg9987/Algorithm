import sys
import math

# 에라토스테네스의 체
def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    inputF = sys.stdin.readline

    t = int(inputF().rstrip())
    for i in range(t):
        n = int(inputF().rstrip())
        while True:
            if prime(n):
                print(n)
                break
            else:
                n += 1