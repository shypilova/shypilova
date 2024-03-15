list_1 = []
list_2 = []
def common_elements(first_list, second_list):
    first_list = []
    second_list = []
    for i in range(0, 31, 3):
        first_list.append(i)
    for i in range(0, 31, 5):
        second_list.append(i)
    set_a = set(first_list)
    set_b = set(second_list)
    diff_set = set_a.intersection(set_b)
    return diff_set
print(common_elements( list_1, list_2))
