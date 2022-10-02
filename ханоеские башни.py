class tower:
    def __init__(self,flapjack,flap,location):
        self.flapjack = flapjack
        self.flap = flap
        self.location = location

    def

def luc(listo):
    for i in range(3):
        if len(listo[i]) == 0:
            print('-')
        else:
            for j in range(len(listo[i])):
                print(listo[i][j], end='   ')
        print()

def move(fromm,too,list1):
    print(f'перестановляю блин {list1[fromm][-1]} c {fromm} столбца на {too}')
    list1[too].append(list1[fromm].pop(-1))
    luc(list1)

list2 = []
list2.append([10 - i for i in range(3)])
list2.append([])
list2.append([])
list2.append([])
move(0, 1, list2)
move(0, 2, list2)
move(0, 3, list2)