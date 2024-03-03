
# a = list_default.pop(0)
# list_1 = list_default
# print(list_1)
# b = list_default.pop(0)
# c = list_default.pop(-2)
# d = int(len(list_default))
# print(list_default(range(0, d, 2)))
#
# len((list_default)-1)
# while i < len(list_default)
#     for el in list_default
#         i += 1
#
#
# new_list = list_dz8[0:2:2]
import random
list_default = []
for i in range(random.randint(3, 10)):
    list_default.append(random.randint(0, 10))
print(list_default)
for i in list_default:
c = list_default.pop(-2)
b = list_default.pop(2)
a = list_default.pop(0)
new_list = [a, b, c]
print(new_list)