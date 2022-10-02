import pygame
from pygame import *
import write_big_text
class expre
    window = pygame.Surface (size)
    font = pygame.font.Font (ComicsansMS,16)
    input_box = pygame.Rect (100,100,130,32)
    active = False
    color_inactive = pygame.Color ('gray')
    color_active = pygame.Color ('navy')
    navy = (0,255,255)
    color = color_inactive
while True:
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if self.input_box.Collidepoint(event.pos):
                self.active = True
                self.text = ''
        else:
            self.active = False
            self.color = self,color_active
        if not self_active: self.color=color_active
        else: self.color_inactive
        if event.type == KEYDOWN:
            if self.active:
                if event.key == K_ENTER:
                print(self.text)
                self.text = ''
            elif event.key == K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text +=event.unicode:
insert_text  (window,text,(100,100),navy)
