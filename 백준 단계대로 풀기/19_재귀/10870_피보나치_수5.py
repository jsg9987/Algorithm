def fibo(n):
    f0 = 0
    f1 = 1
    if n == 0:
        return f0
    if n == 1:
        return f1
    return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))
