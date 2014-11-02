import pygame
import sys
import os
from pygame.locals import *
 
pygame.mixer.init()
white = (255,255,255)
 
'''Used to load resources'''

#image
def load_pic(name):
    nameload = os.path.join('pics', name)
    try:
        image = pygame.image.load(nameload)
    except pygame.error, message:
        print 'Cannot load image:', nameload
        raise SystemExit, message
    image = image.convert()
    return image, image.get_rect()
    
#sounds
def load_sounds(name):
    class NoneSound:
       def play(self): pass
    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    nameload = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(nameload)
    except pygame.error, message:
        print 'Cannot load sound:', nameload
        raise SystemExit, message
    return sound
    
class Bacon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_pic('bacon.png')
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
    
    
#Bacon MOvement
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Bacon Runner')
    pygame.mouse.set_visible(0)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(white)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    bacon = Bacon()
    allsprites = pygame.sprite.RenderPlain((bacon))
    
    #MAIN LOOP
    while 1:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        allsprites.update()
        
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

main()