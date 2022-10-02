class handler:
    text=''
    def read(self,file):
        with open(file,'a')as f1:
            write('прекрасно!')
            self.text=f1.read()

        return self.text
dyachek=handler()
print(dyachek.read(r'E:\sraep\text1.txt'))