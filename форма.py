import re
from re import*
text = 'форма 12,параграф 123'
class expressions:
    def scan (self,text):
        return re.findall('[0-9]+',text)
exp=expressions()
print (exp.scan(text))