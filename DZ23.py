def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    lst = []
    lst.append(begin)
    yield begin
    for i in range(end-1):
        begin = pow(begin)
        lst.append(begin)
        yield begin


from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')