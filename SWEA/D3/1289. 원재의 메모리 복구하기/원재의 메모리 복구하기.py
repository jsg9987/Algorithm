# 4/24 18:28 ~
# 원래 비트가 1일 때만 바꾼다.

T = int(input())

for tc in range(1, T+1):
    memory = list(map(int, input()))
    new = [0] * len(memory)
    result = 0
    for i in range(len(memory)):
        if memory[i] == new[i]:
            continue
        elif memory[i] != new[i]:
            for j in range(i,len(new)):
                new[j] = memory[i]
            result += 1
    print(f"#{tc} {result}")