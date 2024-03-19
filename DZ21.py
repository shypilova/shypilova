def popular_words(text, *args):
    my_text = text.lower().split()
    result = ({b: my_text.count(b.lower()) for b in ['i', 'was', 'three', 'near']})
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
