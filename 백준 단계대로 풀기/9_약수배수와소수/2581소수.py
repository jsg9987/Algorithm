def check_prime_sum(m, n):
    prime_min = n
    arr = []
    for num in range(m, n + 1):
        count = 0
        for i in range(1, num):
            if num % i == 0:
                count += 1
            if count > 1:
                break
        if count == 1:
            arr.append(num)
            if num < prime_min:
                prime_min = num

    if len(arr) == 0:
        print('-1')
    else:
        print(sum(arr))
        print(prime_min)


if __name__ == '__main__':
    m = int(input())
    n = int(input())

    check_prime_sum(m, n)
