import sys

inputF = sys.stdin.readline

s = inputF().rstrip()
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
length = len(s)

for i in arr:
    if i in s:
        if s.count(i)>1:
            for j in range(s.count(i)):
                length= length-len(i) +1
        elif i =='dz=':
            length= length-len(i) +2
        else:
            length= length-len(i) +1

print(length)
