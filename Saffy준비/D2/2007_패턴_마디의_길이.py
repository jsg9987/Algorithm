T = int(input())

for test_case in range(1, T + 1):
    word_len = 1
    word = list(input())

    while word_len <= 10:
        result = 1
        for i in range(0, len(word), word_len):
            if word[:word_len] != word[i:i + word_len] and len(word[:word_len]) == len(word[i:i + word_len]):
                word_len += 1
                result = 0
                break

        if result == 1:
            break

    print(f"#{test_case} {word_len}")
