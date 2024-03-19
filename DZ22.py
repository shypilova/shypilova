# def difference(some_list):
#
#     max_value = max(some_list)
#     min_value = min(some_list)
#     diff = max_value - min_value
#     if len(some_list) >= 1:
#         if diff is int:
#             return int(diff)
#         else:
#             return round(diff, 2)
#     else:
#         return diff == 0
#     print(diff)


# assert difference(1, 2, 3) == 2, "Test1"
some_list = ()
max_value = max(some_list)
min_value = min(some_list)
diff = max_value - min_value
if len(some_list) >= 1:
    if diff is int:
        int(diff)
    else:
        round(diff, 2)
else:
    diff == 0
print(diff)
print(type(some_list))