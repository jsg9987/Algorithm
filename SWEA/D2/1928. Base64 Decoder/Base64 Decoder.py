T = int(input())

for test_case in range(1, T+1):
    base64_table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
    encoded_string = list(input())
    binary = ""
    answer = ""

    for i in encoded_string:
        binary += format(base64_table.index(i), '06b') # 6글자로 표현해야함.

    for k in range(0, len(binary), 8):
        answer += chr(int(binary[k:k+8], 2))

    print(f"#{test_case} {answer}")
