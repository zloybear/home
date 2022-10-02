import os
def copypast(file_name):
        some_file = open(file_name)
        copy_file = open('C:\\chert\\lop.txt'+os.path.basename(file_name),'a')
        copy_file.write(some_file.read())
        some_file.close()
        copy_file.close()
def copypapk(dir_name,rec = 0):
    if rec == 0:
        f = open('c:\\chert\\lop.txt')
    if os.path.isdir(dir_name):
        l = 'f:\\chert' + os.path.basename(dir_name)
        os.mkdir(l)
        for i in os.listdir(l):
            if os.path.isdir(l + i):
                copypapk(l + i)
            elif os.path.isfile(l + i) and i.endswith('.txt'):
                copypast(i)
                f = open('f:\\chert\\lop.txt','a')
                f.write(l + i)
                f.close()

copypapk('f:\\')
