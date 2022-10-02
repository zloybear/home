class handler:
    text=''
    def read(self,file):
        with open(file)as f1:
            self.text=f1.read()
        return self.text
dyachek=handler()
dyachek.read(r'f:\sraep\text1.txt') 
print(dyachek.text)
