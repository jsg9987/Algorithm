import sys

def count_coin(charge):
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1
    result_str = ''
    result_str += str(charge // quarter) + ' ' + str(charge % quarter // dime) + ' ' + str(charge % quarter % dime // nickel) + ' ' +  str(charge % quarter % dime % nickel // penny)

    return result_str
if __name__ == '__main__':
    inputF = sys.stdin.readline
    t = int(inputF().rstrip())

    for i in range(t):
        charge = int(inputF().rstrip())
        print(count_coin(charge))

