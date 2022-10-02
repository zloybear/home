class Warrior:

    def __init__(self,HP = 100,armor = 10):
        self.hp = HP
        self.arm = armor

    def blow(self,damage):
        if self.hp - damage >0:
            self.hp -= damage - self.arm
        else:
            self.hp = 0
        print(f'{self.hp}HP')

    def he_alive(self):
        if self.hp != 0:
            return True
        else:
            return False



class Game:
#game_classes = [Warrior]

    def __init__(self):
        self.player_list = [Warrior()for i in range(2)]

    def fight(self):
        import random
        fiter = 0
        print('fight!!! начинается')
        while self.player_list[0].he_alive() and self.player_list[1].he_alive():
            fiter = random.choice([0,1])
            print(f'player {fiter} получил 10 ур')
            self.player_list[fiter].blow(20)
        print(f'player {fiter} lox ')



game1 = Game()
game1.fight()