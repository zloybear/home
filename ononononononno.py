text1 = True
while text1:
    text = input('види пороль: ')
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    if len(text) >= 8 and not text.islower() and count >= 3:
        text1 = False
        print('хорошо')
    else:
        print('хрень переписывай')








