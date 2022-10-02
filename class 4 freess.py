class Superlist(list):
    def __init__(self):
        super().__init__()
        import random
        for i in range (10):
            self.append(random.randint(1,100))
l1 = Superlist()
print(l1)