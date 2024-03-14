list_1 = (0, 2, 3, 5, 6, 9, 15, 30)
list_2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 30)

def common_elements(first_list, second_list):
    set_a = set(first_list)
    set_b = set(second_list)
    list_new_1 = list()
    list_new_2 = list()
    for el in first_list:
        if (el % 3) == 0:
            list_new_1.append(el)
        else:
            continue
    for el in second_list:
        if (el % 5) == 0:
            list_new_2.append(el)
        else:
            continue
    set_a = set(list_new_1)
    set_b = set(list_new_2)
    diff_set = set_a.intersection(set_b)
    return diff_set

assert common_elements(list_1,list_2) == {15, 30}
print('OK')