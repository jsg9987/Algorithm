import sys

def gcd(a,b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == '__main__':
    inputF = sys.stdin.readline
    a,b = map(int, inputF().rstrip().split())
    gcd_value = gcd(a,b)

    print(a * b // gcd_value)
