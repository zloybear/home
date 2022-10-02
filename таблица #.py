number = int(input('надо цифорку'))
for i in range(number):
    for j in range (number -i):
        print (' ', end= ' ')
    for j in range (i*2+1):
        print('#', end=' ')
    print()

