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

# 더 좋은 방법 -> 가로 세로 변의 점은 2^n + 1씩 증가한다. 점 2개 사이에 점이 하나씩 생기므로 (2*(변의 점 개수 - 1)) + 1)^2 or (2^n + 1) ^2 -> 결국 원래 점에서 2배씩 불어나는 형태이므로 뒤의 식이 좀더 깔끔해보임.