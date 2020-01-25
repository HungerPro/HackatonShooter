import pygame
import threading
pygame.init()
win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.display.get_surface()
winwidth, winheight = surface.get_width(), surface.get_height()
pygame.display.set_caption('My game')
x = winwidth/2 - 51/2
y = winheight/2 - 51/2
speed = 0.00
run = True
side = [False, False, True, False, False, False, False, False]
back = False
side2 = []
spritesW = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\W7.png')]
spritesD = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\D7.png')]
spritesA = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\A7.png')]
spritesS = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\S7.png')]
spritesAW = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AW7.png')]
spritesAS = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\AS7.png')]
spritesWD = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\WD7.png')]
spritesSD = [pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD1.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD2.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD3.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD4.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD5.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD6.png'), pygame.image.load('C:\\Users\\vitit\Desktop\\chekpoint1\\SD7.png')]
impact = 0.5
animCount = 0
def drawpers():
    global animCount
    if side[2] == True:
        win.blit(spritesW[animCount], (x, y))
    if side[1] == True:
        win.blit(spritesD[animCount], (x, y))
    if side[0] == True:
        win.blit(spritesA[animCount], (x, y))
    if side[3] == True:
        win.blit(spritesS[animCount], (x, y))
    if side[6] == True:
        win.blit(spritesWD[animCount], (x, y))
    if side[4] == True:
        win.blit(spritesAW[animCount], (x, y))
    if side[5] == True:
        win.blit(spritesAS[animCount], (x, y))
    if side[7] == True:
        win.blit(spritesSD[animCount], (x, y))
def ac():
    global animCount
    while True:
        pygame.time.delay(50)
        if animCount >= 6:
            animCount = 0
        animCount += 1

def hello():
    global x
    global y
    global speed
    global back
    global side2
    global side
    global impact
    while True:
        pygame.time.delay(50)
        if impact > 0.01:
            impact -= 0.01
        if impact < -0.01:
            impact += 0.01
        if keys[pygame.K_SPACE]:
            for i in range(0, len(side)):
                if side[i] == True:
                    side2 = i
            if speed < 0.7:
                speed += 0.02
            if speed < 0:
                speed += 0.02
        if keys[pygame.K_x]:
            for i in range(0, len(side)):
                if side[i] == True:
                    side2 = i
            if speed > 0:
                speed -= 0.02
            if speed > -0.7:
                speed -= 0.02
        if not keys[pygame.K_SPACE] and not keys[pygame.K_x]:
            if speed < 0.0:
                speed += 0.02
            if speed > 0.0:
                speed -= 0.02
        if speed < 0.01 and speed > -0.01:
            speed = 0.00
def hello2():
    global x
    global y
    global speed
    global side
    global impact
    while True:
        pygame.time.delay(1)
        if side2 == 0:
            x -= speed
        if side2 == 1:
            x += speed
        if side2 == 2:
            y -= speed
        if side2 == 3:
            y += speed
        if side2 == 4:
            x -= speed
            y -= speed
        if side2 == 5:
            x -= speed
            y += speed
        if side2 == 6:
            x += speed
            y -= speed
        if side2 == 7:
            x += speed
            y += speed
hreadd3 = threading.Thread(target=ac)
hreadd3.start()
hreadd2 = threading.Thread(target=hello2)
hreadd2.start()
hreadd = threading.Thread(target=hello)
hreadd.start()

while run:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.K_a]:
        for i in range(0, 8):
            side[i] = False
        side[0] = True
    if keys[pygame.K_d]:
        for i in range(0, 8):
            side[i] = False
        side[1] = True
    if keys[pygame.K_w]:
        for i in range(0, 8):
            side[i] = False
        side[2] = True
    if keys[pygame.K_x]:
        for i in range(0, 8):
            side[i] = False
        side[3] = True
    if keys[pygame.K_a] and keys[pygame.K_w]:
        for i in range(0, 8):
            side[i] = False
        side[4] = True
    if keys[pygame.K_a] and keys[pygame.K_s]:
        for i in range(0, 8):
            side[i] = False
        side[5] = True
    if keys[pygame.K_d] and keys[pygame.K_w]:
        for i in range(0, 8):
            side[i] = False
        side[6] = True
    if keys[pygame.K_d] and keys[pygame.K_x]:
        for i in range(0, 8):
            side[i] = False
        side[7] = True
    if x >= winwidth + 20:
        x = -10
    if x <= -20:
        x = winwidth + 10
    if y >= winheight + 15:
        y = -10
    if y <= -20:
        y = winheight + 5
    win.fill((0, 0, 40))
    drawpers()
pygame.quit()