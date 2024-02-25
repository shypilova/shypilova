x = int(input('Type 4 digit number: '))
a = 100
left, right = divmod(x, a)
print(x // 1000)
print(left % 10)
print(right // 10)
print(x % 10)
