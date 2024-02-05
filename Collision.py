import pygame, sys
from pygame.locals import*

print("\n\n\n              COLLIDING BLOCKS PROBLEM VISUALISATION          ")
print("\n\n\nLook at the pygame caption for number of collisions")
n=int(input("\n\n\nMass Ratio (<=100): "))
print("\n\n This program might crash for certain values")

pygame.init()
scr=pygame.display.set_mode((1100,600))
c=pygame.time.Clock()
x2 = Rect(350,250,50,50)
x1 = Rect(500,250,50,50)
x0 = Rect(50,250,3,50)
v1 = -3
v2 = 0
x=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    c.tick(100)
    x2.x += v2
    x1.x += v1
    tol=1000
    if x2.colliderect(x0):
        if v2<=0:
            ovlp = x0.right-x2.left
            x2.x+=ovlp
            x+=1
            v2*=-1
        print(v2,v1)
    
    if x1.colliderect(x2):
        if v1 <= 0 and v2 >= 0:
            ovlp1 = abs(x2.right-x1.left)
            x1.x+=ovlp1/2
            x2.x-=ovlp1/2
            v1,v2 = (((n-1)*v1/(n+1))+(2*v2/(n+1))),((2*n*v1/(n+1))-((n-1)*v2/(n+1)))
            x+=1
        print(v2,v1)   
    if x2.colliderect(x1):
        if v1 >= 0 and v2 >= 0:
            ovlp2 = abs(x2.right-x1.left)
            x1.x+=ovlp2/2
            x2.x-=ovlp2/2
            v1,v2 = (((n-1)*v1/(n+1))+(2*v2/(n+1))),((2*n*v1/(n+1))-((n-1)*v2/(n+1)))
            x+=1
        print(v2,v1)  

    pygame.display.set_caption(str(x))
    pygame.draw.rect(scr,(255,255,255),x2)
    pygame.draw.rect(scr,(255,255,0),x1)
    pygame.draw.rect(scr,(255,255,255),x0)
    pygame.draw.line(scr,(255,255,255),[50,300],[50,50],5)
    pygame.draw.line(scr,(255,255,255),[50,300],[1100,300],2)
    pygame.display.flip()
    scr.fill((0,0,0))
