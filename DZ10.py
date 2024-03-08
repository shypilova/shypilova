import string
import keyword
my_string = input('Enter string :')
spec_char = """!"#$%&'()*+,-./:;<» «=>?@[]^`{|}~"""
for l in my_string:
    if l in spec_char:
        print('False')
        break
    if my_string[0].isdigit() or my_string.isdigit() or l.istitle():
        print('False')
        break
else:
    print('True')