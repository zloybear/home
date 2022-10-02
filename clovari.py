t = int(input('кол заказов: '))
clients = {}
for i in range(t):
    order = input(f'{i+1} заказ: ').lower().split()
    if order[0] not in clients.keys():
        clients[order[0]] = {}
    if order[1] not in clients[order[0]].keys():
        clients[order[0]][order[1]] = int(order[2])
    else:
        clients[order[0]][order[1]] += int(order[2])
for i in clients.keys():
    print(i)
    for k in clients[i].keys():
        print(f'     {k}   -  {clients[i][k]}')
ask = input('ты кто ')
if ask in clients.keys():
    best = ['',0]
    for i in clients[ask].keys():
        if clients[ask][i] > best[1]:
            best[0] = i
            best[1] = clients[ask][i]
    print(f'клиенту {ask} стоит предположить пиццу {best[0]}')
