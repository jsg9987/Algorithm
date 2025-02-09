import time

def print_fracs(n):
    if n == 1:
        None
    else:
        div = 2
        while n != 1:
            if n % div == 0:
                print(div)
                n /= div
            else:
                div += 1


if __name__ == '__main__':
    n = int(input())
    print_fracs(n)
