n = int(input())
f = [0 for _ in range(n + 1)]
cnt1 = 0
cnt2 = 0

def fib(n):
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a+b

    return b


def fibonacci(n):
    global f, cnt2

    f[1] = 1
    f[2] = 2
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(n)
fibonacci(n)
print(fib(n), cnt2)
