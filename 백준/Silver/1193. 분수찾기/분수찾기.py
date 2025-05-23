# 18:04 ~

def get_line(x):
    line = 1
    while x > line:
        x -= line
        line += 1

    return line, x


x = int(input())
num = 0
cnt = 0
i,j = 0,0
line, order = get_line(x)
if line % 2 != 0:
    i = line
    j = 1
    i -= order -1
    j += order -1
else:
    i = 1
    j = line
    i += order - 1
    j -= order - 1

print(f"{i}/{j}")
