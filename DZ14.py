x = int(input('Enter digit:')) # input('Enter some letter')
def digits(a):
    my_list = []
    while a != 0:
        my_list.append(a % 10)
        a = a // 10
    return my_list
def persistence(x):
    while x > 9:
        d = digits(x)
        mul = 1
        for el in d:
            mul = mul * el
        x = mul
        test = ('*'.join(map(str, d)) + '=' + str(mul))
    print(mul)
persistence(x)