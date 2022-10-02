import os
def script1():

    file = os.path.abspath('F:\scraep')
    print(chek(file))
    print(file)
def chek(chekae, count = 0):
    print(os.listdir(chekae))
    for i in os.listdir(chekae):
        if '.' in i:
            if i.endswith('.txt'):
                count += 1
        else:
            chek(chekae+'\\'+i)
            count += 1
    return count

script1()
