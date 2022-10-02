class handler:
    text=''
    def read(self,file):
        with open(file)as f1:
            self.text=f1.read()
        return self.text
    def write(self,file,imputtext):
        with open(file,'a') as f1:
            f1.write(imputtext)
        return self.text
dyachek=handler()
print(dyachek.read(r'E:\sraep\text1.txt'))
dyachek.write(r'E:\sraep\text1.txt',' c')
print(dyachek.read(r'E:\sraep\text1.txt'))
