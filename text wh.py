text = input('название ресторана: ')
if text[0] in '!@#$%^&*()_':
    print('ошибка')
elif not (text.endswith('.txt') or text.endswith('.docx')):
    print('ошибка')
else:
    print('норм имя')
