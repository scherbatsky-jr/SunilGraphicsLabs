import pygame
import time
import random
from tkinter import *
from tkinter import messagebox

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("Snake Impact")
done = False
clock = pygame.time.Clock()
black =(0,0,0)
white = (255,255,255)
ground = (0,150,0)
red = (255,0,0)
green = (0,255,0)
back = (100,99,98)
first = True
score = 0
check = 0
fonttype = pygame.font.SysFont('Comic Sans MS',30)
scoretext = fonttype.render("SCORE",False,red)
scoreboard = fonttype.render(str(score),False,red)
picture = pygame.image.load('pgame.png')
#init
headX = 250
headY = 250
direction = "RIGHT"
ntail  = 30
tailX = [0]*1000
tailY = [0]*1000
fruitX = random.randint(20,580)
fruitY = random.randint(20,530)


def checkCollision():
    #wall Collision
    global ntail,fruitX,fruitY,first,score,check
    if headX <=20 or headX >=595 or headY <=20 or headY >=545:
        Tk().wm_withdraw()
        m = messagebox.showinfo("Snake Impact","Your score is "+str(score))
        if m == "ok":
            pygame.display.quit()
            pygame.quit()


    if first== False:
        for i in range(2,ntail):
            if abs(headX-tailX[i]) < 3 and abs(headY-tailY[i])<3:
                Tk().wm_withdraw()
                m = messagebox.showinfo("Snake Impact","Your score is "+str(score))
                if m == "ok":
                    pygame.display.quit()
                    pygame.quit()
    first = False

    if abs(headX-fruitX) < 20 and abs(headY-fruitY)<20:
        ntail+=13
        score+=5
        fruitX = random.randint(20,580)
        fruitY = random.randint(20,530)


def logic():
    checkCollision()

    global headX, headY, direction
    if direction == "RIGHT":
        headX += 3
    elif direction == "LEFT":
        headX -= 3
    elif direction == "UP":
        headY -=3
    elif direction == "DOWN":
        headY += 3


def drawStuff():
    global headX,headY,scoreboard
    screen.fill(white)
    scoreboard = fonttype.render(str(score),False,red)
    pygame.draw.polygon(screen,black,((9,9),(601,9),(601,551),(9,551)),1)
    pygame.draw.polygon(screen,ground,((10,10),(600,10),(600,550),(10,550)),0)
    pygame.draw.polygon(screen,black,((650,10),(850,10),(850,200),(650,200)),1)
    screen.blit(picture,(700,600))
    pygame.draw.circle(screen,red,(fruitX,fruitY),10)
    screen.blit(scoretext,(700,50))
    screen.blit(scoreboard,(700,100))
    pygame.draw.circle(screen,green,(headX,headY),10)
    for i in range(ntail):
        pygame.draw.circle(screen,green,(tailX[i],tailY[i]),10)

while not done:
    drawStuff()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction == "UP" or direction == "DOWN":
                    direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if direction == "UP" or direction == "DOWN":
                    direction = "RIGHT"
            elif event.key == pygame.K_UP:
                if direction == "LEFT" or direction == "RIGHT":
                    direction = "UP"
            elif event.key == pygame.K_DOWN:
                if direction == "LEFT" or direction == "RIGHT":
                    direction = "DOWN"

    prevX = tailX[0]
    prevY = tailY[0]
    tailX[0] = headX
    tailY[0] = headY
    for i in range(ntail):
        prev2X = tailX[i]
        prev2Y = tailY[i]
        tailX[i] = prevX
        tailY[i] = prevY
        prevX = prev2X
        prevY = prev2Y
    logic()
    pygame.display.flip()
    clock.tick(60)
