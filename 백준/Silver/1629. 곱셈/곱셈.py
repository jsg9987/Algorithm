# 5/14 16:46 ~
import sys

inputF = sys.stdin.readline
a, b, c = map(int, inputF().split())
print(pow(a,b,mod=c))