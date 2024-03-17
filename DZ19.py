def is_palindrome(text):
    import string
    spec_chars = string.punctuation + string.whitespace
    b = [ch for ch in text.lower() if ch not in spec_chars]
    c = "".join(b)
    a = c[::-1]
    result = (a == c)
    return result

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
