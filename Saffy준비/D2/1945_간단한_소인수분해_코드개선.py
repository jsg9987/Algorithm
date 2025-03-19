T = int(input())

for test_case in range(1, T+1):
    n = int(input())

    divisor = [2,3,5,7,11]
    abcde = [0,0,0,0,0]

    for i in range(len(abcde)):
        while n % divisor[i] == 0:
            n //= divisor[i]
            abcde[i] += 1

    print(f"#{test_case}", *abcde)

