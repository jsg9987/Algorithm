# 4/23 21:02 ~ 22:08
# 올바른 암호코드: (홀수 자리의 합 *3) + (짝수 자리 합)이 10의 배수

T = int(input())
dic = dict()
dic["0001101"] = 0
dic["0011001"] = 1
dic["0010011"] = 2
dic["0111101"] = 3
dic["0100011"] = 4
dic["0110001"] = 5
dic["0101111"] = 6
dic["0111011"] = 7
dic["0110111"] = 8
dic["0001011"] = 9

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    binary_code = [input() for _ in range(n)]
    for row in range(n):
        temp = []
        decode = 0
        result = 0
        if "1" in binary_code[row]:
            last_idx = 0
            for i in range(len(binary_code[row])-1,-1,-1):
                if binary_code[row][i] == "1":
                    last_idx = i
                    break
            start_idx = last_idx - 55
            for i in range(start_idx, last_idx+1, 7):
                bit = ''.join(binary_code[row][i:i + 7])
                if "1" in bit:
                    temp.append(bit)

            if temp:
                for i in range(len(temp)):
                    if (i+1) % 2 != 0:
                        decode += dic[temp[i]] * 3
                        result += dic[temp[i]]
                    else:
                        decode += dic[temp[i]]
                        result += dic[temp[i]]

        if decode > 0:
            if decode % 10 == 0:
                print(f"#{tc} {result}")
                break
            else:
                print(f"#{tc} 0")
                break