list_1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
if 0 in list_1:
    for i, el in enumerate(list_1):
        if el == 0:
            list_1.remove(el)
            list_1.append(0)
else:
    print('no 0 in list')
print(list_1)