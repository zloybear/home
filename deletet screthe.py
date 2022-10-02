def chek(che='F:'):
    import os

    for i in os.listdir(che):
        k = che + '\\' + i
        
        if os.path.isfile(k):
            if i.lower().endswith('.txt'):
                os.remove(k)
        elif os.path.isdir(k):
            chek(k)


chek()