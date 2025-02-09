import math


def snail_up(a, b, v):
    return math.ceil((v-a) / (a-b)) + 1


if __name__ == '__main__':
    a, b, v = map(int, input().split())

    print(snail_up(a, b, v))
