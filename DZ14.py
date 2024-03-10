x = '999' #input('Enter some letter')
y = tuple(x)
mult = 1
for el in y:
    mult *= int(el)

print(mult)
print(y)
print(type(y))
print(type(y[0]))



# string = "это пример строки....wow!!!"
# a = string.zfill(30)
# print ("str.zfill : ", a)
# import string
# print(string.ascii_lowercase)
# print(string.ascii_letters)