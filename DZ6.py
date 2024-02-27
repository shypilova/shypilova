empty_list = []
list = [12, 3, 4, 10]
list2 = [12, 3, 4, 10, 8]
list3 = [1]

if len(empty_list) == 0:
    print(empty_list)

if len(list) > 0:
    a = list.pop(-1)
    new_list = list.insert(0, a)
    print(list)

if len(list2) > 0:
    b = list2.pop(-1)
    new_list2 = list2.insert(0, b)
    print(list2)

if len(list3) > 0:
    c = list3.pop(-1)
    new_list3 = list3.insert(0, c)
    print(list3)