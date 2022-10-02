import re
from re import*
class expressions:
    words = 'боярышник'
    def compar (self,text):
        return  re.findall(r'({}[йцукенгшщзхъфывапролджэячсмитьбю]+)'.format(text),self.words)
exp=expressions()
print (exp.compar(words))
