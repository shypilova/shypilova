def popular_words(text, *args):
    my_text = text.lower().split()
    my_args = list(args)
    lst = list()
    for el in args[0]:
        my_list = lst.append(el)
    result = ({b: my_text.count(b) for b in lst})
    return result


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
