class Citizen:
    __city = 'Олег'
    def __init__(self,name):
        self.name = name

    def get_city(self):
        return self.__city

    def set_city(self,new_city):
        self.__city = new_city

    def __salt(self):
        print(f'{self.name} умеет делаеть соль')

    def loxotron(self):
        self.__salt()
        print(f'{self.name} делает соль')

    def relax(self):
        print(f'{self.name} нюхает соль')

class Worker(Citizen):

    def __init__(self,name,work):
        super().__init__(name)
        self.work = work

    def stonks(self):
        print(f'{self.name} повысели просто повысили не чё токова')

    def relax(self):
        print(f'{self.name} садится на соль')


Vasya = Citizen('Vasya')
Vasya.set_city('Oлегастан')
Kolya = Worker(work='dns',name='Kolya')
print(Kolya.get_city())
print(Kolya.work)
Kolya.relax()
Vasya.relax()