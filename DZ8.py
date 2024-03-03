list_dz8 = [0, 1, 7, 2, 4, 8]
new_list = list_dz8[::2]
if list_dz8:
    a = (sum(new_list)) * list_dz8[- 1]
    print(a)
else:
    a = (sum(new_list)) * 0
    print(a)