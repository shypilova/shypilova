import string
new = input('Enter some letter, e.g. a-c:')
lst = list(new)
x = string.ascii_letters.index(lst[0])
y = string.ascii_letters.index(lst[-1])
new = string.ascii_letters[x:y+1]
print(new)