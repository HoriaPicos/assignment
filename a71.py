import pygame
import sys
import os
import math
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
    def __init__(self, speed, toggle):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = speed
        self.toggle = toggle

        if not self.toggle:
            self.image, self.rect = load_pic('bacon.png')
        else:
            self.image, self.rect = load_pic('bacon.png')
               
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.velocity = [0, 0];
        self.speed = speed
        self.toggle = toggle

    def update(self):
        if not self.toggle:
            target = pygame.mouse.get_pos()
        else:
            target = self.toggle.topleft
        #print "mous: "
        #print target
        
        v = target[0] - self.rect.topleft[0], target[1] - self.rect.topleft[1]
        norm = math.sqrt(v[0]**2 + v[1]**2) * self.speed

        if not ((int(v[0]) >= -5 and int(v[0]) <= 5 and int(v[1]) >= -5 and int(v[1]) <= 5)):
            unit_vec = 10 * v[0] / norm, 10 * v[1] / norm
            self.velocity = (((self.velocity[0] *.9) + unit_vec[0]), ((self.velocity[1] *.9) + unit_vec[1]))

            self.rect.topleft = self.rect.topleft[0] + self.velocity[0], self.rect.topleft[1]+ self.velocity[1]
        
        #print "rect: "
        #print self.rect.topleft
    
        
#Bacon MOvement
def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption('Bacon Runner')
    pygame.mouse.set_visible(1)
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(white)
    
    screen.blit(background, (0, 0))
    pygame.display.flip()
    clock = pygame.time.Clock()
    bacon = Bacon(5, False)
    bacon2 = Bacon(10, bacon.rect)
    allsprites = pygame.sprite.Group(bacon, bacon2)
    
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
