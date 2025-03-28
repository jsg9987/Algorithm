import sys

inputF = sys.stdin.readline
n = int(inputF().rstrip())
names = set()
cnt = 0

for i in range(n):
    input_data = inputF().rstrip()

    if input_data == 'ENTER':
        names = set() # names.clear()도 가능
    else:
        if input_data in names:
            None
        else:
            names.add(input_data)
            cnt += 1

print(cnt)