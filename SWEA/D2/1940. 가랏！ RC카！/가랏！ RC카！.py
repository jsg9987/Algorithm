T = int(input())

for tc in range(1, T+1):
    n = int(input())
    move = 0
    accelerate = 0

    for i in range(n):
        command = list(map(int, input().split()))
        if command[0] == 0:
            move += accelerate
        elif command[0] == 1:
            accelerate += command[1]
            move += accelerate
        elif command[0] == 2:
            if accelerate <= command[1]:
                accelerate = 0
            else:
                accelerate -= command[1]
                move += accelerate
    
    print(f"#{tc} {move}")

