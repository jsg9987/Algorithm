import sys

def dec_to_other_base(n,b):
    num_dict = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sum_result = ''
    while (n != 0):
        sum_result += num_dict[n % b]
        n //= b # 파이썬 실수 주의

    sum_result = sum_result[::-1]
    return sum_result

if __name__ == '__main__':
    inputF = sys.stdin.readline
    n, b = map(int, inputF().rstrip().split())

    print(dec_to_other_base(n,b))



