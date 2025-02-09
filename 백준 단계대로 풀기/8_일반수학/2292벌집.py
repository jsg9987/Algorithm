import sys

def min_across(n):
    count = 0
    sub = 6
    while (n > 0):
        if count == 0:
            n -= 1
            count += 1
        else:
            n -= sub
            sub += 6
            count += 1
    return count

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    print(min_across(n))
