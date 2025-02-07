def check_perfect_number(num):
    div = 1
    div_sum = 0
    result = []
    while num > div:
        if num % div == 0:
            div_sum += div
            result.append(div)
        div += 1

    if num == div_sum:
        num_str = ''
        for i in range(len(result)):
            if i != len(result)-1:
                num_str += str(result[i]) + ' + '
            elif i == len(result)-1:
                num_str += str(result[i])

        return str(num) + ' = ' + num_str
    elif num != div_sum:
      return str(num) + ' is NOT perfect.'

if __name__ == '__main__':
    while 1:
        num = int(input())
        if num == -1:
            break
        print(check_perfect_number(num))

