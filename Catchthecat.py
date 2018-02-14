import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Catch the Cat')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
winImg = pygame.image.load('img_you_win.png')
failImg = pygame.image.load('tryagain.jpg')
catx = 10
caty = 100
direction = 'right'
decider = 1

while decider == 1: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            catx = 10
    

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            nowx, nowy = pygame.mouse.get_pos()
            if nowx > catx-21 and nowx < catx+21:
                decider = 0
                break
            else:
                decider = 2
                #sys.exit()
            

    pygame.display.update()
    fpsClock.tick(FPS)


while decider == 0:
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('You caught the cat')
    DISPLAYSURF.blit(winImg, (catx, caty))

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    
while decider == 2:
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption('Better luck next time')
    DISPLAYSURF.blit(failImg, (catx, caty))

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
    pygame.display.update()
