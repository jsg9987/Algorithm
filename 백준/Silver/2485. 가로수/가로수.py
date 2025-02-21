import sys


def gcd(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == '__main__':
    inputF = sys.stdin.readline
    n = int(inputF().rstrip())
    arr = []
    dist_arr = []
    count = 0

    for i in range(n):
        dist = 0
        arr.append(int(inputF().rstrip()))

        if i != 0:
            dist_arr.append(arr[i] - arr[i - 1])

    gcd_value = dist_arr[0]
    for i in range(1, len(dist_arr)):
        gcd_value = gcd(gcd_value, dist_arr[i])

    for num in dist_arr:
        count += (num // gcd_value) -1

    print(count)