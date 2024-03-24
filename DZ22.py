def difference(*args):
    some_list = list()
    for el in args:
        new = some_list.append(el)
    if len(some_list) == 0:
        return (0)
    if len(some_list) > 0:
        max_value = max(some_list)
        min_value = min(some_list)
        diff = max_value - min_value
        if diff is int:
            return (int(diff))
        else:
            return (round(diff, 2))

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')