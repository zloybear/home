def d (number):
    indikator= True
    for i in range(number):
        if i !=0 and i!=1 and number % i == 0 :
            indikator = False
    return indikator

number = int (input('цифорки суды'))
for i in range(number):
    if d(i):
        print(i,end=', ')
