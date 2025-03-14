s = list(input())

for i in range(len(s)):
    if s[i].islower():
        s[i] = s[i].upper()

print(*s, sep="")

