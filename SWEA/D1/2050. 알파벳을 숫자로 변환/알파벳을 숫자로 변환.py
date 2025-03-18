alphabet = list(input())

for alpha in alphabet:
    print(ord(alpha) - ord('A') + 1, end=" ")