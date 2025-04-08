import sys

def recursion(s, l, r):\

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        global cnt
        cnt += 1
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


inputF = sys.stdin.readline
T = int(inputF())

for i in range(T):
    cnt = 1
    s = inputF().rstrip()
    print(isPalindrome(s), cnt)
