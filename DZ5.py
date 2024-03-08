lst = [1, 2, 3, 4, 5, 6]
if len(lst) == 0:
    new_list3 = [lst[:], lst[:]]
    print(new_list3)
if len(lst) == 1:  # cписок з одним індексом
    new_list4 = [lst[:], lst[1:]]
    print(new_list4)
if len(lst) > 1:
    if len(lst) % 2 == 0:
        x = int((len(lst)) / 2)
        new_list = [lst[:x], lst[x:]]
        print(new_list)
    else:
        y = int((len(lst)) // 2 + 1)
        new_list_1 = [lst[:y], lst[y:]]
        print(new_list_1)