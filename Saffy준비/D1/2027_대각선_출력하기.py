li = list("+++++")

for i in range(5):
    li[i] = '#'
    print(*li, sep="")
    li = list("+++++")