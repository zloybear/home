text = input('види ip: ')
text = text.split('.')
k = 0
if len(text) != 4:
    print('хрень')
else:
    for i in text:
        if not i.isdigit():
            print(f'{i} не челое число')
            break
        elif int(i) > 255 :
            print(f'{i}больше 255')
            break
        k += 1
if k == 4:
    print('хорошо')