T = int(input())

for test_case in range(1, T+1):
    word = input().strip()
    word2 = ''.join(reversed(word))

    if word == word2:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")
