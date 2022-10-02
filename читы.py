max_number = int(input('максимальное значение '))
p1 = ()
p2 = ()
good = {0}
bad = {0}
while True:
    p1 = input('среди этих чисел есть верное!!! ')
    if p1 != 'h':
        p2 = input('y/n ')
        if p2 == 'y':
            good = good | set(p1.split())
        else:
            bad = bad | set(p1.split())
    else:
        print()
        for i in good - bad:
            if i <= max_number:
                print(i, end=', ')