from __future__ import division
import math
import sys
import pygame

class MyGame(object):
  def __init__(self):
    """Initialize a new game"""
    pygame.mixer.init()
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    white = (255,255,255)
    self.width = 800
    self.height = 600
    self.screen = pygame.display.set_mode((self.width, self.height))
    self.image = pygame.image.load('bacon.png')
    rect = self.image.get_rect()
    self.position = [rect.width//2, rect.height//2]
    self.speed_x = 5
    self.speed_y = 5

    self.bg_color = white

    self.FPS = 30
    self.REFRESH = pygame.USEREVENT+1
    pygame.time.set_timer(self.REFRESH, 1000//self.FPS)

  def run(self):
    """Loop forever processing events"""
    running = True
    while running:

        event = pygame.event.wait()

    if event.type == pygame.QUIT:
      running = False

    elif event.type == self.REFRESH:
      (self.pos_x, self.pos_y) = pygame.mouse.get_pos()
      self.draw()

    else:
      pass 
  def chase(self):
    v = [None, None]
    v[0] = self.pos_x - self.position[0]
    v[1] = self.pos_y - self.position[1]
    norm = (v[0]**2 + v[1]**2)**(1/2)
    self.speed_x = v[0] / norm * 0.9 + self.speed_x
    self.speed_y = v[1] / norm * 0.9 + self.speed_y
    self.position[0] += self.speed_x
    self.position[1] += self.speed_y

  def draw(self):
    self.screen.fill(self.bg_color)
    rect = self.image.get_rect()
    self.chase()
    rect = rect.move(self.position[0], self.position[1])
    self.screen.blit(self.image, rect)

    pygame.display.flip()

MyGame().run()
pygame.quit()
sys.exit()