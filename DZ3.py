x = int(input('Type 5 digit number: '))
left, right = divmod(x, 1000)
# print('Inverse number:', right % 10, (right % 100) // 10, right // 100, left % 10, left // 10)
a = right % 10
b = (right % 100) // 10
c = right // 100
d = left % 10
e = left // 10
new = a * 10000 + b * 1000 + c * 100 + d * 10 + e * 1
print('Inverse number:', new)
