number = int(input('надо цифорку'))

for i in range(number):
    for j in range (number -1,-1,-1):
        if j+1 < number -i :
            print('.', end='')
        else:
            print(j+1, end='')
    for j in range (number):
        if j < number -i-1:
            print('.', end='')
        else:
            print(j+1, end='')
    print()

