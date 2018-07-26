import pygame
pygame.init()
from math import sin, cos, radians

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("3D Translation")
clock = pygame.time.Clock()
done = False

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


def _3Dto2Dconverter(x,y,z):
 fov = 256
 distance = 4
 half_width = 640 / 2
 half_height = 480 / 2
 a = x * fov / (z + distance) + half_width
 b = -y * fov / (z + distance) + half_height
 return a,b


def translate(x,y,z,tx,ty,tz):
 A = [[1, 0, 0, tx],
      [0, 1, 0, ty],
      [0, 0, 1, tz],
      [0, 0, 0, 1]]

 B = [[x],
      [y],
      [z],
      [1]]

 result = [[0],
           [0],
           [0],
           [1]]


 for i in range(len(A)):
   for j in range(len(B[0])):
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]

 return result[0][0],result[1][0],result[2][0]

#before Translation
a1, b1, c1 = 1+0, 1+0, 1+0
a2, b2, c2 = 1+1, 1+0, 1+0
a3, b3, c3 = 1+0, 1+1, 1+0
a4, b4, c4 = 1+1, 1+1, 1+0
a5, b5, c5 = 1+0, 1+0, 1+1
a6, b6, c6 = 1+1, 1+0, 1+1
a7, b7, c7 = 1+0, 1+1, 1+1
a8, b8, c8 = 1+1, 1+1, 1+1

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

screen.fill(white)
pygame.draw.polygon(screen,black,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(screen,black,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(screen,black,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(screen,black,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)

#after Translation
tx,ty,tz = 10, 10, 10
a1,b1,c1 = translate(a1,b1,c1,tx,ty,tz)
a2,b2,c2 = translate(a2,b2,c2,tx,ty,tz)
a3,b3,c3 = translate(a3,b3,c3,tx,ty,tz)
a4,b4,c4 = translate(a4,b4,c4,tx,ty,tz)
a5,b5,c5 = translate(a5,b5,c5,tx,ty,tz)
a6,b6,c6 = translate(a6,b6,c6,tx,ty,tz)
a7,b7,c7 = translate(a7,b7,c7,tx,ty,tz)
a8,b8,c8 = translate(a8,b8,c8,tx,ty,tz)

x1, y1 = _3Dto2Dconverter(a1, b1, c1)
x2, y2 = _3Dto2Dconverter(a2, b2, c2)
x3, y3 = _3Dto2Dconverter(a3, b3, c3)
x4, y4 = _3Dto2Dconverter(a4, b4, c4)
x5, y5 = _3Dto2Dconverter(a5, b5, c5)
x6, y6 = _3Dto2Dconverter(a6, b6, c6)
x7, y7 = _3Dto2Dconverter(a7, b7, c7)
x8, y8 = _3Dto2Dconverter(a8, b8, c8)

pygame.draw.polygon(screen,red,((x3,y3),(x1,y1),(x2,y2),(x4,y4)),1)
pygame.draw.polygon(screen,red,((x7,y7),(x5,y5),(x6,y6),(x8,y8)),1)
pygame.draw.polygon(screen,red,((x3,y3),(x7,y7),(x8,y8),(x4,y4)),1)
pygame.draw.polygon(screen,red,((x1,y1),(x5,y5),(x6,y6),(x2,y2)),1)


while not done:
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   done = True

 pygame.display.update()
 clock.tick(100)
