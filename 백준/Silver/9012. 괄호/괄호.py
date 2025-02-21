import sys

if __name__ == '__main__':
    inputF = sys.stdin.readline
    t = int(inputF().rstrip())

    for _ in range(t):
        ST = []
        li = list(inputF().rstrip())
        for v in li:
            if v == "(":
                ST.append(v)

            if not ST:
                if v == ")":
                    ST.append(v)
                    
            if len(ST) != 0:
                if ST[-1] == "(" and v == ")":
                    ST.pop(-1)

        if ST:
            print("NO")
        else:
            print("YES")