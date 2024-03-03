import random
list_default = []
for i in range(random.randint(3, 10)):
    list_default.append(random.randint(0, 10))
# print(list_default)
for i, el in enumerate(list_default):
    new_list = [list_default[0], list_default[2], list_default[-2]]
print(list_default, '==', new_list)