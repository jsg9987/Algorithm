
if __name__ == '__main__':

    while True:
        s = input()
        ST = []

        if s == ".":
            break
        for v in s:
            if v == "(":
                ST.append(v)
            elif v == "[":
                ST.append(v)

            elif v == ")":
                if ST and ST[-1] == "(":
                    ST.pop(-1)
                else:
                    ST.append(v)
                    break
            elif v == "]":
                if ST and ST[-1] == "[":
                    ST.pop(-1)
                else:
                    ST.append(v)
                    break
        if ST:
            print("no")
        else:
            print("yes")