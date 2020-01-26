import pygame
import threading
import time
import random
import math
from pygame import mixer
mixer.init()
pygame.init()
win = pygame.display.set_mode((1200,800))
surface = pygame.display.get_surface()
winwidth, winheight = surface.get_width(), surface.get_height()
pygame.display.set_caption('Spase Defence')
audiobullet = mixer.Sound('blast.ogg')
audiobombullet = mixer.Sound('blasteraudio.ogg')
audiobomanemy = mixer.Sound('bomaudio1.ogg')
blasteraudio = mixer.Sound('bomaudio3.ogg')
blinkaudio = mixer.Sound('blink.ogg')
lavel1 = False
lavel2 = False
lavel3 = False
bosslevel = 1
x = winwidth/2 - 51/2
y = winheight/2 - 51/2
wight = 40
height = 40
radius = 30
speed = 0.00
speedb = 7
speeden = 0.1
run = False
run2 = False
runn = True
winn1 = False
winn2 = False
side = [False, False, True, False, False, False, False, False]
back = False
side2 = []
appcan = True
life = 10
doublebullet = False
doublebullet2 = False
points = 28 #ljanbdslkjfbnasdjklfbasdhbjklfahnbjksdfnbjkasncm,X>CNVm,n.zxcbnvlkhjabhdns;ja
needpoints = 30
x2 = winwidth/2 - 35
y2 = winheight + 75
x1 = winwidth/2 - 35
y1 = -150
xb = 0
yb = 0
coords1x = (winwidth)/2 - 35
coords2y = (winheight/2 + winheight)/2 - 35
coords2x = (winwidth)/2 - 35
coords1y = (winheight/2 + 0)/2 - 35
bosslife = 100
gradus = 0
isbosslife = False
xboss = -50
yboss = -50
bg = pygame.image.load('bg2.jpg')
spritesW = [pygame.image.load('W1.png'), pygame.image.load('W2.png'), pygame.image.load('W3.png'), pygame.image.load('W4.png'), pygame.image.load('W5.png'), pygame.image.load('W6.png'), pygame.image.load('W7.png')]
spritesD = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png'), pygame.image.load('D7.png')]
spritesA = [pygame.image.load('A1.png'), pygame.image.load('A2.png'), pygame.image.load('A3.png'), pygame.image.load('A4.png'), pygame.image.load('A5.png'), pygame.image.load('A6.png'), pygame.image.load('A7.png')]
spritesS = [pygame.image.load('S1.png'), pygame.image.load('S2.png'), pygame.image.load('S3.png'), pygame.image.load('S4.png'), pygame.image.load('S5.png'), pygame.image.load('S6.png'), pygame.image.load('S7.png')]
spritesAW = [pygame.image.load('AW1.png'), pygame.image.load('AW2.png'), pygame.image.load('AW3.png'), pygame.image.load('AW4.png'), pygame.image.load('AW5.png'), pygame.image.load('AW6.png'), pygame.image.load('AW7.png')]
spritesAS = [pygame.image.load('AS1.png'), pygame.image.load('AS2.png'), pygame.image.load('AS3.png'), pygame.image.load('AS4.png'), pygame.image.load('AS5.png'), pygame.image.load('AS6.png'), pygame.image.load('AS7.png')]
spritesWD = [pygame.image.load('WD1.png'), pygame.image.load('WD2.png'), pygame.image.load('WD3.png'), pygame.image.load('WD4.png'), pygame.image.load('WD5.png'), pygame.image.load('WD6.png'), pygame.image.load('WD7.png')]
spritesSD = [pygame.image.load('SD1.png'), pygame.image.load('SD2.png'), pygame.image.load('SD3.png'), pygame.image.load('SD4.png'), pygame.image.load('SD5.png'), pygame.image.load('SD6.png'), pygame.image.load('SD7.png')]
spritesBUL = [pygame.image.load('BB1t2.png'), pygame.image.load('BB2t2.png')]
spritesenemies = [pygame.image.load('EN1.png'), pygame.image.load('EN2.png')]
spritessuperenemies = [pygame.image.load('SEN1t2.png'), pygame.image.load('SEN2t2.png')]
spritesboom = [pygame.image.load('boom1.png'), pygame.image.load('boom2.png')]
spritespd = [pygame.image.load('boom3-a.png'), pygame.image.load('boom3-b.png')]
spritesbonus = [pygame.image.load('SHB.png'), pygame.image.load('SBB.png')]
spriteshield = [pygame.image.load('shield.png'), pygame.image.load('shield2.png')]
spritesbasa2 = {'start':[pygame.image.load('flybasa1.png'), pygame.image.load('flybasa2.png'), pygame.image.load('flybasa3.png'),
                        pygame.image.load('flybasa4.png'), pygame.image.load('flybasa5.png'), pygame.image.load('flybasa6.png'),
                        pygame.image.load('flybasa7.png'), pygame.image.load('flybasa8.png'), pygame.image.load('flybasa9.png'),
                        pygame.image.load('flybasa10.png')],
               'middle':[pygame.image.load('basa1.png'), pygame.image.load('basa2.png'), pygame.image.load('basa3.png'),
                         pygame.image.load('basa4.png'), pygame.image.load('basa5.png'), pygame.image.load('basa6.png'),
                         pygame.image.load('basa7.png'), pygame.image.load('basa8.png'), pygame.image.load('basa9.png'),
                         pygame.image.load('basa10.png')],
               'end':[pygame.image.load('basa1.png'), pygame.image.load('basa2.png'), pygame.image.load('basa3.png'),
                         pygame.image.load('basa4.png'), pygame.image.load('basa5.png'), pygame.image.load('basa6.png'),
                         pygame.image.load('basa7.png'), pygame.image.load('basa8.png'), pygame.image.load('basa9.png'),
                         pygame.image.load('basa10.png')]}
spritesbasa = {'start':[pygame.image.load('basa1.png'), pygame.image.load('basa2.png'), pygame.image.load('basa3.png'),
                         pygame.image.load('basa4.png'), pygame.image.load('basa5.png'), pygame.image.load('basa6.png'),
                         pygame.image.load('basa7.png'), pygame.image.load('basa8.png'), pygame.image.load('basa9.png'),
                         pygame.image.load('basa10.png')],
               'middle':[pygame.image.load('basa1.png'), pygame.image.load('basa2.png'), pygame.image.load('basa3.png'),
                         pygame.image.load('basa4.png'), pygame.image.load('basa5.png'), pygame.image.load('basa6.png'),
                         pygame.image.load('basa7.png'), pygame.image.load('basa8.png'), pygame.image.load('basa9.png'),
                         pygame.image.load('basa10.png')],
               'end':[pygame.image.load('flybasa1.png'), pygame.image.load('flybasa2.png'), pygame.image.load('flybasa3.png'),
                        pygame.image.load('flybasa4.png'), pygame.image.load('flybasa5.png'), pygame.image.load('flybasa6.png'),
                        pygame.image.load('flybasa7.png'), pygame.image.load('flybasa8.png'), pygame.image.load('flybasa9.png'),
                        pygame.image.load('flybasa10.png')]}
spritesbomen = {'t1':[pygame.image.load('bomen1.png'), pygame.image.load('bomen2.png')], 't2':[pygame.image.load('bomen1t2.png'), pygame.image.load('bomen2t2.png')]}
spritesboombasat1 = [pygame.image.load('basaboom0t1.png'), pygame.image.load('basaboom1t1.png'), pygame.image.load('basaboom2t1.png'), pygame.image.load('basaboom3t1.png'), pygame.image.load('basaboom4t1.png')]
spritesnumbers = [pygame.image.load('n0.png'), pygame.image.load('n1.png'), pygame.image.load('n2.png'), pygame.image.load('n3.png'), pygame.image.load('n4.png'),
                  pygame.image.load('n5.png'), pygame.image.load('n6.png'), pygame.image.load('n7.png'), pygame.image.load('n8.png'),
                  pygame.image.load('n9.png')]
spriteslife = [pygame.image.load('life1.png'), pygame.image.load('life2.png'), pygame.image.load('life3.png'), pygame.image.load('life4.png')]
spritesblaster = {'left':[pygame.image.load('blaster1t1.png'), pygame.image.load('blaster2t1.png')],
                  'right':[pygame.image.load('blaster1t2.png'), pygame.image.load('blaster2t2.png')],
                  'up':[pygame.image.load('blaster1t3.png'), pygame.image.load('blaster2t3.png')],
                  'down':[pygame.image.load('blaster1t4.png'), pygame.image.load('blaster2t4.png')],
                  'upleft':[pygame.image.load('blaster1t5.png'), pygame.image.load('blaster2t5.png')],
                  'upright':[pygame.image.load('blaster1t7.png'), pygame.image.load('blaster2t7.png')],
                  'downleft':[pygame.image.load('blaster1t6.png'), pygame.image.load('blaster2t6.png')],
                  'downright':[pygame.image.load('blaster1t8.png'), pygame.image.load('blaster2t8.png')]}
spritesbigbasabom = [pygame.image.load('BIGBASABOM1.png'),
                     pygame.image.load('BIGBASABOM2.png'),
                     pygame.image.load('BIGBASABOM3.png'),
                     pygame.image.load('BIGBASABOM4.png'),
                     pygame.image.load('BIGBASABOM5.png'),
                     pygame.image.load('BIGBASABOM6.png'),
                     pygame.image.load('BIGBASABOM7.png'),
                     pygame.image.load('BIGBASABOM8.png'),
                     pygame.image.load('BIGBASABOM9.png'),
                     pygame.image.load('BIGBASABOM10.png'),
                     pygame.image.load('BIGBASABOM11.png'),
                     pygame.image.load('BIGBASABOM12.png'),]
spritesbombomen = [pygame.image.load('bombomen1.png'), pygame.image.load('bombomen2.png'), pygame.image.load('bombomen3.png'), pygame.image.load('bombomen4.png')]
spritesmeteor = [pygame.image.load('meteort1.png'), pygame.image.load('meteort2.png'), pygame.image.load('meteort3.png')]
dropedmineralssprites = {'i':pygame.image.load('iron.png'), 'g':pygame.image.load('gold.png'), 'd':pygame.image.load('diamond.png'), 'em':pygame.image.load('emerald.png')}
spritesdash = {'1':[pygame.image.load('dash8.png'), pygame.image.load('dash7.png'), pygame.image.load('dash6.png'),
               pygame.image.load('dash5.png'), pygame.image.load('dash4.png'), pygame.image.load('dash3.png'),
               pygame.image.load('dash2.png'), pygame.image.load('dash1.png')],
               '2': [pygame.image.load('dash8t2.png'), pygame.image.load('dash7t2.png'), pygame.image.load('dash6t2.png'),
                     pygame.image.load('dash5t2.png'), pygame.image.load('dash4t2.png'), pygame.image.load('dash3t2.png'),
                     pygame.image.load('dash2t2.png'), pygame.image.load('dash1t2.png')]
               }
spritesbomba = [pygame.image.load('bomba1.png'), pygame.image.load('bomba2.png')]
spritesboommeteor = {'t1':[pygame.image.load('boommeteor8t1.png'), pygame.image.load('boommeteor7t1.png'), pygame.image.load('boommeteor6t1.png'),
               pygame.image.load('boommeteor5t1.png'), pygame.image.load('boommeteor4t1.png'), pygame.image.load('boommeteor3t1.png'),
               pygame.image.load('boommeteor2t1.png'), pygame.image.load('boommeteor1t1.png')], 't2':
               [pygame.image.load('boommeteor8t2.png'), pygame.image.load('boommeteor7t2.png'), pygame.image.load('boommeteor6t2.png'),
               pygame.image.load('boommeteor5t2.png'), pygame.image.load('boommeteor4t2.png'), pygame.image.load('boommeteor3t2.png'),
               pygame.image.load('boommeteor2t2.png'), pygame.image.load('boommeteor1t2.png')]}
spritesstars = [[pygame.image.load('star1.png'), pygame.image.load('star2.png')], [pygame.image.load('star1t2.png'), pygame.image.load('star2t2.png')],
                [pygame.image.load('star1t2.png'), pygame.image.load('star2t2.png')], [pygame.image.load('star1t3.png'), pygame.image.load('star2t3.png')]]
spritesboss = [pygame.image.load('boss1.png'), pygame.image.load('boss2.png')]
spritesataka1 = [pygame.image.load('bossataka3t2.png'), pygame.image.load('bossataka2t2.png'), pygame.image.load('bossataka1t2.png')]
spritesataka2 = [pygame.image.load('ataka2.png'), pygame.image.load('ataka1.png')]
spritesataka3 = [pygame.image.load('bossataka5.png'), pygame.image.load('bossataka4.png'), pygame.image.load('bossataka3.png'), pygame.image.load('bossataka2.png'), pygame.image.load('bossataka1.png')]
spritesbossbomb = [pygame.image.load('bossbomb1.png'), pygame.image.load('bossbomb2.png'), pygame.image.load('bossbomb3.png')]
spritesbombossbomb = [pygame.image.load('bombossbomb1.png'), pygame.image.load('bombossbomb2.png'), pygame.image.load('bombossbomb3.png'), pygame.image.load('bombossbomb4.png')]
spritesdeathboss = [pygame.image.load('deathboss1.png'), pygame.image.load('deathboss2.png'), pygame.image.load('deathboss3.png'),
                    pygame.image.load('deathboss4.png'), pygame.image.load('deathboss5.png'), pygame.image.load('deathboss6.png')]
defencesprites = [pygame.image.load('defence1.png'), pygame.image.load('defence2.png'), pygame.image.load('defence3.png'), pygame.image.load('defence4.png')]
stars = []
boomesmeteor = []
meteors = []
enemylife = 1
senemylife = 2
bomsbomen = []
bigbasabom = False
canbigbasabom = True
canbigbasabom2 = True
xbb = 0
ybb = 0
bigbasabomCount = 0
animCount = 0
animCount2 = 0
shieldCount = 0
basaCount = 0
bullets = []
enemies = []
bomenemies = []
booms = []
bonuses = []
isshield = False
isshield2 = False
qwerty1 = True
qwerty2 = True
position = 'start'
basabooms = []
speedbomen = 0.1
lifebasa1 = 10
lifebasa2 = 10
number = 0
number2 = 2
isblaster = False
timeon = [1000, 1000, 1000]
minerals = [['d', 'i', 'd', 'em'], ['i', 'i', 'i', 'g', 'd'], ['g', 'i', 'g', 'em']]
lifebomen = 100
sideblaster = 'up'
blasterCount = 0
impact = 0
dropedminerals = []
diamonds = 0
gold = 0
iron = 0
needdiamonds = 2
needgold = 3
neediron = 5
damage = 1
timerbomen = 13
timermen = 3
starttimerbomen = 20
starttimermen = 5
dashx = 0
dashy = 0
dash = 150
candash = True
dashtimes = 2
bombax = 0
isbomba = False
bombay =0
dashs = []
numbermeteorbomba = 0
bossataka1 = False
bossataka1x = 0
bossataka1y = 0
bossataka1Count = 2
delayataka1 = False
bossataka2 = False
bossataka2x = 0
bossataka2y = 0
bossataka2Count = 1
delayataka2 = False
bossataka3 = False
bossataka3x = 0
bossataka3y = 0
bossataka3Count = 4
cdbossataka3 = 3000
delayataka3 = False
bossbomb = False
bossbombx = 0
bossbomby = 0
bossbombCount = 0
delaybossbomb = False
speedbossbomb = 0.3
bombossbomb = False
bombossbombx = 0
bombossbomby = 0
bombossbombCount = 0
deathboss = False
deathbossx = 0
deathbossy = 0
deathbossCount = 0
speedboss = 0.15
defence = False
defenceCount = 0
def deffencew():
    global defence
    global defenceCount
    pygame.time.delay(600)
    audiobombullet.play()
    defenceCount += 1
    pygame.time.delay(600)
    audiobombullet.play()
    defenceCount += 1
    pygame.time.delay(600)
    audiobombullet.play()
    defenceCount += 1
    pygame.time.delay(600)
    audiobombullet.play()
def playblinkaudio():
    global blinkaudio
    blinkaudio.play()
def playblasteraudio():
    global blasteraudio
    blasteraudio.play()
def audiobulletdef():
    global audiobullet
    audiobullet.play()
def audiobombulletdef():
    global audiobombullet
    audiobombullet.play()
def audiobomanemmy():
    global audiobomanemy
    audiobomanemy.play()
def deathbossaa():
    global deathboss
    global deathbossCount
    pygame.time.delay(80)
    deathbossCount += 1
    pygame.time.delay(80)
    deathbossCount += 1
    pygame.time.delay(80)
    deathbossCount += 1
    pygame.time.delay(80)
    deathbossCount += 1
    pygame.time.delay(80)
    deathbossCount += 1
    pygame.time.delay(80)
    deathboss = False
    deathbossCount = 0
def bombossbomba():
    global bombossbomb
    global bombossbombCount
    pygame.time.delay(100)
    bombossbombCount += 1
    pygame.time.delay(100)
    bombossbombCount += 1
    pygame.time.delay(100)
    bombossbombCount += 1
    pygame.time.delay(100)
    bombossbomb = False
    bombossbombCount = 0
def bossbomba():
    global bossbomb
    global bossbombCount
    global delaybossbomb
    global bombossbomb
    global bombossbombx
    global bombossbomby
    global bombossbombCount
    for bbmd in range(0, 6):
        pygame.time.delay(200)
        bossbombCount += 1
        pygame.time.delay(200)
        bossbombCount += 1
        pygame.time.delay(200)
        bossbombCount -= 1
        pygame.time.delay(200)
        bossbombCount -= 1
    pygame.time.delay(200)
    if bossbomb == True:
        bombossbomb = True
        bombossbombx = bossbombx - 5
        bombossbomby = bossbomby - 5
        hreaddb2 = threading.Thread(target=bombossbomba)
        hreaddb2.start()
        bossbomb = False
    pygame.time.delay(1500)
    delaybossbomb = False
    bossbombCount = 0
def bossatak1():
    global bossataka1
    global bossataka1Count
    global delayataka1
    for at in range(0, 2):
        pygame.time.delay(50)
        bossataka1Count -= 1
    pygame.time.delay(50)
    bossataka1 = False
    pygame.time.delay(900)
    delayataka1 = False
    bossataka1Count = 2
def bossatak2():
    global bossataka2
    global bossataka2Count
    global delayataka2
    pygame.time.delay(100)
    bossataka2Count -= 1
    pygame.time.delay(100)
    bossataka2Count += 1
    pygame.time.delay(100)
    bossataka2Count -= 1
    pygame.time.delay(100)
    bossataka2Count += 1
    pygame.time.delay(100)
    bossataka2Count -= 1
    pygame.time.delay(100)
    bossataka2 = False
    pygame.time.delay(100)
    delayataka2 = False
    bossataka2Count = 1
def bossatak3():
    global bossataka3
    global bossataka3Count
    global delayataka3
    global cdbossataka3
    for at in range(0, 4):
        pygame.time.delay(100)
        bossataka3Count -= 1
    pygame.time.delay(100)
    bossataka3 = False
    pygame.time.delay(cdbossataka3)
    delayataka3 = False
    bossataka3Count = 4

def drawnumbers(chis, coordsch1, coordsch2):
    for ch in chis:
        ch = int(ch)
        win.blit(spritesnumbers[ch], (coordsch1, coordsch2))
        coordsch1 += 20
def sstars():
    global stars
    global run
    global run2
    while run or run2:
        for st in range(0, len(stars)):
            if stars[st][2] == 1:
                stars[st][2] = 0
            pygame.time.delay(170)
            if stars[st][2] == 0:
                stars[st][2] = 1

def createmeteor():
    global meteors
    global winwidth
    global winheight
    global timeon
    global minerals
    global isbosslife
    global run
    global run2
    time.sleep(10)
    while run or run2:
        time.sleep(10)
        faq = random.randint(1,2)
        if isbosslife == False:
            if faq == 1:
                mr = [0]
                ym = random.randint(100, winheight - 100)
                if ym < winheight/2 - 100:
                    mr = [0, 0.05, 0.1]
                if ym > winheight/2 + 100:
                    mr = [0, -0.05, -0.1]
                cc = random.choice(mr)
                spritte1 = [1, 2, 0]
                spritte = random.choice(spritte1)
                meteors.append([-150, ym, spritte, 0.1, cc, timeon[spritte], minerals[spritte]])
            if faq == 2:
                mr = [0, 0, 0.05, 0.1, -0.03, -0.08]
                ym = random.randint(100, winheight - 100)
                if ym < winheight/2 - 100:
                    mr = [0, 0.05, 0.1]
                if ym > winheight/2 + 100:
                    mr = [0, -0.05, -0.1]
                cc = random.choice(mr)
                spritte1 = [1, 2, 0]
                spritte = random.choice(spritte1)
                meteors.append([winwidth+150, ym, spritte, -0.1, cc, timeon[spritte], minerals[spritte]])
        if isbosslife == True:
            break
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
def timmer():
    global appcan
    pygame.time.delay(500)
    appcan = True
def timmer2():
    global isshield
    global isshield2
    global shieldCount
    pygame.time.delay(9000)
    if isshield2 == False:
        shieldCount += 1
        isshield = False
    else:
        isshield2 = False
def timmer3():
    global doublebullet
    global doublebullet2
    pygame.time.delay(9000)
    if doublebullet2 == False:
        doublebullet = False
    else:
        doublebullet2 = False

def timmer4():
    global dashtimes
    global run
    global run2
    while run or run2:
        pygame.time.delay(5000)
        if dashtimes < 2:
            dashtimes += 1



def positionbasa():
    global coords1x
    global coords1y
    global coords2x
    global coords2y
    global x1
    global x2
    global y1
    global y2
    global position
    global winwidth
    global winheight
    global run
    global run2
    while run or run2:
        while True and position == 'start':
            pygame.time.delay(100)
            if y1 == coords1y and y2 == coords2y:
                position = 'middle'
                break
        while True and position == 'middle':
            pygame.time.delay(100)
            if points > needpoints:
                position = 'end'
                coords1y = -150
                coords2y = winheight + 75
                break
        while True and position == 'end':
            pygame.time.delay(100)
            if y1 == coords1y and y2 == coords2y:
                position = 'start'
                break
        while True and position == 'start':
            pygame.time.delay(100)
            if bosslife <= 0:
                break

def timmerAnn():
    global enemies
    global qwerty1
    global qwerty2
    global number
    global enemylife
    global winwidth
    global winheight
    global senemylife
    global timermen
    global starttimermen
    global run
    global run2
    time.sleep(starttimermen)
    while run or run2:
        if points > 60 and timermen > 2:
            timermen -= 1
        if points <= needpoints:
            superspisok = ['None', 'None', 'None', 'None', 'None', 'Super']
            arr = random.choice(superspisok)
            time.sleep(timermen)
            xen = 0
            yen = 0
            tt = random.randint(1,2)
            if tt == 1:
                xen = random.randint(-50, 0)
                yen = random.randint(-50, winheight + 75)
            if tt == 2:
                xen = random.randint(winwidth + 20, winwidth + 60)
                yen = random.randint(-50, winheight + 75)
            if arr == 'Super':
                enemies.append([xen, yen, arr, senemylife, 75])
            if arr == 'None':
                enemies.append([xen, yen, arr, enemylife, 40])
        if points == needpoints - 10 and qwerty1 == True:
            for asdf in range(0, 3):
                superspisok = ['None', 'None', 'None', 'None', 'None', 'Super']
                arr = random.choice(superspisok)
                xen = 0
                yen = 0
                tt = random.randint(1, 2)
                if tt == 1:
                    xen = random.randint(-50, 0)
                    yen = random.randint(-50, winheight + 75)
                if tt == 2:
                    xen = random.randint(winwidth + 20, winwidth + 60)
                    yen = random.randint(-50, winheight + 75)
                qwerty1 = False
                if arr == 'Super':
                    enemies.append([xen, yen, arr, senemylife, 75])
                if arr == 'None':
                    enemies.append([xen, yen, arr, enemylife, 40])
        if points == needpoints and qwerty2 == True:
            for asdf2 in range(0, 8):
                superspisok = ['None', 'None', 'None', 'None', 'None', 'Super']
                arr = random.choice(superspisok)
                xen = 0
                yen = 0
                tt = random.randint(1, 2)
                if tt == 1:
                    xen = random.randint(-50, 0)
                    yen = random.randint(-50, winheight + 75)
                if tt == 2:
                    xen = random.randint(winwidth + 20, winwidth + 60)
                    yen = random.randint(-50, winheight + 75)
                qwerty2 = False
                if arr == 'Super':
                    enemies.append([xen, yen, arr, senemylife, 75])
                if arr == 'None':
                    enemies.append([xen, yen, arr, enemylife, 40])
        if points > needpoints:
            break

def timmerAnn2():
    global bomenemies
    global lifebomen
    global winwidth
    global winheight
    global timerbomen
    global starttimerbomen
    global run
    global run2
    time.sleep(starttimerbomen)
    time.sleep(0)
    starttimerbomen = 0
    while run or run2:
        dl = 700
        if 700 - points * 3 > 200:
            dl = 700 - points * 3
        if 700 - points * 3 < 200:
            dl = 200
        if (points < needpoints and lifebasa1 > 0) or (points < needpoints and lifebasa2 > 0):
            time.sleep(timerbomen)
            alt = random.randint(1,2)
            if alt == 1:
                if lifebasa1 > 0:
                    yy = random.randint(-100, winheight + 75)
                    s1 = (x1 - 50) ** 2
                    s2 = (y1 - yy) ** 2
                    s3 = math.sqrt(s1 + s2)
                    s4 = (x2 - 50) ** 2
                    s5 = (y2 - yy) ** 2
                    s6 = math.sqrt(s4 + s5)
                    if s3 <= s6:
                        for i in range(0, 5):
                            pygame.time.delay(dl)
                            bomenemies.append([-50, yy, 't1', 'basa1', lifebomen])
                    if s3 > s6:
                        for i in range(0, 5):
                            pygame.time.delay(dl)
                            bomenemies.append([-50, yy, 't1', 'basa2', lifebomen])
                if lifebasa1 <= 0:
                    yy = random.randint(-100, 700)
                    for i in range(0, 5):
                        pygame.time.delay(dl)
                        bomenemies.append([-50, yy, 't1', 'basa2', lifebomen])
            if alt == 2:
                if lifebasa2 > 0:
                    yy2 = random.randint(-100, winheight + 75)
                    s1 = (x1 + winwidth) ** 2
                    s2 = (y1 - yy2) ** 2
                    s3 = math.sqrt(s1 + s2)
                    s4 = (x2 + winwidth) ** 2
                    s5 = (y2 - yy2) ** 2
                    s6 = math.sqrt(s4 + s5)
                    if s3 <= s6:
                        for i in range(0, 5):
                            pygame.time.delay(dl)
                            bomenemies.append([winwidth + 50, yy2, 't2', 'basa1', lifebomen])
                    if s3 > s6:
                        for i in range(0, 5):
                            pygame.time.delay(dl)
                            bomenemies.append([winwidth + 50, yy2, 't2', 'basa2', lifebomen])
                if lifebasa2 <= 0:
                    yy2 = random.randint(-100, 700)
                    for i in range(0, 5):
                        pygame.time.delay(dl)
                        bomenemies.append([winwidth + 50, yy2, 't2', 'basa1', lifebomen])
        if (points > needpoints) or (lifebasa1 <= 0 and lifebasa2 <= 0):
            break
def timerbigbasabom():
    global bigbasabom
    global bigbasabomCount
    for bi in range(0, 12):
        bigbasabomCount = bi
        pygame.time.delay(60)
    bigbasabom = False
def ac():
    global animCount
    global animCount2
    global blasterCount
    global run
    global run2
    while run or run2:
        pygame.time.delay(50)
        if blasterCount == 0:
            blasterCount += 1
        else:
            blasterCount -= 1
        if animCount >= 6:
            animCount = 0
        animCount += 1
def anc2():
    global booms
    global animCount2
    global run
    global run2
    while run or run2:
        pygame.time.delay(200)
        animCount2 += 1
        pygame.time.delay(200)
        animCount2 -= 1
        for bull in range(0, len(booms)):
            try:
                if booms[bull][2] > 0:
                    booms[bull][2] -= 1
                else:
                    booms.remove(booms[bull])
            except:
                pass
def anc1t2():
    global basabooms
    global run
    global run2
    while run or run2:
        pygame.time.delay(50)
        for bbomt1 in range(0, len(basabooms)):
            pygame.time.delay(50)
            try:
                if basabooms[bbomt1][2] >= 4:
                    basabooms.remove(basabooms[bbomt1])
                else:
                    basabooms[bbomt1][2] += 1
            except:
                pass
def anc1t3():
    global bomsbomen
    global run
    global run2
    while run or run2:
        pygame.time.delay(50)
        for bbomen in range(0, len(bomsbomen)):
            pygame.time.delay(50)
            try:
                if bomsbomen[bbomen][2] >= 3:
                    bomsbomen.remove(bomsbomen[bbomen])
                else:
                    bomsbomen[bbomen][2] += 1
            except:
                pass
def dashtimer():
    global dashs
    global boomesmeteor
    global run
    global run2
    while run or run2:
        pygame.time.delay(50)
        for ddash in range(0, len(dashs)):
            try:
                if dashs[ddash][2] < 1:
                    dashs.remove(dashs[ddash])
                    break
                if dashs[ddash][2] > 0:
                    dashs[ddash][2] -= 1
            except:
                pass
        for bmm in range(0, len(boomesmeteor)):
            try:
                if boomesmeteor[bmm][2] < 1:
                    boomesmeteor.remove(boomesmeteor[bmm])
                    break
                if boomesmeteor[bmm][2] > 0:
                    boomesmeteor[bmm][2] -= 1
            except:
                pass

def anc3():
    global basaCount
    global run
    global run2
    while run or run2:
        for bdc in range(0,9):
            pygame.time.delay(100)
            basaCount += 1
        basaCount = 0
def timmer5():
    global candash
    global dropedminerals
    global run
    global run2
    while run or run2:
        pygame.time.delay(800)
        if candash == False:
            candash = True
        for min3 in range(0, len(dropedminerals)):
            if dropedminerals[min3][3] > 0:
                dropedminerals[min3][3] -= 1
def hello():
    global x
    global y
    global speed
    global back
    global side2
    global side
    global impact
    global run
    global run2
    while run or run2:
        pygame.time.delay(50)
        if impact > 0.01:
            impact -= 0.01
        if impact < -0.01:
            impact += 0.01
        if keys[pygame.K_r]:
            for i in range(0, len(side)):
                if side[i] == True:
                    side2 = i
            if speed < 0.7:
                speed += 0.02
            if speed < 0:
                speed += 0.02
        if keys[pygame.K_4]:
            for i in range(0, len(side)):
                if side[i] == True:
                    side2 = i
            if speed > 0:
                speed -= 0.02
            if speed > -0.7:
                speed -= 0.02
        if not keys[pygame.K_r] and not keys[pygame.K_4]:
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
    global booms
    global bullets
    global enemies
    global life
    global points
    global bonuses
    global isshield
    global doublebullet
    global isshield2
    global doublebullet2
    global shieldCount
    global coords1x
    global coords1y
    global coords2x
    global coords2y
    global x1
    global x2
    global y1
    global y2
    global bomenemies
    global speedbomen
    global lifebasa1
    global lifebasa2
    global basabooms
    global xb
    global yb
    global sideblaster
    global bigbasabom
    global canbigbasabom
    global canbigbasabom2
    global xbb
    global ybb
    global run
    global bomsbomen
    global isbosslife
    global bosslife
    global xboss
    global yboss
    global needpoints
    global position
    global qwerty1
    global qwerty2
    global impact
    global side2
    global winwidth
    global winheight
    global bosslevel
    global dropedminerals
    global diamonds
    global gold
    global iron
    global damage
    global dashx
    global dashy
    global dash
    global bombax
    global bombay
    global isbomba
    global numbermeteorbomba
    global boomesmeteor
    global speedboss
    global bossataka1
    global bossataka1x
    global bossataka1y
    global bossataka1Count
    global delayataka1
    global bossataka2
    global bossataka2x
    global bossataka2y
    global bossataka2Count
    global delayataka2
    global bossataka3
    global bossataka3x
    global bossataka3y
    global bossataka3Count
    global delayataka3
    global cdbossataka3
    global bossbomb
    global bossbombx
    global bossbomby
    global bossbombCount
    global delaybossbomb
    global speedbossbomb
    global bombossbomb
    global bombossbombx
    global bombossbomby
    global bombossbombCount
    global deathboss
    global deathbossx
    global deathbossy
    global deathbossCount
    global run
    global run2
    global winn1
    global winn2
    global defence
    global defenceCount
    while run or run2:
        pygame.time.delay(1)
        if needdiamonds <= diamonds and needgold <= gold and neediron <= iron and winn1 == False and winn2 == False:
            winn1 = True
            defencethr = threading.Thread(target=deffencew)
            defencethr.start()
            time.sleep(6)
            defence = False
            defenceCount = 0
            run = False
        if side[0] == True:
            sideblaster = 'left'
            dashy = y
            dashx = x - dash
            yb = y - 5
            xb = x - 55
            x += impact
        if side[1] == True:
            sideblaster = 'right'
            dashy = y
            dashx = x + dash
            yb = y - 5
            xb = x + 55
            x -= impact
        if side[2] == True:
            sideblaster = 'up'
            dashy = y - dash
            dashx = x
            yb = y - 55
            xb = x - 5
            y += impact
        if side[3] == True:
            sideblaster = 'down'
            dashy = y + dash
            dashx = x
            yb = y + 55
            xb = x - 5
            y -= impact
        if side[4] == True:
            sideblaster = 'upleft'
            dashy = y - dash
            dashx = x - dash
            yb = y - 45
            xb = x - 45
            x += impact
            y += impact
        if side[5] == True:
            sideblaster = 'downleft'
            dashy = y + dash
            dashx = x - dash
            yb = y + 45
            xb = x - 45
            x += impact
            y -= impact
        if side[6] == True:
            sideblaster = 'upright'
            dashy = y - dash
            dashx = x + dash
            yb = y - 45
            xb = x + 45
            x -= impact
            y += impact
        if side[7] == True:
            sideblaster = 'downright'
            dashy = y + dash
            dashx = x + dash
            yb = y + 45
            xb = x + 45
            x -= impact
            y -= impact
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
        for met2 in range(0, len(meteors)):
            try:
                tip = 't1'
                if meteors[met2][2] == 0 or meteors[met2][2] == 2:
                    tip = 't1'
                if meteors[met2][2] == 1:
                    tip = 't2'
                if meteors[met2][5] <= 0:
                    mineral = random.choice(meteors[met2][6])
                    if meteors[met2][2] == 0 or meteors[met2][2] == 2:
                        dropedminerals.append([mineral, meteors[met2][0] + 75, meteors[met2][1] + 75, 2])
                    if meteors[met2][2] == 1:
                        dropedminerals.append([mineral, meteors[met2][0] + 25, meteors[met2][1] + 25, 2])
                    if numbermeteorbomba == met2:
                        isbomba = False
                    boomesmeteor.append([meteors[met2][0] - 25, meteors[met2][1] - 25, 8, tip])
                    meteors.remove(meteors[met2])
                if meteors[met2][0] > winwidth + 200:
                    meteors.remove(meteors[met2])
                if meteors[met2][0] < - 200:
                    meteors.remove(meteors[met2])
                if meteors[met2][1] > winheight + 100:
                    meteors.remove(meteors[met2])
                if meteors[met2][1] < - 100:
                    meteors.remove(meteors[met2])
                meteors[met2][0] += meteors[met2][3]
                meteors[met2][1] += meteors[met2][4]

                needfaqrast = 0
                razmer = 0
                if meteors[met2][2] == 0 or meteors[met2][2] == 2:
                    needfaqrast = 100
                    razmer = 100
                if meteors[met2][2] == 1:
                    needfaqrast = 50
                    razmer = 50
                faqrast1 = (meteors[met2][0] + razmer - x - 25) ** 2
                faqrast2 = (meteors[met2][1] + razmer - y - 25) ** 2
                faqrast3 = math.sqrt(faqrast1 + faqrast2)
                if faqrast3 <= needfaqrast:
                    numbermeteorbomba = met2
                    isbomba = True
                    bombax = meteors[met2][0] + needfaqrast - 20
                    bombay = meteors[met2][1] + needfaqrast - 20
                    meteors[met2][5] -= 1
                if faqrast3 > needfaqrast:
                    if numbermeteorbomba == met2:
                        isbomba = False
                    meteors[met2][5] = 1000

            except:
                pass
        for min2 in range(0, len(dropedminerals)):
            mineralrast1 = (dropedminerals[min2][1] - x) ** 2
            mineralrast2 = (dropedminerals[min2][2] - y) ** 2
            mineralrast3 = math.sqrt(mineralrast1 + mineralrast2)
            if mineralrast3 <= 35 and dropedminerals[min2][3] <= 0:
                if dropedminerals[min2][0] == 'i':
                    iron += 1
                if dropedminerals[min2][0] == 'g':
                    gold += 1
                if dropedminerals[min2][0] == 'd':
                    diamonds += 1
                if dropedminerals[min2][0] == 'em':
                    diamonds += 1
                    gold += 1
                    iron += 1
                dropedminerals.remove(dropedminerals[min2])
        for i in range(0, len(bullets)):
            if bullets[i][0] >= winwidth:
                bullets.remove(bullets[i])
                break
            if bullets[i][0] <= 0:
                bullets.remove(bullets[i])
                break
            if bullets[i][1] >= winheight + 30:
                bullets.remove(bullets[i])
                break
            if bullets[i][1] <= 0:
                bullets.remove(bullets[i])
                break
        for i in range(0, len(enemies)):
            try:
                if enemies[i][3] <= 0:
                    booms.append([enemies[i][0], enemies[i][1], 2])
                    if enemies[i][2] == 'Super':
                        bonusspisok = ['shield', 'doublebullet', 'shield']
                        bonus = random.choice(bonusspisok)
                        bonuses.append([enemies[i][0] + 20, enemies[i][1] + 5, bonus])
                    points += 1
                    enemies.remove(enemies[i])
                rastx = (enemies[i][0] - x) ** 2
                rasty = (enemies[i][1] - y) ** 2
                rast = math.sqrt(rastx + rasty)
                if isshield == True:
                    if rast <= 45:
                        audioplay3 = threading.Thread(target=audiobomanemmy)
                        audioplay3.start()
                        booms.append([enemies[i][0], enemies[i][1], 2])
                        enemies.remove(enemies[i])
                        shieldCount += 1
                        isshield = False
                if isshield == False:
                    shieldCount = 0
                    if rast <= 35:
                        audioplay3 = threading.Thread(target=audiobomanemmy)
                        audioplay3.start()
                        booms.append([enemies[i][0], enemies[i][1], 2])
#                        booms.append([x, y, 2, 'pd'])
                        enemies.remove(enemies[i])
                        life -= 1
#                        time.sleep(2)
#                        print(points)
#                        pygame.quit()
                if rast >= 35:
                    for n in range(0, len(bullets)):
                        try:
                            if bullets[n][0] >= enemies[i][0] and bullets[n][0] <= enemies[i][0]+enemies[i][4]:
                                if bullets[n][1] >= enemies[i][1] and bullets[n][1] <= enemies[i][1]+enemies[i][4]/2:
                                    audioplay2 = threading.Thread(target=audiobombulletdef)
                                    audioplay2.start()
                                    enemies[i][3] -= damage
                                    bullets.remove(bullets[n])
                                    break
                            if bullets[n][1] >= enemies[i][1] and bullets[n][1] <= enemies[i][1]+enemies[i][4]/2:
                                if bullets[n][0] >= enemies[i][0] and bullets[n][0] <= enemies[i][0]+enemies[i][4]:
                                    audioplay2 = threading.Thread(target=audiobombulletdef)
                                    audioplay2.start()
                                    enemies[i][3] -= damage
                                    bullets.remove(bullets[n])
                                    break
                        except:
                            pass
            except:
                pass
        if life <= 0:
            booms.append([x, y, 2, 'pd'])
            time.sleep(2)
            run = False
        for i in range(0, len(enemies)):
            try:
                if enemies[i][0] > x:
                    enemies[i][0] -= speeden
                if enemies[i][0] < x:
                    enemies[i][0] += speeden
                if enemies[i][1] > y:
                    enemies[i][1] -= speeden
                if enemies[i][1] < y:
                    enemies[i][1] += speeden
            except:
                pass
        for bon in range(0, len(bonuses)):
            try:
                rastx2 = (bonuses[bon][0] - x) ** 2
                rasty2 = (bonuses[bon][1] - y) ** 2
                rast2 = math.sqrt(rastx2 + rasty2)
                if rast2 <= 35:
                    if bonuses[bon][2] == 'shield':
                        if isshield == True:
                            isshield2 = True
                            bonuses.remove(bonuses[bon])
                            hreadd6 = threading.Thread(target=timmer2)
                            hreadd6.start()
                        if isshield == False:
                            isshield = True
                            bonuses.remove(bonuses[bon])
                            hreadd6 = threading.Thread(target=timmer2)
                            hreadd6.start()
                    if bonuses[bon][2] == 'doublebullet':
                        if doublebullet == True:
                            doublebullet2 = True
                            bonuses.remove(bonuses[bon])
                            hreadd8 = threading.Thread(target=timmer3)
                            hreadd8.start()
                        if doublebullet == False:
                            doublebullet = True
                            bonuses.remove(bonuses[bon])
                            hreadd8 = threading.Thread(target=timmer3)
                            hreadd8.start()


            except:
                pass
        if y1 >= coords1y - 1 and y1 <= coords1y + 1:
            y1 = coords1y
        if y2 >= coords2y - 1 and y2 <= coords2y + 1:
            y2 = coords2y
        if y1 < coords1y:
            y1 += 0.2
        if y2 > coords2y:
            y2 -= 0.2
        if y1 > coords1y:
            y1 -= 0.2
        if y2 < coords2y:
            y2 += 0.2
        for bomenn in range(0, len(bomenemies)):
            try:
                if bomenemies[bomenn][3] == 'basa1' and lifebasa1 <= 0:
                    bomenemies[bomenn][3] = 'basa2'
                if bomenemies[bomenn][3] == 'basa2' and lifebasa2 <= 0:
                    bomenemies[bomenn][3] = 'basa1'
                if lifebasa1 <= 0 and lifebasa2 <= 0:
                    bomenemies.remove(bomenemies[bomenn])
                    bomsbomen.append([bomenemies[bomenn][0], bomenemies[bomenn][1], 0])
                    break
                if position == 'end' or position == 'start':
                    bomenemies.remove(bomenemies[bomenn])
                    bomsbomen.append([bomenemies[bomenn][0], bomenemies[bomenn][1], 0])
                    break
                if bomenemies[bomenn][3] == 'basa1':
                    ss1 = (x1 + 20 - bomenemies[bomenn][0]) ** 2
                    ss2 = (y1 + 40 - bomenemies[bomenn][1]) ** 2
                    ss3 = math.sqrt(ss1 + ss2)
                    if bomenemies[bomenn][0] < x1 + 20:
                        bomenemies[bomenn][0] += speedbomen
                    if bomenemies[bomenn][0] > x1 + 20:
                        bomenemies[bomenn][0] -= speedbomen
                    if bomenemies[bomenn][1] < y1 + 35:
                        bomenemies[bomenn][1] += speedbomen
                    if bomenemies[bomenn][1] > y1 + 35:
                        bomenemies[bomenn][1] -= speedbomen
                    if ss3 <= 40:
                        lifebasa1 -= 1
                        basabooms.append([x1, y1, 0])
                        bomsbomen.append([bomenemies[bomenn][0], bomenemies[bomenn][1], 0])
                        bomenemies.remove(bomenemies[bomenn])
                if bomenemies[bomenn][3] == 'basa2':
                    ss1 = (x2 + 20 - bomenemies[bomenn][0]) ** 2
                    ss2 = (y2 + 40 - bomenemies[bomenn][1]) ** 2
                    ss3 = math.sqrt(ss1 + ss2)
                    if bomenemies[bomenn][0] < x2 + 20:
                        bomenemies[bomenn][0] += speedbomen
                    if bomenemies[bomenn][0] > x2 + 20:
                        bomenemies[bomenn][0] -= speedbomen
                    if bomenemies[bomenn][1] < y2 + 35:
                        bomenemies[bomenn][1] += speedbomen
                    if bomenemies[bomenn][1] > y2 + 35:
                        bomenemies[bomenn][1] -= speedbomen
                    if ss3 <= 40:
                        lifebasa2 -= 1
                        basabooms.append([x2, y2, 0])
                        bomsbomen.append([bomenemies[bomenn][0], bomenemies[bomenn][1], 0])
                        bomenemies.remove(bomenemies[bomenn])
                if isblaster == True:
                    if bomenemies[bomenn][4] > 0:
                        cc1 = (xb + 10 - bomenemies[bomenn][0]+15) ** 2
                        cc2 = (yb + 10 - bomenemies[bomenn][1]+15) ** 2
                        cc3 = math.sqrt(cc1 + cc2)
                        if cc3 <= 40:
                            bomenemies[bomenn][4] -= 1
                    if bomenemies[bomenn][4] <= 0:
                        bomsbomen.append([bomenemies[bomenn][0], bomenemies[bomenn][1], 0])
                        bomenemies.remove(bomenemies[bomenn])
            except:
                pass
        if lifebasa1 <= 0 and canbigbasabom == True:
            canbigbasabom = False
            bigbasabom = True
            xbb = x1 - 190
            ybb = y1 - 60
            hreadd97 = threading.Thread(target=timerbigbasabom)
            hreadd97.start()
        if lifebasa2 <= 0 and canbigbasabom2 == True:
            canbigbasabom2 = False
            bigbasabom = True
            xbb = x2 - 190
            ybb = y2 - 60
            hreadd97 = threading.Thread(target=timerbigbasabom)
            hreadd97.start()
        if lifebasa1 <= 0 and lifebasa2 <= 0:
            time.sleep(2)
            run = False
        if points > needpoints and isbosslife == False and len(enemies) < 1:
            isbosslife = True
            bosslife = 100 + ((bosslevel - 1) * 10)
        if isbosslife == True and bosslife > 0:
            if xboss < x:
                xboss += speedboss
            if xboss > x:
                xboss -= speedboss
            if yboss < y:
                yboss += speedboss
            if yboss > y:
                yboss -= speedboss
            xmp = (x + 25 - xboss) ** 2
            ymp = (y + 25 - yboss) ** 2
            xymp = math.sqrt(xmp + ymp)
            if bossbomb == True:
                if bossbombx < x:
                    bossbombx += speedbossbomb
                if bossbombx > x:
                    bossbombx -= speedbossbomb
                if bossbomby < y:
                    bossbomby += speedbossbomb
                if bossbomby > y:
                    bossbomby -= speedbossbomb
                xmp3 = (x + 10 - bossbombx) ** 2
                ymp3 = (y + 10 - bossbomby) ** 2
                xymp3 = math.sqrt(xmp3 + ymp3)
                if xymp3 < 35:
                    audioplay3 = threading.Thread(target=audiobomanemmy)
                    audioplay3.start()
                    if isshield == True:
                        isshield = False
                    if isshield == False:
                        life -= 1
                    bombossbomb = True
                    bombossbombx = bossbombx - 5
                    bombossbomby = bossbomby - 5
                    hreaddbb2 = threading.Thread(target=bombossbomba)
                    hreaddbb2.start()
                    bossbomb = False
            if bossbomb == False and delaybossbomb == False:
                bossbomb = True
                delaybossbomb = True
                bossbombx = xboss
                bossbomby = yboss
                hreaddbb1 = threading.Thread(target=bossbomba)
                hreaddbb1.start()
            if xymp <= 70 and bossataka1 == False and delayataka1 == False:
                bossataka1 = True
                delayataka1 = True
                bossataka1x = x - 25
                bossataka1y = y - 25
                if isshield == True:
                    isshield = False
                if isshield == False:
                    life -= 1
                hreaddb1 = threading.Thread(target=bossatak1)
                hreaddb1.start()
            if xymp <= 500 and bossataka2 == False and delayataka2 == False and bossataka3 == False and delayataka3 == False:
                bossataka2 = True
                delayataka2 = True
                bossataka2x = x - 25
                bossataka2y = y - 25
                hreaddb2 = threading.Thread(target=bossatak2)
                hreaddb2.start()
            if bossataka2 == False and delayataka2 == True and bossataka3 == False and delayataka3 == False:
                bossataka3 = True
                delayataka3 = True
                xboss = bossataka2x + 50
                yboss = bossataka2y + 50
                xmp2 = (x + 25 - xboss) ** 2
                ymp2 = (y + 25 - yboss) ** 2
                xymp2 = math.sqrt(xmp2 + ymp2)
                bossataka3x = xboss - 100
                bossataka3y = yboss - 100
                hreaddb3 = threading.Thread(target=bossatak3)
                hreaddb3.start()
                if xymp2 <= 70:
                    life -= 1
            try:
                for bbull in range(0, len(bullets)):
                    if isbosslife == True:
                        ebanrast1 = (xboss - bullets[bbull][0]) ** 2
                        ebanrast2 = (yboss - bullets[bbull][1]) ** 2
                        ebanrast3 = math.sqrt(ebanrast1 + ebanrast2)
                        if ebanrast3 < 50:
                            audioplay2 = threading.Thread(target=audiobombulletdef)
                            audioplay2.start()
                            bullets.remove(bullets[bbull])
                            bosslife -= damage * 10
            except:
                pass
        if isbosslife == True and bosslife <= 0:
            deathboss = True
            deathbossx = xboss - 65
            deathbossy = yboss - 65
            hreaddb9 = threading.Thread(target=deathbossaa)
            hreaddb9.start()
            bosslevel += 1
            xboss = -50
            yboss = -50
            needpoints += 30
            if cdbossataka3 >= 1000:
                cdbossataka3 -= 500
            speedboss += 0.05
            isbosslife = False
            coords2y = (winheight / 2 + winheight) / 2 - 35
            coords1y = (winheight / 2 + 0) / 2 - 35
            qwerty1 = True
            qwerty2 = True
            hreadd99 = threading.Thread(target=timmerAnn2)
            hreadd99.start()
            hreadd5 = threading.Thread(target=timmerAnn)
            hreadd5.start()
            hreadd45 = threading.Thread(target=createmeteor)
            hreadd45.start()

def peremens():
    global lavel1
    global lavel2
    global lavel3
    global bosslevel
    global x
    global y
    global wight
    global height
    global radius
    global speed
    global speedb
    global speeden
    global side
    global back
    global side2
    global appcan
    global life
    global doublebullet
    global doublebullet2
    global points
    global needpoints
    global x2
    global y2
    global x1
    global y1
    global xb
    global yb
    global coords1x
    global coords2y
    global coords2x
    global coords1y
    global bosslife
    global gradus
    global isbosslife
    global xboss
    global yboss
    global stars
    global boomesmeteor
    global meteors
    global enemylife
    global senemylife
    global bomsbomen
    global bigbasabom
    global canbigbasabom
    global canbigbasabom2
    global xbb
    global ybb
    global bigbasabomCount
    global animCount
    global animCount2
    global shieldCount
    global basaCount
    global bullets
    global enemies
    global bomenemies
    global booms
    global bonuses
    global isshield
    global isshield2
    global qwerty1
    global qwerty2
    global position
    global basabooms
    global speedbomen
    global lifebasa1
    global lifebasa2
    global number
    global number2
    global isblaster
    global timeon
    global minerals
    global lifebomen
    global sideblaster
    global blasterCount
    global impact
    global dropedminerals
    global diamonds
    global gold
    global iron
    global needdiamonds
    global needgold
    global neediron
    global damage
    global timerbomen
    global timermen
    global starttimerbomen
    global starttimermen
    global dashx
    global dashy
    global dash
    global candash
    global dashtimes
    global bombax
    global isbomba
    global bombay
    global dashs
    global numbermeteorbomba
    global bossataka1
    global bossataka1x
    global bossataka1y
    global bossataka1Count
    global delayataka1
    global bossataka2
    global bossataka2x
    global bossataka2y
    global bossataka2Count
    global delayataka2
    global bossataka3
    global bossataka3x
    global bossataka3y
    global bossataka3Count
    global cdbossataka3
    global delayataka3
    global bossbomb
    global bossbombx
    global bossbomby
    global bossbombCount
    global delaybossbomb
    global speedbossbomb
    global bombossbomb
    global bombossbombx
    global bombossbomby
    global bombossbombCount
    global deathboss
    global deathbossx
    global deathbossy
    global deathbossCount
    global speedboss
    lavel1 = False
    lavel2 = False
    lavel3 = False
    bosslevel = 1
    x = winwidth / 2 - 51 / 2
    y = winheight / 2 - 51 / 2
    wight = 40
    height = 40
    radius = 30
    speed = 0.00
    speedb = 7
    speeden = 0.1
    side = [False, False, True, False, False, False, False, False]
    back = False
    side2 = []
    appcan = True
    life = 3
    doublebullet = False
    doublebullet2 = False
    points = 0  # ljanbdslkjfbnasdjklfbasdhbjklfahnbjksdfnbjkasncm,X>CNVm,n.zxcbnvlkhjabhdns;ja
    needpoints = 30
    x2 = winwidth / 2 - 35
    y2 = winheight + 75
    x1 = winwidth / 2 - 35
    y1 = -150
    xb = 0
    yb = 0
    coords1x = (winwidth) / 2 - 35
    coords2y = (winheight / 2 + winheight) / 2 - 35
    coords2x = (winwidth) / 2 - 35
    coords1y = (winheight / 2 + 0) / 2 - 35
    bosslife = 100
    gradus = 0
    isbosslife = False
    xboss = -50
    yboss = -50
    stars = []
    boomesmeteor = []
    meteors = []
    enemylife = 1
    senemylife = 2
    bomsbomen = []
    bigbasabom = False
    canbigbasabom = True
    canbigbasabom2 = True
    xbb = 0
    ybb = 0
    bigbasabomCount = 0
    animCount = 0
    animCount2 = 0
    shieldCount = 0
    basaCount = 0
    bullets = []
    enemies = []
    bomenemies = []
    booms = []
    bonuses = []
    isshield = False
    isshield2 = False
    qwerty1 = True
    qwerty2 = True
    position = 'start'
    basabooms = []
    speedbomen = 0.1
    lifebasa1 = 10
    lifebasa2 = 10
    number = 0
    number2 = 2
    isblaster = False
    timeon = [1000, 1000, 1000]
    minerals = [['d', 'i', 'd', 'em'], ['i', 'i', 'i', 'g', 'd'], ['g', 'i', 'g', 'em']]
    lifebomen = 100
    sideblaster = 'up'
    blasterCount = 0
    impact = 0
    dropedminerals = []
    diamonds = 2
    gold = 3
    iron = 4
    needdiamonds = 2
    needgold = 3
    neediron = 5
    damage = 1
    timerbomen = 13
    timermen = 3
    starttimerbomen = 20
    starttimermen = 5
    dashx = 0
    dashy = 0
    dash = 150
    candash = True
    dashtimes = 2
    bombax = 0
    isbomba = False
    bombay = 0
    dashs = []
    numbermeteorbomba = 0
    bossataka1 = False
    bossataka1x = 0
    bossataka1y = 0
    bossataka1Count = 2
    delayataka1 = False
    bossataka2 = False
    bossataka2x = 0
    bossataka2y = 0
    bossataka2Count = 1
    delayataka2 = False
    bossataka3 = False
    bossataka3x = 0
    bossataka3y = 0
    bossataka3Count = 4
    cdbossataka3 = 3000
    delayataka3 = False
    bossbomb = False
    bossbombx = 0
    bossbomby = 0
    bossbombCount = 0
    delaybossbomb = False
    speedbossbomb = 0.3
    bombossbomb = False
    bombossbombx = 0
    bombossbomby = 0
    bombossbombCount = 0
    deathboss = False
    deathbossx = 0
    deathbossy = 0
    deathbossCount = 0
    speedboss = 0.15
def potoks():
    for i in range(0, 20):
        xs = random.randint(20, winwidth - 80)
        ys = random.randint(20, winheight - 80)
        sp = random.choice(spritesstars)
        stars.append([xs, ys, 0, sp])
    hreadd10 = threading.Thread(target=positionbasa)
    hreadd10.start()
    hreadd99 = threading.Thread(target=timmerAnn2)
    hreadd99.start()
    hreadd98 = threading.Thread(target=anc1t2)
    hreadd98.start()
    hreadd90 = threading.Thread(target=anc1t3)
    hreadd90.start()
    hreadd11 = threading.Thread(target=anc3)
    hreadd11.start()
    hreadd22 = threading.Thread(target=createmeteor)
    hreadd22.start()
    hreadd225 = threading.Thread(target=timmer4)
    hreadd225.start()
    hreadd245 = threading.Thread(target=sstars)
    hreadd245.start()
    hreadd235 = threading.Thread(target=timmer5)
    hreadd235.start()
    hreadd224 = threading.Thread(target=dashtimer)
    hreadd224.start()
    hreadd5 = threading.Thread(target=timmerAnn)
    hreadd5.start()
    hreadd2 = threading.Thread(target=hello2)
    hreadd2.start()
    hreadd3 = threading.Thread(target=ac)
    hreadd3.start()
    hreadd4 = threading.Thread(target=anc2)
    hreadd4.start()
    hreadd = threading.Thread(target=hello)
    hreadd.start()
while runn:
    pygame.time.delay(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            runn = False
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if run == False and keys[pygame.K_r]:
        peremens()
        run = True
        potoks()
        winn1 = False
        winn2 = False
    if run == False and keys[pygame.K_ESCAPE]:
        runn = False
    win.fill((0, 0, 40))
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                runn = False
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False
        if points > 25 and lavel1 == False:
            lavel1 = True
            speeden += 0.1
            speedbomen += 0.05
        if points > 50 and lavel2 == False:
            lavel2 = True
            speeden += 0.1
            speedbomen += 0.05
        if points > 75 and lavel3 == False:
            lavel3 = True
            speeden += 0.1
            speedbomen += 0.05
        if life >= 3:
            number2 = 2
        if life == 2:
            number2 = 1
        if life == 1:
            number2 = 0
        if life <= 0:
            number2 = 3
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
        if keys[pygame.K_s]:
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
        if keys[pygame.K_d] and keys[pygame.K_s]:
            for i in range(0, 8):
                side[i] = False
            side[7] = True
        if keys[pygame.K_u] and candash == True and dashtimes > 0:
            audioplay5 = threading.Thread(target=playblinkaudio)
            audioplay5.start()
            dashs.append([x, y, 7, '1'])
            dashs.append([dashx, dashy, 7, '2'])
            dashtimes -= 1
            candash = False
            x = dashx
            y = dashy
        if keys[pygame.K_t]:
            if appcan == True:
                audioplay1 = threading.Thread(target=audiobulletdef)
                audioplay1.start()
                if doublebullet != True:
                    impact += 0.1
                if side[0] == True:
                    if doublebullet == True:
                        bullets.append([x, y+20, -speedb, 'x'])
                        bullets.append([x + 51, y + 20, speedb, 'x'])
                    if doublebullet == False:
                        bullets.append([x, y + 20, -speedb, 'x'])
                if side[1] == True:
                    if doublebullet == True:
                        bullets.append([x, y + 20, -speedb, 'x'])
                        bullets.append([x+51, y+20, speedb, 'x'])
                    if doublebullet == False:
                        bullets.append([x+51, y+20, speedb, 'x'])
                if side[2] == True:
                    if doublebullet == True:
                        bullets.append([x+20, y+51, -speedb, 'y'])
                        bullets.append([x + 20, y, speedb, 'y'])
                    if doublebullet == False:
                        bullets.append([x + 20, y + 51, -speedb, 'y'])
                if side[3] == True:
                    if doublebullet == True:
                        bullets.append([x+20, y, speedb, 'y'])
                        bullets.append([x + 20, y + 51, -speedb, 'y'])
                    if doublebullet == False:
                        bullets.append([x+20, y, speedb, 'y'])
                if side[4] == True:
                    if doublebullet == True:
                        bullets.append([x, y, -speedb, 'xy', -speedb])
                        bullets.append([x + 51, y + 51, speedb, 'xy', speedb])
                    if doublebullet == False:
                        bullets.append([x, y, -speedb, 'xy', -speedb])
                if side[5] == True:
                    if doublebullet == True:
                        bullets.append([x, y+51, -speedb, 'xy', speedb])
                        bullets.append([x + 51, y, speedb, 'xy', -speedb])
                    if doublebullet == False:
                        bullets.append([x, y + 51, -speedb, 'xy', speedb])
                if side[6] == True:
                    if doublebullet == True:
                        bullets.append([x+51, y, speedb, 'xy', -speedb])
                        bullets.append([x, y + 51, -speedb, 'xy', speedb])
                    if doublebullet == False:
                        bullets.append([x + 51, y, speedb, 'xy', -speedb])
                if side[7] == True:
                    if doublebullet == True:
                        bullets.append([x+51, y+51, speedb, 'xy', speedb])
                        bullets.append([x, y, -speedb, 'xy', -speedb])
                    if doublebullet == False:
                        bullets.append([x + 51, y + 51, speedb, 'xy', speedb])
                appcan = False
                hreadd7 = threading.Thread(target=timmer)
                hreadd7.start()
        if keys[pygame.K_y]:
            audioplay4 = threading.Thread(target=playblasteraudio)
            audioplay4.start()
            isblaster = True
        if not keys[pygame.K_y]:
            isblaster = False

        if x >= winwidth + 20:
            x = -10
        if x <= -20:
            x = winwidth + 10
        if y >= winheight + 15:
            y = -10
        if y <= -20:
            y = winheight + 5
        win.fill((0, 0, 40))
        for st2 in range(0, len(stars)):
            win.blit(stars[st2][3][stars[st2][2]], (stars[st2][0], stars[st2][1]))
        for min in range(0, len(dropedminerals)):
            win.blit(dropedmineralssprites[dropedminerals[min][0]], (dropedminerals[min][1], dropedminerals[min][2]))
        for met in range(0, len(meteors)):
            try:
                win.blit(spritesmeteor[meteors[met][2]], (meteors[met][0], meteors[met][1]))
            except:
                pass
        if isbomba == True:
            win.blit(spritesbomba[animCount2], (bombax, bombay))
        for bmm2 in range(0, len(boomesmeteor)):
            try:
                win.blit(spritesboommeteor[boomesmeteor[bmm2][3]][boomesmeteor[bmm2][2]], (boomesmeteor[bmm2][0], boomesmeteor[bmm2][1]))
            except:
                pass
        for i in range(0, len(bullets)):
            try:
                if bullets[i][3] == 'x':
                    win.blit(spritesBUL[animCount2], (bullets[i][0], bullets[i][1]))
                    bullets[i][0] += bullets[i][2]
                if bullets[i][3] == 'y':
                    win.blit(spritesBUL[animCount2], (bullets[i][0], bullets[i][1]))
                    bullets[i][1] += bullets[i][2]
                if bullets[i][3] == 'xy':
                    win.blit(spritesBUL[animCount2], (bullets[i][0], bullets[i][1]))
                    bullets[i][0] += bullets[i][2]
                    bullets[i][1] += bullets[i][4]
            except:
                pass
        for z in range(0, len(enemies)):
            try:
                if enemies[z][2] == 'Super':
                    win.blit(spritessuperenemies[animCount2], (enemies[z][0], enemies[z][1]))
                if enemies[z][2] == 'None':
                    win.blit(spritesenemies[animCount2], (enemies[z][0], enemies[z][1]))
            except:
                pass
        if isbosslife == True:
            win.blit(spritesboss[animCount2], (xboss - 50, yboss - 50))
        for bonnus in range(0, len(bonuses)):
            try:
                if bonuses[bonnus][2] == 'shield':
                    win.blit(spritesbonus[0], (bonuses[bonnus][0], bonuses[bonnus][1]))
                if bonuses[bonnus][2] == 'doublebullet':
                    win.blit(spritesbonus[1], (bonuses[bonnus][0], bonuses[bonnus][1]))
            except:
                pass

        for bom in range(0, len(booms)):
            try:
                if len(booms[bom]) == 4:
                    win.blit(spritespd[animCount2], (booms[bom][0], booms[bom][1]))
                else:
                    win.blit(spritesboom[animCount2], (booms[bom][0], booms[bom][1]))
            except:
                pass

        if isshield == True:
            win.blit(spriteshield[shieldCount], (x-15, y-10))

        for bomenn2 in range(0, len(bomenemies)):
            try:
                win.blit(spritesbomen[bomenemies[bomenn2][2]][animCount2], (bomenemies[bomenn2][0], bomenemies[bomenn2][1]))
            except:
                pass
        if bossataka2 == True:
            try:
                win.blit(spritesataka2[bossataka2Count], (bossataka2x, bossataka2y))
            except:
                pass
        if bossataka3 == True:
            try:
                win.blit(spritesataka3[bossataka3Count], (bossataka3x, bossataka3y))
            except:
                pass
        if bossbomb == True:
            try:
                win.blit(spritesbossbomb[bossbombCount], (bossbombx, bossbomby))
            except:
                pass
        if bombossbomb == True:
            try:
                win.blit(spritesbombossbomb[bombossbombCount], (bombossbombx, bombossbomby))
            except:
                pass
        if deathboss == True:
            try:
                win.blit(spritesdeathboss[deathbossCount], (deathbossx, deathbossy))
            except:
                pass
        if life > 0:
            drawpers()
        if bossataka1 == True:
            try:
                win.blit(spritesataka1[bossataka1Count], (bossataka1x, bossataka1y))
            except:
                pass
        for ddash2 in range(0, len(dashs)):
            try:
                win.blit(spritesdash[dashs[ddash2][3]][dashs[ddash2][2]], (dashs[ddash2][0], dashs[ddash2][1]))
            except:
                pass


        if isblaster == True:
            try:
                win.blit(spritesblaster[sideblaster][blasterCount], (xb, yb))
            except:
                pass
        for bben2 in range(0, len(bomsbomen)):
            try:
                win.blit(spritesbombomen[bomsbomen[bben2][2]], (bomsbomen[bben2][0], bomsbomen[bben2][1]))
            except:
                pass
        if lifebasa1 > 0:
            win.blit(spritesbasa2[position][basaCount], (x1, y1))
        if lifebasa2 > 0:
            win.blit(spritesbasa[position][basaCount], (x2, y2))
        if winn1 == True:
            win.blit(defencesprites[defenceCount], (x1 - 30, y1 - 30))
            win.blit(defencesprites[defenceCount], (x2 - 30, y2 - 30))
        for bbom1t1 in range(0, len(basabooms)):
            try:
                win.blit(spritesboombasat1[basabooms[bbom1t1][2]], (basabooms[bbom1t1][0], basabooms[bbom1t1][1]))
            except:
                pass
        if bigbasabom == True:
            win.blit(spritesbigbasabom[bigbasabomCount], (xbb, ybb))
        drawnumbers(str(points), 50, 10)
        drawnumbers(str(bosslevel), winwidth - 70, 10)
        drawnumbers(str(iron), winwidth/2 + 100, 10)
        drawnumbers(str(gold), winwidth/2 + 150, 10)
        drawnumbers(str(diamonds), winwidth/2 + 200, 10)
        drawnumbers(str(neediron), winwidth/2 + 100, 40)
        drawnumbers(str(needgold), winwidth/2 + 150, 40)
        drawnumbers(str(needdiamonds), winwidth/2 + 200, 40)
        win.blit(spriteslife[number2], (winwidth/2 - 75, 5))
print(points)
pygame.quit()