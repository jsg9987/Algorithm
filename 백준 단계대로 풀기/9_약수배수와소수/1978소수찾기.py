def check_prime_number(n, arr):
    count = 0

    for num in arr:
        if num != 1:
            for i in range(2, num):
                if num % i == 0:
                    count += 1
                    break
        elif num == 1:
            count += 1

    print(n - count)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    check_prime_number(n, arr)
