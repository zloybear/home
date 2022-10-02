class handler:
    text = ''
    def read (self,file):
        with open(file,'r') as f:
            self.text = f.read()
        return self.text
text=handler()
print (text.read(r'E:\scraep\text.txt'))