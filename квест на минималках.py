keydoor = ''

def hallway():
    print ('выберись из хаты')
    print ('куда идём (коридор)')
    print ('1 в ванную')
    print ('2 в спальную')
    print ('3 в кухню')
    print ('4 дверь')
    player=input()
    if player == '1':
        banna()
    if player == '2':
        bedroom()
    if player == '3':
        cook()
    if player == '4':
        door()
    if player == '5':
        Keyisen()
    if player == 'key':
        print('win')
        bedroom()

def bedroom():
    print ('ты в спальне,что сделать')
    print ('1 в ванную')
    print ('2 в коридор')
    print ('3 ключ на тумбе')
    player=input()
    if player == '1':
        banna()
    if player == '2':
        hallway()
    if player == '3':
        keytrue()

def banna():
    print('куда идём (ванная)')
    print('1 в коридор')
    print('2 помытся')
    player=input()
    if player == '1':
        hallway()

def cook():
    print('куда идём (кухня)')
    print('1 в коридор')
    print('2 окно')
    print('3 пожрать')
    player = input()
    if player == '1':
        hallway()
    if player == '2':
        okno()

def okno():
    print('хреновая погода ')
    cook()

def door():
    print('дверь закрыта')
    hallway()

def Keyisen():
    print(f'{keydoor}')
    hallway()

def keytrue():
    print(f'ключ(key)')
    bedroom()


bedroom()
