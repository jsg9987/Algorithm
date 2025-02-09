def check_num(a, b):
    result = ''

    if b % a == 0:
        result = 'factor'
    elif a % b == 0:
        result = 'multiple'
    else:
        result = 'neither'

    return result

if __name__ == '__main__':
    while 1:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        print(check_num(a, b))
