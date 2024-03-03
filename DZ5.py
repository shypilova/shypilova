lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lst_uneven = [1, 2, 3, 4, 5, 6, 7]
# lst_empty = []
# lst_1 = [1]

# список з парною кількістю
# x = int((len(lst_even))/2)
# new_list = [lst_even[:x], lst_even[x:]]
# print(new_list)

# список з непарною кількістю
# y = round((len(lst_uneven))/2)
# new_list2 = [lst_uneven[:y], lst_uneven[y:]]
# print(new_list2)


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
        y = int((len(lst)) / 2)
        new_list_1 = [lst[:y], lst[y:]]
        print(new_list_1)
print(y)

#     else:
#         y = round(x)
#         new_list2 = [lst[:y], lst[y:]]
#         print(new_list2)
#         print(len(lst))
#         print(type(x))
#         print(y)
