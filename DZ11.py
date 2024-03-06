x = int(input('Please enter first number:'))
y = int(input('Please enter second number:'))
z = input('Please enter action:')

if z == '*':
    print(int(x * y))
elif z == '+':
    print(int(x + y))
elif z == '-':
    print(int(x - y))

if z == '/':
    if y == 0:
        print('You can not divide by 0')
    else:
        print(int(x / y))

while input("Do you want to perform another calculation? 'y' or 'n':") == 'y':
    x = int(input('Please enter first number:'))
    y = int(input('Please enter second number:'))
    z = input('Please enter action:')
    if z == '*':
        print(int(x * y))
    elif z == '+':
        print(int(x + y))
    elif z == '-':
        print(int(x - y))
    if input("Do you want to perform another calculation? 'y' or 'n':") == 'n':
        break
