tupl1 = {}
while True:
    t1 = input('1-запiсать, 2-найтi: ')
    if t1 == '1':
        name = input('имя: ')
        fame = input('фамiлiя: ')
        nome = input('номер: ')
        tupl1[(name, fame)] = nome
        print(tupl1)
    elif t1 == '2':
        nome_adress = input('ФАМIЛУЮ!!!!: ')
        count = 0
        for (i, l), k in tupl1.items():
            if l == nome_adress:
                print(f'челу {i} {l} прiнадлiжiт  {k}')
            else:
                count += 1
        if count == len(tupl1):
            print('абонент не доступн')
    else:
        print('I dont`s anderstent')