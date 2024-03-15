def correct_sentence(string):
    lst = list(string)
    lst[0] = lst[0].title()
    if lst[-1] != '.':
        lst[-1] = lst[-1] + '.'
    new_string = ("".join(lst))
    return new_string

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')