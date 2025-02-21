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
    a, b = map(int, inputF().rstrip().split())
    a2, b2 = map(int, inputF().rstrip().split())
    
    a3 = a*b2 + a2 * b
    b3 = b * b2
    gcd_value = gcd(a3, b3)
    print(a3 // gcd_value, b3 // gcd_value)