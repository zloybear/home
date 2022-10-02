class Apple:

    ripenss_stage = {0 : 'цветok',1: 'узелок',2:'зелёное',3:'спелое'}


    def __init__(self,ripenss = 0,apple_id = 0):
        self.apple_id = apple_id
        self.ripenss = ripenss

    def grow(self):
        if self.ripenss <= 2:
            self.ripenss += 1
            print(f' яблокчо {self.apple_id} теперь {self.ripenss_stage[self.ripenss]}')
        else:
            print(f' яблочко {self.apple_id} не растёт')


    def is_ripe(self):
        indicator = True
        if self.ripenss == 3:
            indicator = True
        else:
            indicator = False
            return indicator


class AppleTree:

    def __init__(self,number):
        self.apple_list = [Apple(i) for i in range(number)]


    def show_apples(self):
        for apple in self.apple_list:
            print(f'яблочко {apple.apple_id} {apple.ripenss_stage[apple.ripenss]}')


    def grow_apples(self):
        for i in range(len(self.apple_list)-1):
            self.apple_list[i].grow()