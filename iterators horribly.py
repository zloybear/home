import random
def simple(number):
    indikator = True
    for _ in range(2, number):
        if number % _ == 0:
            indikator = False
    return indikator

class InfIter:
    def __init__(self, max_number):
        self.max_number = max_number
        self.element = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.element += 1
        while not simple(self.element):
            self.element += 1
        if self.element < self.max_number:
            return self.element
        else:
            raise StopIteration


my_iter = InfIter(int(input('верхняя граница простых чисел ')))
print('елементы ☺☻')
for _ in my_iter:
    print(_)