t = int(input('кол стран: '))
geo ={}
for i in range(t):
    c = input(f'{i+1}'
              f' страна: ').split()
    geo[c[0]] = c[1:]
for i in range(3):
    city = input(f'{i+1} город: ')
    count = 0
    for k in geo.keys():
        if city in geo[k]:
            print(f'город {city}'
                  f'расположен в стране {k}')
            break
        else:
            count +=1
    if count == len(geo):
        print(f'по городу {city} данных нет.')