import  os
def filo (file1):
    l = 0
    file_object = open(file1, 'r')
    for i in file_object:
        for j in i.split():
            l += int(j)
    file_object.close()
    return l
def proch (file1):
    simbols = {}
    simbols_count = 0
    file_object = open(file1)
    for i in file_object:
        print(i)
        for k in i:
            if k in simbols.keys():
                simbols[k] += 1
            elif k not in simbols.keys() and k.isalpha():
                simbols[k] = 1
            simbols_count += 1
    file_object.close()
    logs = open('logs.txt', 'w')
    for i, k in simbols.items():
        t = f'{i} - {k*100/simbols_count} % \n'
        print(t)
        logs.write(t)
    logs.close()

proch('f:\\scraep\\text.txt')