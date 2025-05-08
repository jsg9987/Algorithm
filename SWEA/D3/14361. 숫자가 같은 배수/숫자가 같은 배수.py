# 5/8 22:30 ~
T = int(input())


def dfs(n, result):
    if len(result) == len(n):
        n_value = int(''.join(n))
        result_value = int(''.join(result))
        if n_value != result_value and result_value % n_value == 0:
            return True

    for i in range(len(n)):
        if len(result) == 0:
            if n[i] == 0:
                continue
            else:
                if not visited[i]:
                    visited[i] = 1
                    result.append(n[i])
                    if dfs(n, result):
                        return True
                    result.pop()
                    visited[i] = 0
        else:
            if not visited[i]:
                visited[i] = 1
                result.append(n[i])
                if dfs(n, result):
                    return True
                result.pop()
                visited[i] = 0


for tc in range(1, T + 1):
    n = list(input())
    visited = [0] * len(n)
    if dfs(n,[]):
        print(f"#{tc} possible")
    else:
        print(f"#{tc} impossible")

