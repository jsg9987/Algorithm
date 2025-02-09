import sys

def find_num(num):
    line = 1
    a = 0
    b = 0

    while num > line:
        num -= line
        line += 1

    if line % 2 == 0:
        a = num
        b = line - num + 1
    elif line % 2 != 0:
        a = line - num + 1
        b = num

    return str(a) + '/' + str(b)

if __name__ == '__main__':
    num = int(input())
    print(find_num(num))