import sys
import math

def dot_count_loop(n):
    dot_count = 4
    for i in range(1, n+1):
        dot_count = dot_count + 4 * pow(4, i-1) - 2 * (math.sqrt(pow(4,i-1)) * (math.sqrt(pow(4,i-1)) -1)) + pow(4, i-1)

    return int(dot_count)

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    print(dot_count_loop(n))