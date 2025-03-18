r_c_p = {1:3, 2:1, 3:2}
a,b = map(int, input().split())
winner = None

if r_c_p[a] == b:
    winner = "A"
else:
    winner = "B"

print(winner)