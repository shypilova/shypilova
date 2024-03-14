def say_hi(name, age):
    my_name = 'Hi. My name is ' + name
    my_age = my_name + " and I'm "
    my_string = my_age + str(age) + ' years old'
    return my_string

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
assert say_hi("Maryna", 31) == "Hi. My name is Maryna and I'm 31 years old", 'Test3'
print('ОК')
