import string
import keyword
print(keyword.kwlist)
new_string = 'I 232l4ike^%$^ Python'        # input("enter the string: ")
lst = list(new_string)
spec_chars = string.punctuation + '\n\xa0«»\t—…'
spec_chars_list = list(spec_chars)
print(new_string)
print(spec_chars_list)
def remove_chars_from_text(lst, spec_chars):
    return "".join([ch for ch in lst if ch not in spec_chars])
text = remove_chars_from_text(lst, spec_chars)
print(text)

# for el in lst:
#     if el in lst == spec_chars:
#         lst.remove(el)
#         print(lst)

#         string.join(lst)

# spec_chars = string.punctuation + '\n\xa0«»\t—…'
# for ch in my_string:
#     if not ch == spec_chars:
#         string.join(my_string)
#     print(my_string)
#
# text = my_string.join([ch for ch in my_string if ch not in spec_chars])
# text = remove_chars_from_text(text, spec_chars)
# print(text)
# my_string_1 = my_string
# remove_punctuation(my_string)
#
#     return ''.join(c для c в тексте, если c нет в string.punctuation)
# string_hashtag = '#' + enter_string
# my_string = string_hashtag.title()
