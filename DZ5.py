lst_even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst_uneven = [1, 2, 3, 4, 5, 6, 7]
lst_empty = []
lst_1 = [1]

# список з парною кількістю
x = int((len(lst_even))/2)
new_list = [lst_even[:x], lst_even[x:]]
print(new_list)


# список з непарною кількістю
y = round((len(lst_uneven))/2)
new_list2 = [lst_uneven[:y], lst_uneven[y:]]
print(new_list2)

# пустий список
if len(lst_empty) == 0:
    new_list3 = [[],[]]
    print(new_list3)

# список з одним індексом
if len(lst_1) == 1:
    new_list4 = [[], []]
    print(new_list4)