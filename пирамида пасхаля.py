number = int(input('надо цифорку'))
k = 1
for i in range(number):
    for j in range (number -i):
        print ('  ', end= '')
    for j in range (i+1):
        if k < 10:
            print(k, end= '   ')
        else:
            print(k, end='  ')
        k+=2
    print()










    print()
