import string
new_string = input("enter the string: ")       # Should, I. subscribe? Yes!
spec_chars = string.punctuation + string.whitespace                # string.whitespace
string_1 = [ch for ch in new_string.title() if ch not in spec_chars]
string_2 = "".join(string_1)
end_string = '#' + string_2
print(end_string)
if len(end_string) <= 140:
    print(end_string)
else:
    string_5 = end_string[:140]
    print(string_5)
