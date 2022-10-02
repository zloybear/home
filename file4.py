import re
import pygame,sys
import write_big_text as wr

pygame.init()
# #---------------------------------------------------------
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Консоль")

class expressions:
    window = pygame.Surface(size)
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(100, 100, 130, 32)
    active = False
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')#
    aqua = (0, 255, 255)  # морская волна
    color = color_inactive

    text = 'Введите имя героя'

    def compar(self,filename,symb):
        text_out=''
        text=''
        with open(filename) as f:
            for i in range(6):
                line = f.readline().split('-')
                text_out = line[1]
                text = line[0]
                words = re.findall(r'({}[абвгдежзиклмнопрстуфхцчшщьыъэюя0123456789]+)'
                                   .format(symb), text.lower())
                if len(words): break
        return text,text_out
    def text_box(self,filename):
        text_out="Герой","описание"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Если пользователь нажал на прямоугольник input_box.
                    if self.input_box.collidepoint(event.pos):
                        #инверсия переменной.
                        self.active = not self.active
                        self.text = ''
                    else:
                        self.active = False
                    #Изменение текущего цвета поля ввода.
                    self.color = self.color_active if self.active else self.color_inactive

                if event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key == pygame.K_RETURN:
                            print(self.text)
                            text_out =self.compar(filename,self.text)
                            self.text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            self.text = self.text[:-1]
                        else:
                            self.text += event.unicode

            self.window.fill((255, 255, 255))
            # Визуализация текущего текста.
            txt_surface = self.font.render(self.text, True, self.color)
            # Размер поля.
            self.input_box.w = 230
            # Отображение текста.
            self.window.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
            information = text_out[0] + "-" + text_out[1]
            wr.insert_text(self.window, information, (20, 140), self.font)
            # Отображение прямоугольника ввода текста.
            pygame.draw.rect(self.window, self.color, self.input_box, 2)
            # Отображение консольного окна.
            screen.blit(self.window, (0, 0))
            pygame.display.update()

exp=expressions()
exp.text_box('text.txt')






