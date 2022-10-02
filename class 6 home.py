class Home:
    def __init__(self):
        super().__init__()
        self.money = 100
        self.dert = 0
        self.feed = 50
        self.feed_cat = 30

    def game(self,dert,fun):
        dert + 10
        if dert > 90:
            fun - 10
        print(f'{+1}')
        Valera('game')


class Valera:
    def __init__(self,fun = 100,food = 30):
        self.fun = fun
        self.food = food
        print(f'{self.fun},{self.food}')

    def game(self):
        if input == 'eat':
            eat()
        if input == 'play':
            play()
        if input == 'job':
            job()
        if input == 'cat':
            cat_fun()

    def eat(self):
        self.food + 30
        self.feed - 10

    def play(self):
        self.fun + 20
        self.food - 10

    def job(self):
        self.money + 150
        self.food - 10
        self.fun - 10

    def cat_fun(self):
        self.fun + 5
        self.food - 10


class Eva:
    def __init__(self, fun=100, food=30):
        self.fun = fun
        self.food = food

    def eat(self):
        self.food + 30
        self.feed - 10

    def produkt(self):
        self.feed + 10
        self.money - 10
        self.food - 10

    def produkt(self):
        self.feed_cat + 10
        self.money - 10
        self.food - 10

    def wiba(self):
        self.fun + 60
        self.money - 350
        self.food - 10

    def uborka(self):
        self.dert - 50
        self.food - 10

    def cat_fun(self):
        self.fun + 5
        self.food - 10


class Mur:
    def __init__(self,food = 30):
        self.food = food

    def eat(self):
        self.food + 30
        self.feed_cat - 10

    def slep(self):
        self.food - 10

    def aligi(self):
        self.dert + 5
        self.food - 10

l1=Home
man=Valera
Home.game(input(''))