from random import *
import os
import pygame
import time
import random
import math
import glob
import json

pygame.init()

screenWidth = 1920
screenHeight = 1080
screenDisp = ((screenWidth - 800)/2, (screenHeight - 600)/2)

image = pygame.image.load("itemSprites/hat.png")
pygame.display.set_icon(image)

gameDisplay = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Spurrs')
clock = pygame.time.Clock()

infoObject = pygame.display.Info()
pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.HWSURFACE)

playerSprites = [pygame.image.load("charSprites/player1.png"), pygame.image.load("charSprites/player1-1.png"), pygame.image.load("charSprites/player1-2.png"), pygame.image.load("charSprites/player2.png"), pygame.image.load("charSprites/player2-1.png"), pygame.image.load("charSprites/player2-2.png"), pygame.image.load("charSprites/player3.png"), pygame.image.load("charSprites/player3-1.png"), pygame.image.load("charSprites/player3-2.png"), pygame.image.load("charSprites/player4.png"), pygame.image.load("charSprites/player4-1.png"), pygame.image.load("charSprites/player4-2.png")]
horseSprites = [pygame.image.load("charSprites/horse1L.png"), pygame.image.load("charSprites/horse1L-1.png"), pygame.image.load("charSprites/horse1L-2.png"), pygame.image.load("charSprites/horse1R.png"), pygame.image.load("charSprites/horse1R-1.png"), pygame.image.load("charSprites/horse1R-2.png"), pygame.image.load("charSprites/horsedie1-1.png"), pygame.image.load("charSprites/horsedie1-2.png"), pygame.image.load("charSprites/horsedie1-3.png"), pygame.image.load("charSprites/horse1Dead.png")]
wolfSprites = [pygame.image.load("charSprites/wolf1.png"), pygame.image.load("charSprites/wolf1-1.png"), pygame.image.load("charSprites/wolf1-2.png"), pygame.image.load("charSprites/wolf2.png"), pygame.image.load("charSprites/wolf2-1.png"), pygame.image.load("charSprites/wolf2-2.png"), pygame.image.load("charSprites/wolfdie1-1.png"), pygame.image.load("charSprites/wolfdie1-2.png"), pygame.image.load("charSprites/wolfdie1-3.png"), pygame.image.load("charSprites/wolfdead.png") ]
hawkSprites = [pygame.image.load("charSprites/hawk1.png"), pygame.image.load("charSprites/hawk1-1.png"), pygame.image.load("charSprites/hawk1-2.png"), pygame.image.load("charSprites/hawkFall.png"), pygame.image.load("charSprites/hawkDead.png")]
npcSprites = [[pygame.image.load("charSprites/npc1-U.png"), pygame.image.load("charSprites/npc1-R.png"), pygame.image.load("charSprites/npc1-D.png"), pygame.image.load("charSprites/npc1-L.png"), pygame.image.load("charSprites/npc1Dead.png")], [pygame.image.load("charSprites/npc2-U.png"), pygame.image.load("charSprites/npc2-R.png"), pygame.image.load("charSprites/npc2-D.png"), pygame.image.load("charSprites/npc1-L.png"), pygame.image.load("charSprites/npc2Dead.png")], [pygame.image.load("charSprites/npc3-U.png"), pygame.image.load("charSprites/npc3-R.png"), pygame.image.load("charSprites/npc3-D.png"), pygame.image.load("charSprites/npc3-L.png"), pygame.image.load("charSprites/npc3Dead.png")], [pygame.image.load("charSprites/npc4-U.png"), pygame.image.load("charSprites/npc4-R.png"), pygame.image.load("charSprites/npc4-D.png"), pygame.image.load("charSprites/npc4-L.png"), pygame.image.load("charSprites/npc4Dead.png")], [pygame.image.load("charSprites/npc5-U.png"), pygame.image.load("charSprites/npc5-R.png"), pygame.image.load("charSprites/npc5-D.png"), pygame.image.load("charSprites/npc5-L.png"), pygame.image.load("charSprites/npc5Dead.png")], [pygame.image.load("charSprites/npc6-U.png"), pygame.image.load("charSprites/npc6-R.png"), pygame.image.load("charSprites/npc6-D.png"), pygame.image.load("charSprites/npc6-L.png"), pygame.image.load("charSprites/npc6Dead.png")], [pygame.image.load("charSprites/npc7-U.png"), pygame.image.load("charSprites/npc7-R.png"), pygame.image.load("charSprites/npc7-D.png"), pygame.image.load("charSprites/npc7-L.png"), pygame.image.load("charSprites/npc7Dead.png")], [pygame.image.load("charSprites/npc8-U.png"), pygame.image.load("charSprites/npc8-R.png"), pygame.image.load("charSprites/npc8-D.png"), pygame.image.load("charSprites/npc8-L.png"), pygame.image.load("charSprites/npc8Dead.png")], [pygame.image.load("charSprites/npc9-U.png"), pygame.image.load("charSprites/npc9-R.png"), pygame.image.load("charSprites/npc9-D.png"), pygame.image.load("charSprites/npc9-L.png"), pygame.image.load("charSprites/npc9Dead.png")]]
hats = [pygame.image.load("itemSprites/Akobra Hat.png"), pygame.image.load("itemSprites/Leather Hat.png"), pygame.image.load("itemSprites/Bowler Hat.png"), pygame.image.load("itemSprites/Top Hat.png"), pygame.image.load("itemSprites/Rough Hat.png")]
paintSprites = [pygame.image.load("particleSprites/p1.png"), pygame.image.load("particleSprites/p2.png"), pygame.image.load("particleSprites/p3.png"), pygame.image.load("particleSprites/p4.png"), pygame.image.load("particleSprites/p5.png"), pygame.image.load("particleSprites/p6.png"), pygame.image.load("particleSprites/p7.png"), pygame.image.load("particleSprites/p8.png"), pygame.image.load("particleSprites/p9.png"), pygame.image.load("particleSprites/p10.png"), pygame.image.load("particleSprites/p11.png"), pygame.image.load("particleSprites/p12.png"), pygame.image.load("particleSprites/p13.png"), pygame.image.load("particleSprites/p14.png"), pygame.image.load("particleSprites/p15.png"), pygame.image.load("particleSprites/p16.png"), pygame.image.load("particleSprites/p17.png"), pygame.image.load("particleSprites/p18.png"), pygame.image.load("particleSprites/p19.png"), pygame.image.load("particleSprites/p20.png"), pygame.image.load("particleSprites/p21.png"), pygame.image.load("particleSprites/p22.png"), pygame.image.load("particleSprites/p23.png"), pygame.image.load("particleSprites/p24.png"), pygame.image.load("particleSprites/p25.png"), pygame.image.load("particleSprites/p26.png"), pygame.image.load("particleSprites/p27.png"), pygame.image.load("particleSprites/p28.png"), pygame.image.load("particleSprites/p29.png"), pygame.image.load("particleSprites/p30.png"), pygame.image.load("particleSprites/p31.png"), pygame.image.load("particleSprites/p32.png"), pygame.image.load("particleSprites/p33.png"), pygame.image.load("particleSprites/p34.png"), pygame.image.load("particleSprites/p35.png")]
expSprites = [pygame.image.load("particleSprites/exp1-1.png"), pygame.image.load("particleSprites/exp1-2.png"), pygame.image.load("particleSprites/exp1-3.png"), pygame.image.load("particleSprites/exp1-4.png"), pygame.image.load("particleSprites/exp1-5.png"), pygame.image.load("particleSprites/exp1-6.png"), pygame.image.load("particleSprites/exp1-7.png"), pygame.image.load("particleSprites/exp1-8.png"), pygame.image.load("particleSprites/exp1-9.png"), pygame.image.load("particleSprites/exp1-10.png"), pygame.image.load("particleSprites/exp1-11.png"), pygame.image.load("particleSprites/exp1-12.png"), pygame.image.load("particleSprites/exp2-1.png"), pygame.image.load("particleSprites/exp2-2.png"), pygame.image.load("particleSprites/exp2-3.png"), pygame.image.load("particleSprites/exp2-4.png"), pygame.image.load("particleSprites/exp2-5.png"), pygame.image.load("particleSprites/exp2-6.png"), pygame.image.load("particleSprites/exp2-7.png"), pygame.image.load("particleSprites/exp2-8.png"), pygame.image.load("particleSprites/exp2-9.png"), pygame.image.load("particleSprites/exp2-10.png"), pygame.image.load("particleSprites/exp2-11.png"), pygame.image.load("particleSprites/exp2-12.png")]
tntSprites = [pygame.image.load("itemSprites/DynamiteFuse1.png"), pygame.image.load("itemSprites/DynamiteFuse2.png")]
wanted = pygame.image.load("tileSprites/wanted.png")
xTrans = 0
yTrans = 0

tileSprites = [pygame.image.load("tileSprites/dirt.png")]

mapWidth = 10
mapHeight = 10
objNum = 15
objList = []
objDelList = []
bulletList = []
delList = []
charList = []
charDelList = []

filePlaying = "maps/map.json"
screenQuadX = []
screenQuadY = []
screenObjects = []
screenObjX = []
screenObjY = []
screenImg = []
screenDimX = []
screenDimY = []

exp = False
explosions = []
expDel = []

collNum = []
collTrue = False
collItems = []
collTime = []
collDel = []
invItems = []
invNum = []

gameExit = False
menuExit = False
gamePlay = False
settingsExit = True

class Player:
    def __init__(self):
        self.direction = "null"
        self.x = screenWidth/2
        self.y = screenHeight/2
        self.quadX = mapWidth / 2
        self.quadY = mapHeight / 2
        self.xDisp = 0
        self.yDisp = 0
        self.step = 0
        self.walkL = [0, 0, 0, 0]
        self.width = 30
        self.height = 40
        self.health = 30
        self.horseMounted = 0
        self.spriteDisplay = 3
        self.state = "normal"
        self.configure()

    def configure(self):
        with open("charSprites/player.json", "r") as jsonFile:
            data = json.load(jsonFile)
        self.pistol = data[0]["gun"]
        self.hat = data[0]["hat"]
        self.vest = data[0]["vest"]
        self.spurrs = data[0]["spurrs"]
    
    def inventory(self, item, num):
        print("player inv")
        global collTrue
        
        collItems.append(str(item))
        collTime.append(200 + (len(collItems)*50))
        collNum.append(str(num))
        if len(collItems) > 5:
            collItems.pop(0)
            collTime.pop(0)
            collNum.pop(0)
        collTrue = True
        with open("charSprites/player.json", "r") as jsonFile:
            data = json.load(jsonFile)
        for n in range(0, num):
            data[0]["items"].append(item)
        with open('charSprites/player.json', 'w') as outfile:  
            json.dump(data, outfile)
            
    def walk(self):
        if random.randint(0,40) == 10:
            if self.spurrs == "Spurrs o' 'Splodin":
                explosion = Explosion(random.randint(0, 800)+screenDisp[0], random.randint(0,600)+screenDisp[1], 100, "small")
                explosions.append(explosion)
        if random.randint(0, 20) == 10:
            if self.spurrs == "Spurrs o' Hue":
                screenQuadX.append(player.quadX)
                screenQuadY.append(player.quadY)
                screenObjects.append("paint")
                screenObjX.append(player.x+20+player.xDisp)
                screenObjY.append(player.y+20+player.yDisp)
                screenImg.append(paintSprites[random.randint(0, 34)])
                screenDimX.append(0)
                screenDimY.append(0)
        if self.step >= 20 and self.state != "mounted":
            self.step = 0
            if self.direction == "up":
                if self.spriteDisplay == 1:
                    self.spriteDisplay = 2
                else:
                    self.spriteDisplay = 1
            elif self.direction == "right":
                if self.spriteDisplay == 4:
                    self.spriteDisplay = 5
                else:
                    self.spriteDisplay = 4
            elif self.direction == "down":
                if self.spriteDisplay == 7:
                    self.spriteDisplay = 8
                else:
                    self.spriteDisplay = 7
            elif self.direction == "left":
                if self.spriteDisplay == 10:
                    self.spriteDisplay = 11
                else:
                    self.spriteDisplay = 10
        else:
            self.step += 1

    def update(self):
        if self.health <= 0:
            self.state = "dead"

class Bullet:
    def __init__(self,x,y, speedX, speedY, owner):
        self.direction = "null"
        self.x = x
        self.y = y
        self.owner = owner
        self.speedX = speedX
        self.speedY = speedY
        
    def update(self):
        self.x += self.speedX
        self.y += self.speedY
        self.collide()

    def collide(self):
        for j in range(0, len(objList)):
            if self.x > objList[j].x - player.xDisp and self.x < objList[j].x -player.xDisp + objList[j].width and self.y > objList[j].y - player.yDisp and self.y < objList[j].y - player.yDisp + objList[j].height:
                if objList[j].type != "Dynamite":
                    if objList[j].state != "mounted" and objList[j].state != "dead":
                        delList.append(i)
                        objList[j].health -= 10
        for j in range(0, len(charList)):
            if self.owner != j:
                if self.x > charList[j].x-player.xDisp and self.x < charList[j].x-player.xDisp + charList[j].width and self.y+15 > charList[j].y-player.yDisp and self.y < charList[j].y-player.yDisp + charList[j].height:
                    print("hit")
                    if charList[j].state != "dead" and self.owner != j:
                        delList.append(i)
                        if len(charList) > j:
                            charList[j].health -= 10
        if self.owner != "player":
            if self.x > player.x and self.x < player.x + player.width and self.y > player.y and self.y < player.y + player.height:
                print("HTI PLAYER")
                delList.append(i)
                player.health -= 10

class Explosion:
    def __init__(self, x, y, size, typ):
        self.x = x
        self.y = y
        self.type = typ
        self.size = size
        self.spriteDisplay = 0
        self.time = 0
        self.val = 0

    def combust(self):
        for j in range(0, len(charList)):
            if charList[j].x > self.x and charList[j].x < self.x+self.size and charList[j].y > self.y and charList[j].y < self.y+self.size or self.x > charList[j].x and self.x < charList[j].x+charList[j].width and self.y > charList[j].y and self.y < charList[j].y+charList[j].height:
                charList[j].health -= 50
                if charList[j].x > self.x:
                    charList[j].x += 3
                else:
                    charList[j].x -= 3
                if charList[j].y > self.y:
                    charList[j].y += 3
                else:
                    charList[j].y -= 3
        for j in range(0, len(objList)):
            if objList[j].type != "Dynamite":
                if objList[j].x > self.x and objList[j].x < self.x+self.size and objList[j].y > self.y and objList[j].y < self.y+self.size or self.x > objList[j].x and self.x < objList[j].x+objList[j].width and self.y > objList[j].y and self.y < objList[j].y+objList[j].height:
                    objList[j].health -= 50
                    if objList[j].x > self.x:
                        objList[j].x += 3
                    else:
                        objList[j].x -= 3
                    if objList[j].y > self.y:
                        objList[j].y += 3
                    else:
                        objList[j].y -= 3
#        if player.x > self.x and player.x < self.x+self.size and player.y > self.y and player.y < self.y+self.size or self.x > player.x and self.x < player.x+player.width and self.y > player.y and self.y < player.y+player.height:
#            player.health -= 50
#            if player.x > self.x:
#                player.x += 3
#                player.xDisp += 3
#            else:
#                player.x -= 3
#                player.xDisp -= 3
#            if player.y > self.y:
#                player.y += 3
#                player.yDisp += 3
#            else:
#                player.y -= 3
#                player.yDisp -= 3
                    
    def update(self):
        if self.time > 10:
            self.val += 1
            if self.type == "big" and random.randint(0, 2) == 1:
                explosion = Explosion(self.x+random.randint(-self.size/2, self.size/2), self.y+random.randint(-self.size/2, self.size/2), 100, "small")
                explosions.append(explosion)
            self.time = 0
            if self.spriteDisplay < 11:
                self.spriteDisplay += 1
            else:
                expDel.append(i)
        else:
            self.time += 1
        if self.val > 10:
            expDel.append(i)
        self.combust()
        self.display()
        
    def display(self):
        if self.type == "big":
            image = pygame.transform.scale(expSprites[11+self.spriteDisplay], (self.size, self.size))
        else:
            image = pygame.transform.scale(expSprites[self.spriteDisplay], (110, 86))
        gameDisplay.blit(image, (self.x-player.xDisp, self.y-player.yDisp))

class Dynamite:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.type = "Dynamite"
        self.width = 55
        self.height = 55
        self.state = "null"
        self.size = size
        self.time = 500
        self.flip = 50
        self.spriteDisplay = 0
        self.expTrue = False
        
    def explode(self):
        explosion = Explosion(self.x-60, self.y-60, 120, "big")
        explosions.append(explosion)
        objDelList.append(i)
    
    def update(self):
        if self.time > 0:
            self.time -= 1
            if self.flip == 0:
                self.flip = 50
                if self.spriteDisplay == 0:
                    self.spriteDisplay = 1
                else:
                    self.spriteDisplay = 0
            else:
                self.flip -= 1
        elif self.expTrue == False:
            self.explode()
            self.expTrue = True
                          
class Wolf:
    def __init__(self,x,y,typ):
        self.direction = "null"
        self.x = x
        self.y = y
        self.attack = False
        self.type = typ
        self.looted = False
        self.speedX = 0
        self.speedY = 0
        self.time = 0
        self.step = 0
        self.prey = -1
        self.width = 48
        self.height = 29
        self.state = "wild"
        self.health = 5
        self.items = ["Tooth", "Fur", "Meat"]
        self.back = False
        self.spriteDisplay = 0
        
    def interact(self):
        if self.looted == False and self.state == "dead":
            if (player.x > self.x - player.xDisp and player.x < self.x - player.xDisp + 95 and player.y > self.y - player.yDisp and player.y < self.y - player.yDisp + 81 or self.x-player.xDisp > player.x-50 and self.x-player.xDisp < player.x+50 and self.y-player.yDisp > player.y-50 and self.y-player.yDisp < player.y+50):
                for k in range(0, random.randint(0,3)):
                    player.inventory(self.items[random.randint(0, len(self.items)-1)], random.randint(1,3))
                    self.looted = True
                    
    def pursue(self):
        #if len(charList)-1 > self.prey:
        #    vic = charList[self.prey]
        #else:
        vic = player
        if vic.state != "mounted":
            distance = math.sqrt(((int(vic.x-(self.x-player.xDisp)))*(int(vic.x-(self.x-player.xDisp))))+((int(vic.y-(self.y-player.yDisp)))*(int(vic.y-(self.y-player.yDisp)))))
            if distance > 100:
                if (self.x-player.xDisp < vic.x):
                    self.x += 1
                    self.direction = "right"
                if (self.x-player.xDisp > vic.x):
                    self.x -= 1
                    self.direction = "left"
                if (self.y-player.yDisp < vic.y):
                    self.y += 1
                if (self.y-player.yDisp > vic.y):
                    self.y -= 1
            elif distance < 101 and distance > 5:
                self.speedX = 0
                self.speedY = 0
                if xTrans == 0 and yTrans == 0:
                    if self.step >= 5:
                        self.step = 0
                        if (self.x-player.xDisp < vic.x):
                            self.x += 1
                            self.direction = "right"
                        if (self.x-player.xDisp > vic.x):
                            self.x -= 1
                            self.direction = "left"
                        if (self.y-player.yDisp < vic.y):
                            self.y += 1
                        if (self.y-player.yDisp > vic.y):
                            self.y -= 1
                    else:
                        self.step += 1
                else:
                    if (self.x-player.xDisp < vic.x):
                        self.x += 2
                        self.direction = "right"
                    if (self.x-player.xDisp > vic.x):
                        self.x -= 2
                        self.direction = "left"
                    if (self.y-player.yDisp < vic.y):
                        self.y += 2
                    if (self.y-player.yDisp > vic.y):
                        self.y -= 2
            elif distance < 6:
                self.bite(vic)
        else:
            if xTrans == 0 and yTrans == 0:
                distance = math.sqrt(((int(player.x-(self.x-player.xDisp)))*(int(player.x-(self.x-player.xDisp))))+((int(player.y-(self.y-player.yDisp)))*(int(player.y-(self.y-player.yDisp)))))
                if distance < 6:
                    self.bite(player)
                if self.step >= 5:
                    self.step = 0
                    if (self.x-player.xDisp < player.x):
                        self.x += 1
                        self.direction = "right"
                    if (self.x-player.xDisp > player.x):
                        self.x -= 1
                        self.direction = "left"
                    if (self.y-player.yDisp < player.y):
                        self.y += 1
                    if (self.y-player.yDisp > player.y):
                        self.y -= 1
                else:
                    self.step += 1
                
            else:
                if (self.x-player.xDisp-50 < player.x):
                    self.x += 2
                    self.direction = "right"
                if (self.x-player.xDisp-50 > player.x):
                    self.x -= 2
                    self.direction = "left"
                if (self.y-player.yDisp+random.randint(90,110) < player.y):
                    self.y += 2
                if (self.y-player.yDisp-random.randint(90,110) > player.y):
                    self.y -= 2

    def bite(self, vic):
        if player.state != "mounted":
            if (self.x-player.xDisp > vic.x and self.x-player.xDisp < vic.x+vic.width and self.y-player.yDisp > vic.y and self.y-player.yDisp < vic.y+vic.height):
                vic.health -= 3
                print(vic)
            if (vic.x > self.x-player.xDisp and vic.x < self.x-player.xDisp+self.width and vic.y > self.y-player.yDisp and vic.y < self.y-player.yDisp+self.height):
                vic.health -= 3
                print(vic)
        else:
            if objList[player.horseMounted].health > 3:
                objList[player.horseMounted].health -= 3
            else:
                player.state = "normal"
                objList[player.horseMounted].state = "wild"
                objList[player.horseMounted].x = 400
                objList[player.horseMounted].y = 300
                objList[player.horseMounted].health -= 3
            
    def die(self):
        if self.step >= 20:
            self.step = 0
            if self.spriteDisplay > -1 and self.spriteDisplay < 6:
                self.spriteDisplay = 6
            elif self.spriteDisplay == 6:
                self.spriteDisplay =7
            elif self.spriteDisplay == 7:
                self.spriteDisplay = 8
            elif self.spriteDisplay == 8:
                self.state = "dead"
                self.spriteDisplay = 9
                for j in range(0, len(charList)):
                    if self.prey == j:
                        charList[j].hunter = -1
                        charList[j].chased = False
                        self.prey = -1
                        self.attack = False
                        
        else:
            self.step += 1
            
    def feed(self, vic):
        distance = math.sqrt(((int(vic.x-self.x))*(int(vic.x-self.x)))+((int(vic.y-self.y))*(int(vic.y-self.y))))
        if (distance > 40):
            if (self.x-player.xDisp < vic.x-player.xDisp):
                self.x += 1
                self.direction = "right"
            if (self.x-player.xDisp > vic.x-player.xDisp):
                self.x -= 1
                self.direction = "left"
            if (self.y-player.yDisp < vic.y-player.yDisp):
                self.y += 1
            if (self.y-player.yDisp > vic.y-player.yDisp):
                self.y -= 1
        elif (distance < 51):
            if (self.time >= 100):
                self.time = 0
                self.speedY = randint(-2,2)
                self.speedX = randint(-2,2)
            else:
                self.time += 1
                self.x += self.speedX
                self.y += self.speedY
        
    def update(self):
        if self.state != "dead":
            for i in range(0, len(objList)):
                if objList[i].state == "dead" and self.prey != -1:
                    self.feed(objList[i])
                    self.attack = False
                    if len(charList) > self.prey:
                        charList[self.prey].hunter = -1
                        self.prey = -1
            if (self.health <= 0):
                self.attack = False
                self.die()
            if not self.attack and gamePlay == True:
                distance = math.sqrt(((int(player.x-(self.x-player.xDisp)))*(int(player.x-(self.x-player.xDisp))))+((int(player.y-(self.y-player.yDisp)))*(int(player.y-(self.y-player.yDisp)))))
                if (distance <= screenWidth):
                    self.attack = True
            elif self.attack == True and gamePlay == True:
                self.pursue()
            
            if (self.direction != "null" and self.health > 0):
                if (self.step == 20):
                    self.step = 0
                    if (self.direction == "right"):
                        if (self.spriteDisplay == 4):
                            self.spriteDisplay = 5
                        else:
                            self.spriteDisplay = 4
                    else:
                        if (self.spriteDisplay == 1):
                            self.spriteDisplay = 2
                        else:
                            self.spriteDisplay = 1
                else:
                    self.step += 1
            if (self.state == "wild" and self.attack != True and self.health > 0):
                if(self.time > 0):
                    self.time -= 1
                    self.x += self.speedX
                    self.y += self.speedY
                else:
                    self.direction = "null"
                    if (self.spriteDisplay == 4 or self.spriteDisplay == 5):
                        self.spriteDisplay = 3
                    elif (self.spriteDisplay == 1 or self.spriteDisplay == 2):
                        self.spriteDisplay = 0
                    self.logic()
        else:
            self.spriteDisplay = 9
    def logic(self):
        if not self.attack:
            randNum = random.randint(0, 20)
            if (randNum == 1):
                self.speedX = random.randint(-3, 3)
                self.speedY = random.randint(-3, 3)
                self.time = random.randint(50, 100)
                if (self.speedX > 0):
                    self.direction = "right"
                else:
                    self.direction = "left"
            elif (randNum > 1 and randNum < 10):
                self.speedX = random.randint(-1, 1)
                self.speedY = random.randint(-1, 1)
                self.time = random.randint(50, 100)
                if (self.speedX > 0):
                    self.direction = "right"
                else:
                    self.direction = "left"
            else:
                self.speedX = 0
                self.speedY = 0
                self.time = random.randint(50, 500)

class Human:
    def __init__(self,x,y,typ,state, direction, tile):
        self.direction = "null"
        self.x = x
        self.y = y
        self.bDir = "up"
        self.direction = direction
        self.type = typ
        self.speedX = 0
        self.speedY = 0
        self.hat = random.randint(0, len(hats)-1)
        self.time = 0
        self.looted = False
        self.horseMounted = -1
        self.step = 0
        self.width = 30
        self.height = 40
        self.state = state
        self.health = 30
        self.chased = False
        self.hunter = 0
        self.spriteDisplay = 0
        self.items = ["Beans", "Corn", "Bullet", "Dynamite", "pistol", "Better Pistol", "Best Pistol", "Spurrs o' Leather"]
        self.npcCreate(tile)

    def npcCreate(self, tile):
        randNum = random.randint(0,3)
        if tile == "path":
            for i in range(0, len(screenObjects)):
                if screenObjects[i] == "path":
                    if player.direction == "right":
                        self.y = screenObjY[i]+screenHeight
                    else:
                        self.xy = screenObjY[i]-screenHeight
            randNum = random.randint(0,1)
            if randNum == 0:
                print("HOSRE MAAAAAN")
                self.state = "mounted"
                horse = Horse(random.randint(0, 800)+screenWidth, random.randint(0, 600)+screenHeight, "horse", len(charList)-1)
                self.horseMounted = len(objList)
                objList.append(horse)
            elif randNum == 1:
                self.state = "mobile"
        elif tile == "town" or tile == "camp":
            self.state = "townsfolk"
            print("townsfolk")

    def interact(self):
        if self.looted == False and self.state == "dead":
            if (player.x > self.x - player.xDisp and player.x < self.x - player.xDisp + 95 and player.y > self.y - player.yDisp and player.y < self.y - player.yDisp + 81 or self.x-player.xDisp > player.x-50 and self.x-player.xDisp < player.x+50 and self.y-player.yDisp > player.y-50 and self.y-player.yDisp < player.y+50):
                player.inventory("hat"+ str(self.hat+1), 1)
                for k in range(0, random.randint(0,3)):
                    player.inventory(self.items[random.randint(0, len(self.items)-1)], random.randint(1,2))
                    self.looted = True
    
    def update(self):
        if self.health <= 0:
            self.spriteDisplay = 4
            self.state = "dead"
            self.direction = "null"
        if self.direction == "up":
            self.spriteDisplay = 0
        elif self.direction == "right":
            self.spriteDisplay = 1
        elif self.direction == "down":
            self.spriteDisplay = 2
        elif self.direction == "left":
            self.spriteDisplay = 3
        if self.state == "mounted" or self.state == "mobile":
            for j in range(0, len(objList)):
                if objList[j].type == "wolf":
                    distance = math.sqrt(((int(objList[j].x-self.x))*(int(objList[j].x-self.x)))+((int(objList[j].y-self.y))*(int(objList[j].y-self.y))))
                    if distance <= screenWidth:
                        self.chased = True
                        self.hunter = j
                        objList[j].prey = i
            if self.time >= 2 and not self.chased:
                self.time = 0
                if self.direction == "left":
                    if self.state == "mobile":
                        self.x -= 1
                    else:
                        self.x -= 2
                if self.direction == "right":
                    if self.state == "mobile":
                        self.x += 1
                    else:
                        self.x += 2
            else:
                self.time += 1
            if self.chased:
                self.attack()
        if self.state == "townsfolk":
            if(self.time > 0):
                self.time -= 1
                self.x += self.speedX
                self.y += self.speedY
            else:
                if not self.chased:
                    self.logic()
                else:
                    self.attack()

    def logic(self):
        randNum = random.randint(0, 20)
        if (randNum < 10):
            self.speedX = random.randint(-1, 1)
            self.speedY = random.randint(-1, 1)
            self.time = random.randint(50, 75)
            if (self.speedX > 0):
                self.direction = "right"
            else:
                self.direction = "left"
            if self.state != "mounted":
                if (self.speedY > 0):
                    self.direction = "down"
                else:
                    self.direction = "up"
        else:
            self.speedX = 0
            self.speedY = 0
            self.time = random.randint(50, 300)
    
    def attack(self):
        #distance = math.sqrt(((int(objList[self.hunter].x-self.x))*(int(objList[self.hunter].x-self.x)))+((int(objList[self.hunter].y-self.y))*(int(objList[self.hunter].y-self.y))))
        if len(objList) > self.hunter:
            dY = (objList[self.hunter].y - self.y) * (objList[self.hunter].y - self.y)
            dX = (objList[self.hunter].x - self.x) * (objList[self.hunter].x - self.x)
            #print("dX: " + str(math.sqrt(dX)))
            #print("dY: " + str(math.sqrt(dY)))
            if dX > dY:
                if objList[self.hunter].x > self.x and math.sqrt(dX) > 200:
                    self.x += 1
                    self.direction = "right"
                    self.bDir = "right"
                elif objList[self.hunter].x < self.x and math.sqrt(dX) > 200:
                    self.x -= 1
                    self.direction = "left"
                    self.bDir = "left"
            elif dX < dY:
                if objList[self.hunter].y > self.y and math.sqrt(dY) > 200:
                    self.y += 1
                    if self.state != "mounted":
                        self.direction = "down"
                        self.bDir = "down"
                elif objList[self.hunter].y < self.y and math.sqrt(dY) > 200:
                    self.y -= 1
                    if self.state != "mounted":
                        self.direction = "up"
                        self.bDir = "up"
            else:
                if self.time >= 200:
                    self.time = 0
                    if objList[self.hunter].y - self.y > 0:
                        if objList[self.hunter].x - self.x > 0:
                            bullet = Bullet((self.width/2), self.y+(self.height/2), 3, 3, i)
                        else:
                            bullet = Bullet((self.width/2), self.y+(self.height/2), -3, 3, i)
                        bulletList.append(bullet)
                    else:
                        if objList[self.hunter].x - self.x > 0:
                            bullet = Bullet((self.width/2), self.y+(self.height/2), 3, -3, i)
                        else:
                            bullet = Bullet((self.width/2), self.y+(self.height/2), -3, -3, i)
                    bulletList.append(bullet)
                else:
                    self.time += 1
        self.fire()
    def fire(self):
        if self.time >= 200:
            self.time = 0
            if len(objList) > self.hunter:
                if self.bDir == "up":
                    bullet = Bullet((self.width/2), self.y+(self.height/2), 0, 3, i)
                if self.bDir == "down":
                    bullet = Bullet((self.width/2), self.y+(self.height/2), 0, -3, i)
                if self.bDir == "left":
                    bullet = Bullet((self.width/2), self.y+(self.height/2), -3, 0, i)
                if self.bDir == "right":
                    bullet = Bullet((self.width/2), self.y+(self.height/2), 3, 0, i)
                bulletList.append(bullet)
        else:
            self.time += 1
        
class Horse:
    def __init__(self,x,y,typ,npc):
        self.direction = "null"
        self.x = x
        self.y = y
        self.type = typ
        self.speedX = 0
        self.speedY = 0
        self.time = 0
        self.npc = npc
        self.step = 0
        self.width = 95
        self.height = 81
        self.state = "wild"
        self.health = 15
        self.back = False
        self.looted = False
        self.items = ["Leather", "Meat"]
        self.spriteDisplay = 0

    def interact(self):
        if self.state != "dead":
            if self.state == "mounted":
                self.state = "wild"
                player.state = "normal"
                self.x = 400+player.xDisp+screenDisp[0]
                self.y = 300+player.yDisp+screenDisp[1]
                player.horseMounted = 0
            elif (player.x > self.x - player.xDisp and player.x < self.x - player.xDisp + 95 and player.y > self.y - player.yDisp and player.y < self.y - player.yDisp + 81):
                self.state = "mounted"
                player.state = "mounted"
                player.horseMounted = i
                objList[player.horseMounted].y = 297
                if player.direction == "left":
                    objList[player.horseMounted].x = 363
                else:
                    objList[player.horseMounted].x = 372
        elif self.looted == False:
            if (player.x > self.x - player.xDisp and player.x < self.x - player.xDisp + 95 and player.y > self.y - player.yDisp and player.y < self.y - player.yDisp + 81 or self.x-player.xDisp > player.x-50 and self.x-player.xDisp < player.x+50 and self.y-player.yDisp > player.y-50 and self.y-player.yDisp < player.y+50):
                for k in range(0, random.randint(0,3)):
                    player.inventory(self.items[random.randint(0, len(self.items)-1)], random.randint(1,3))
                    self.looted = True
    def die(self):
        if (self.step == 30):
            self.step = 0
            if not self.back:
                if self.spriteDisplay > -1 and self.spriteDisplay < 6:
                    self.spriteDisplay = 6
                elif self.spriteDisplay == 6:
                    self.spriteDisplay =7
                elif self.spriteDisplay == 7:
                    self.spriteDisplay = 8
                elif self.spriteDisplay == 8:
                    self.back = True
                    self.spriteDisplay = 7
            else:
                if self.spriteDisplay == 7:
                    self.spriteDisplay = 6
                elif self.spriteDisplay == 6:
                    self.spriteDisplay = 0
                elif self.spriteDisplay == 0:
                    self.y += 35
                    #SAVE HORSE CARCAS
                    print("dead")
                    self.state = "dead"
        else: 
            self.step += 1
    
    def update(self):
        if self.state != "dead":
            if (self.direction != "null" and self.state == "wild" and self.npc == -1):
                if (self.step == 20):
                    self.step = 0
                    if (self.direction == "left"):
                        if (self.spriteDisplay == 4):
                            self.spriteDisplay = 5
                        else:
                            self.spriteDisplay = 4
                    else:
                        if (self.spriteDisplay == 1):
                            self.spriteDisplay = 2
                        else:
                            self.spriteDisplay = 1 
                else:
                    self.step += 1
            if (self.state == "wild" and self.npc == -1):
                if(self.time > 0):
                    self.time -= 1
                    self.x += self.speedX
                    self.y += self.speedY
                else:
                    self.direction = "null"
                    if (self.spriteDisplay == 4 or self.spriteDisplay == 5):
                        self.spriteDisplay = 3
                    elif (self.spriteDisplay == 1 or self.spriteDisplay == 2):
                        self.spriteDisplay = 0
                    self.logic()
            if (self.health <= 0 and self.state != "dead"):
                self.die()
        else:
            self.spriteDisplay = 9
    def logic(self):
        randNum = random.randint(0, 20)
        if (randNum == 1):
            self.speedX = random.randint(-3, 3)
            self.speedY = random.randint(-3, 3)
            self.time = random.randint(50, 75)
            if (self.speedX > 0):
                self.direction = "right"
            else:
                self.direction = "left"
        elif (randNum > 1 and randNum < 10):
            self.speedX = random.randint(-1, 1)
            self.speedY = random.randint(-1, 1)
            self.time = random.randint(50, 75)
            if (self.speedX > 0):
                self.direction = "right"
            else:
                self.direction = "left"
        else:
            self.speedX = 0
            self.speedY = 0
            self.time = random.randint(50, 300)

class Hawk:
    def __init__(self,x,y,typ):
        self.x = x
        self.y = y
        self.type = typ
        self.speedX = 0
        self.speedY = 0
        self.time = 0
        self.step = 0
        self.looted = False
        self.width = 25
        self.height = 25
        self.fall = 200
        self.state = "wild"
        self.health = 3
        self.flyTrue = False
        self.items = ["Beak", "Feather", "Feather", "Feather"]
        self.spriteDisplay = 0

    def interact(self):
        if self.looted == False and self.state == "dead":
            if (player.x > self.x - player.xDisp and player.x < self.x - player.xDisp + 95 and player.y > self.y - player.yDisp and player.y < self.y - player.yDisp + 81 or self.x-player.xDisp > player.x-50 and self.x-player.xDisp < player.x+50 and self.y-player.yDisp > player.y-50 and self.y-player.yDisp < player.y+50):
                for k in range(0, random.randint(0,3)):
                    player.inventory(self.items[random.randint(0, len(self.items)-1)], random.randint(1,3))
                    self.looted = True
    
    def fly(self):
        if player.x > self.x-player.xDisp:
            if player.x-(self.x-player.xDisp) < 250:
                self.x -= 1
        elif player.x < self.x-player.xDisp:
            if (self.x-player.xDisp)-player.x < 250:
                self.x += 1
        self.y -= 1

    def die(self):
        if self.flyTrue == True:
            if self.fall > 0:
                self.fall -= 2
                self.y += 1
                self.spriteDisplay = 3
            else:
                self.spriteDisplay = 4
                self.state = "dead"
        else:
            self.state = "dead"
            self.spriteDisplay = 4
    
    def update(self):
        if self.health > 0:
            distance = math.sqrt(((int(player.x-(self.x-player.xDisp)))*(int(player.x-(self.x-player.xDisp))))+((int(player.y-(self.y-player.yDisp)))*(int(player.y-(self.y-player.yDisp)))))
            if distance < 200:
                self.flyTrue = True
            if distance > screenHeight*2:
                self.flyTrue = False
                objDelList.append(i)
            if self.flyTrue:
                self.fly()
                if self.step >= 30:
                    self.step = 0
                    if self.spriteDisplay == 1:
                        self.spriteDisplay = 2
                    else:
                        self.spriteDisplay = 1
                else:
                    self.step += 1
        elif self.state != "dead":
            self.die()
        if self.state == "dead":
            self.spriteDisplay = 4

def text(msg, color, x, y, size, *positional_parameters, **keyword_parameters):
    if ('font' in keyword_parameters):
        font = pygame.font.Font(keyword_parameters['font'], size)
    else:
        font = pygame.font.Font("fonts/western.ttf", size)
    screen_text = font.render(msg, True, color)         #Text Popup
    gameDisplay.blit(screen_text, (x, y))

def charTile(screenObjX, screenObjY, screenImg, string, mapWidth, mapHeight):
    data = []
    indiviSet = []
    #TOWN CODE
    townX = []
    townY = []
    townSize = []
    town = -1
    tileType = "normal"
    for i in range(0, int((mapWidth+mapHeight)/8)):
        townX.append(random.randint(0, mapWidth))
        townY.append(random.randint(0, mapHeight))
        townSize.append(random.randint(1,2))
    print(townX)
    print(townY)
    #TOWN CODE - END
    
    #RAIL CODE
    randDir = random.randint(0,1)
    if randDir == 0:
        randNum = random.randint(0, mapWidth)
        randX = random.randint(0, 800)
    else:
        randNum = random.randint(0, mapHeight)
        randY = random.randint(0, 600)
    total = mapWidth * mapHeight
    #RAIL CODE - END
    for i in range(0, mapWidth):
        thing = i
        for j in range(0, mapHeight):
            tileType = "normal"
            town = -1
            for k in range(0, len(townX)):
                if townX[k] == thing and townY[k] == j:
                    tileType = "town"
                    town = k
            if tileType != "town":
                indiviSet = []
                #PATH CODE - START
                for k in range(0, len(townX)):
                    if townX[k] == thing:
                        for l in range(0, 16):
                            indiviSet.append({
                                'type': "path",
                                'x': 400+random.randint(-40, 40),
                                'y': l*40,
                            })
                    if townY[k] == j:
                        for l in range(0, 20):
                            indiviSet.append({
                                'type': "path",
                                'x': l*50,
                                'y': 300+random.randint(-40, 40),
                            })
                #PATH CODE - END
                
                #RAIL CODE
                if randNum == i and randDir == 0:
                    indiviSet.append({
                        'type': "railV",
                        'x': randX,
                        'y': 1,
                    })
                if randNum == j and randDir == 1:
                    indiviSet.append({
                        'type': "railH",
                        'x': 1,
                        'y': randY,
                    })
                #RAIL CODE - END

                if random.randint(0, 15) == 10:
                    fireX = random.randint(0, 800)
                    fireY = random.randint(0, 600)
                    campSize = random.randint(0, 3)
                    indiviSet.append({'type': 'tentH','x': fireX - 270,'y': fireY})
                    if campSize > 0:
                        indiviSet.append({'type': 'tentH','x': fireX + 120,'y': fireY})
                    if campSize > 1:
                        indiviSet.append({'type': 'tentV','x': fireX - 45,'y': fireY - 230})
                    if campSize > 2:
                        indiviSet.append({'type': 'tentV','x': fireX-45,'y': fireY + 150})
                    indiviSet.append({'type': 'fire','x': fireX ,'y': fireY+45})

                if random.randint(0, 20) == 10:
                    print("indivi HOUSE")
                    indiviSet.append({'type': 'house1','x': random.randint(0, 800),'y': random.randint(0, 600)})
                    
                for k in range(0, objNum):
                    randObj = random.randint(0, 21)
                    screenObjX.append(random.randint(0, 800))
                    screenObjY.append(random.randint(0, 600))
                    if randObj == 0 or randObj == 1:            
                        screenObjects.append("cactusBig")
                        screenImg.append(pygame.image.load("objectSprites/cactus1.png"))
                    elif randObj > 1 and randObj < 6:
                        screenObjects.append("cactusSmall")
                        screenImg.append(pygame.image.load("objectSprites/cactus2.png"))
                    elif randObj > 5 and randObj < 11:
                        screenObjects.append("rockSmall")
                        if random.randint(0, 2) == 0:
                            screenImg.append(pygame.image.load("objectSprites/rock2.png"))
                        else:
                            screenImg.append(pygame.image.load("objectSprites/rock1.png"))
                    elif randObj > 10 and randObj < 17:
                        screenObjects.append("grass")
                        screenImg.append(pygame.image.load("objectSprites/grass2.png"))
                    elif randObj > 16 and randObj < 21:
                        screenObjects.append("grassBig")
                        screenImg.append(pygame.image.load("objectSprites/grass1.png"))
                    indiviSet.append({
                        'type': screenObjects[len(screenObjects)-1],
                        'x': screenObjX[len(screenObjects)-1],
                        'y': screenObjY[len(screenObjects)-1]
                    })
            elif tileType == "town":
                indiviSet.append({'type': 'bank','x': 0,'y': 0})
                indiviSet.append({'type': 'sherrif','x': 300,'y': 0})
                modX = 0
                modY = 0
                for k in range(0, townSize[town]):
                    if random.randint(0,1) == 0:
                        indiviSet.append({'type': 'house1','x': k*300,'y': 300})
                    else:
                        indiviSet.append({'type': 'house2','x': k*300,'y': 300})
            
            data.append({
                'x': thing,
                'y': j,
                'type': tileType,
                'obj': indiviSet
            })
            with open('maps/' + string + '.json', 'w') as outfile:  
                json.dump(data, outfile)

            #DISPLAY STUFF
            gameDisplay.fill((194, 178, 128))
            for i in range(0, len(objList)-1):
                if not gamePlay:
                    objList[i].update()
                if(objList[i].type == "horse"):
                    gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
                elif(objList[i].type == "wolf"):
                    gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            percent = int(((thing*mapHeight + j)/total)*100)
            text("Spurrs", (0, 0, 0), 20, 20, 60)
            text("v-Alpha", (0, 0, 0), 60, 85, 15)
            text("Creating Map", (0, 0, 0), 20, 270, 60, font="fonts/normal.ttf")
            text(str(percent) + "% complete", (0, 0, 0), 20, 350, 20, font="fonts/normal.ttf")
            pygame.display.update()

def loadFile(file):
    global mapWidth
    global mapHeight
    
    largestXVal = 0
    largestYVal = 0
    with open(str(file), "r") as jsonFile:
        data = json.load(jsonFile)
    for i in range(0, len(data)):
        largestXVal = data[i]["x"]
        largestYVal = data[i]["y"]
    mapWidth = largestXVal+1
    mapHeight = largestYVal+1

def itemInfo(items, selected):
    if len(items) > selected:
        with open("itemSprites/items.json", "r") as jsonFile:
            data = json.load(jsonFile)
        for n in range(0, len(data)):
            if data[n]["item"] == items[selected]:
                image = pygame.image.load("itemSprites/" + items[selected] + ".png")
                image = pygame.transform.scale(image, (120, 120))
                gameDisplay.blit(image, (125, 95))
                text(data[n]["item"], (0,0,0), 255, 120, 16, font="fonts/normal.ttf")
                if data[n]["type"] == "item":
                    text(data[n]["boost"]+":", (0,0,0), 255, 150, 16, font="fonts/normal.ttf")
                    text(str(data[n]["inc"]), (0,0,0), 265, 167, 16, font="fonts/normal.ttf")
                else:
                    for k in range(0, len(data[n]["perk"])):
                        if data[n]["tier"] == 0:
                            text(str(data[n]["perk"][k]), (0,191,255), 255, 147+k*12, 12, font="fonts/normal.ttf")
                        if data[n]["tier"] == 1:
                            text(str(data[n]["perk"][k]), (255,255,0), 255, 147+k*12, 12, font="fonts/normal.ttf")
                        if data[n]["tier"] == 2:
                            text(str(data[n]["perk"][k]), (147,112,219), 255, 147+k*12, 12, font="fonts/normal.ttf")
                text("Press Z to apply item", (0,0,0), 125, 265, 14, font="fonts/normal.ttf")
                for k in range(0, len(data[n]["description"])):
                    text(data[n]["description"][k], (0,0,0), 125, 220+k*16, 14, font="fonts/normal.ttf")
            
def drawMap(file):
    global mapX
    global mapY
    global mapType

    mapX = []
    mapY = []
    mapType = []
    
    with open(str(file), "r") as jsonFile:
        data = json.load(jsonFile)
    for i in range(0, len(data)):
        for j in range(0, len(data[i]["obj"])):
            if data[i]["obj"][j]["type"] == "path" or data[i]["obj"][j]["type"] == "bank" or data[i]["obj"][j]["type"] == "camp":
                mapType.append(data[i]["obj"][j]["type"])
                mapX.append(data[i]["x"])
                mapY.append(data[i]["y"])

def loadInv():
    global invItems
    global invNum

    invItems = []
    invNum = []
    
    with open("charSprites/player.json", "r") as jsonFile:
        data = json.load(jsonFile)
    for n in range(0, len(data[0]["items"])):
        placed = False
        if len(invItems) > 0:
            for k in range(0, len(invItems)):
                if data[0]["items"][n] == invItems[k]:
                    invNum[k] += 1
                    placed = True
        if placed != True:
            invItems.append(data[0]["items"][n])
            invNum.append(1)
    
def renderTiles(file):
    print("render")
    global screenQuadX
    global screenQuadY
    global screenObjects
    global screenObjX
    global screenObjY
    global screenImg
    global screenDimX
    global screenDimY
    global mapWidth
    global mapHeight
    tile = "null"
    
    screenQuadX = []
    screenQuadY = []
    screenObjects = []
    screenObjX = []
    screenObjY = []
    screenImg = []
    screenDimX = []
    screenDimY = []
    largestXVal = 0
    largestYVal = 0
    with open(str(file), "r") as jsonFile:
        data = json.load(jsonFile)
    #render the tiles surrounding the player
    for i in range(0, len(data)):
        if (data[i]["x"] > largestXVal):
            largestXVal = data[i]["x"]
        if (data[i]["y"] > largestYVal):
            largesyYVal = data[i]["y"]
        
        if (data[i]["x"] == player.quadX or data[i]["x"] == player.quadX+1 or data[i]["x"] == player.quadX-1):
            if (data[i]["y"] == player.quadY or data[i]["y"] == player.quadY+1 or data[i]["y"] == player.quadY-1):
                
                for j in range(0, len(data[i]["obj"])):
                    screenQuadX.append(data[i]["x"])
                    screenQuadY.append(data[i]["y"])
                    screenObjects.append(data[i]["obj"][j]["type"])
                    screenObjX.append(data[i]["obj"][j]["x"])
                    screenObjY.append(data[i]["obj"][j]["y"])
                    if data[i]["obj"][j]["type"] == "cactusBig":
                        screenImg.append(pygame.image.load("objectSprites/cactus1.png"))
                        screenDimX.append(40)
                        screenDimY.append(100)
                    elif data[i]["obj"][j]["type"] == "cactusSmall":
                        screenImg.append(pygame.image.load("objectSprites/cactus2.png"))
                        screenDimX.append(30)
                        screenDimY.append(30)
                    elif data[i]["obj"][j]["type"] == "rockSmall":
                        screenImg.append(pygame.image.load("objectSprites/rock1.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                    elif data[i]["obj"][j]["type"] == "grass":
                        screenImg.append(pygame.image.load("objectSprites/grass2.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                    elif data[i]["obj"][j]["type"] == "grassBig":
                        screenImg.append(pygame.image.load("objectSprites/grass1.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                    elif data[i]["obj"][j]["type"] == "railH":
                        screenImg.append(pygame.image.load("tileSprites/railhorizontal.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                    elif data[i]["obj"][j]["type"] == "railV":
                        screenImg.append(pygame.image.load("tileSprites/railvertical.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                    elif data[i]["obj"][j]["type"] == "path":
                        screenImg.append(pygame.image.load("tileSprites/path.png"))
                        screenDimX.append(0)
                        screenDimY.append(0)
                        if tile != "town":
                            tile = "path"
                    elif data[i]["obj"][j]["type"] == "bank":
                        screenImg.append(pygame.image.load("tileSprites/bank.png"))
                        screenDimX.append(400)
                        screenDimY.append(300)
                        tile = "town"
                    elif data[i]["obj"][j]["type"] == "sherrif":
                        screenImg.append(pygame.image.load("tileSprites/sherrif.png"))
                        screenDimX.append(400)
                        screenDimY.append(300)
                        tile = "town"
                    elif data[i]["obj"][j]["type"] == "house1":
                        screenImg.append(pygame.image.load("tileSprites/house1.png"))
                        screenDimX.append(400)
                        screenDimY.append(300)
                        tile = "town"
                    elif data[i]["obj"][j]["type"] == "house2":
                        screenImg.append(pygame.image.load("tileSprites/house2.png"))
                        screenDimX.append(400)
                        screenDimY.append(300)
                        tile = "town"
                    elif data[i]["obj"][j]["type"] == "fire":
                        screenImg.append(pygame.image.load("tileSprites/fire.png"))
                        screenDimX.append(30)
                        screenDimY.append(30)
                        tile = "camp"
                    elif data[i]["obj"][j]["type"] == "tentH":
                        screenImg.append(pygame.image.load("tileSprites/tentH.png"))
                        screenDimX.append(180)
                        screenDimY.append(125)
                        tile = "camp"
                    elif data[i]["obj"][j]["type"] == "tentV":
                        screenImg.append(pygame.image.load("tileSprites/tentV.png"))
                        screenDimX.append(125)
                        screenDimY.append(180)
                        tile = "camp"
    spawnEntities(tile)
    
def spawnEntities(tile):
    for i in range(0, objNum):
        randNum = random.randint(0, 100)
        if (randNum < 5):
            print("horse")
            if (player.direction == "right"):
                horse = Horse(random.randint(0, 800)+screenWidth, random.randint(0, 600), "horse", -1)
            elif (player.direction == "left"):
                horse = Horse(random.randint(0, 800)-screenWidth, random.randint(0, 600), "horse", -1)
            elif (player.direction == "up"):
                horse = Horse(random.randint(0, 800), random.randint(0, 600)-screenHeight, "horse", -1)
            else:
                horse = Horse(random.randint(0, 800), random.randint(0, 600)+screenHeight, "horse", -1)
            objList.append(horse)
        elif randNum > 4 and randNum < 7:
            wolfNum = random.randint(3, 5)
            if player.direction == "up":
                for j in range(0, wolfNum):
                    wolf = Wolf(random.randint(0, 800), random.randint(0, 600)-screenHeight, "wolf")
                    objList.append(wolf)
            elif player.direction == "right":
                for j in range(0, wolfNum):
                    wolf = Wolf(random.randint(0, 800)+screenWidth, random.randint(0, 600), "wolf")
                    objList.append(wolf)
            elif player.direction == "down":
                for j in range(0, wolfNum):
                    wolf = Wolf(random.randint(0, 800), random.randint(0, 600)+screenHeight, "wolf")
                    objList.append(wolf)
            elif player.direction == "left":
                for j in range(0, wolfNum):
                    wolf = Wolf(random.randint(0, 800)-screenWidth, random.randint(0, 600), "wolf")
                    objList.append(wolf)
            print("wolf")
        elif randNum > 6 and randNum < 11:
            if (player.direction == "right"):
                for i in range(0, random.randint(3,5)):
                    hawk = Hawk(random.randint(0, 800)+screenWidth, random.randint(0, 600), "hawk")
            elif (player.direction == "left"):
                for i in range(0, random.randint(3,5)):
                    hawk = Hawk(random.randint(0, 800)-screenWidth, random.randint(0, 600), "hawk")
            elif (player.direction == "up"):
                for i in range(0, random.randint(3,5)):
                    hawk = Hawk(random.randint(0, 800), random.randint(0, 600)-screenHeight, "hawk")
            else:
                for i in range(0, random.randint(3,5)):
                    hawk = Hawk(random.randint(0, 800), random.randint(0, 600)+screenHeight, "hawk")
            objList.append(hawk)
            print("hawk")
        elif randNum > 10 and randNum < 20:
            if tile == "town" or tile == "path" or tile == "camp":
                print("npc")
                if (player.direction == "right"):
                    npc = Human(random.randint(0, 800)+screenWidth, random.randint(0, 600), random.randint(0, len(npcSprites)-1), "normal", "left", tile)
                elif (player.direction == "left"):
                    npc = Human(random.randint(0, 800)-screenWidth, random.randint(0, 600), random.randint(0, len(npcSprites)-1), "normal", "right", tile)
                elif (player.direction == "up"):
                    npc = Human(random.randint(0, 800), random.randint(0, 600)-screenHeight, random.randint(0, len(npcSprites)-1), "normal", "left", tile)
                else:
                    npc = Human(random.randint(0, 800), random.randint(0, 600)+screenHeight, random.randint(0, len(npcSprites)-1), "normal", "right", tile)
                charList.append(npc)

while not gameExit:
    for i in range(0, random.randint(5, 12)):
        randNum = random.randint(0, 1)
        if randNum == 0:
            horse = Horse(random.randint(0, 800), random.randint(0, 600), "horse", False)
            objList.append(horse)
        elif randNum == 1:
            wolf = Wolf(random.randint(0, 800), random.randint(0, 600), "wolf")
            objList.append(wolf)
    while not menuExit:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    setupExit = False
                    menuExit = True
                if event.key == pygame.K_F1:
                    infoObject = pygame.display.Info()
                    pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:
                    menuExit = True
                    settingsExit = False

        gameDisplay.fill((194, 178, 128))
        
        for i in range(0, len(objList)-1):
            objList[i].update()
            if(objList[i].type == "horse"):
                gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            elif(objList[i].type == "wolf"):
                gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))

        text("Spurrs", (0, 0, 0), 20, 20, 60)
        text("v-Alpha", (0, 0, 0), 60, 85, 15)
        text("hit ENTER to begin the game", (0, 0, 0), 20, 565, 15)
        text("hit F1 to enter fullscreen", (0, 0, 0), 20, 540, 15)
        pygame.display.update()

    selected = 0
    while not settingsExit:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected > 0:
                        selected -= 1
                    else:
                        selected = 2
                if event.key == pygame.K_DOWN:
                    if selected < 2:
                        selected += 1
                    else:
                        selected = 0
                if event.key == pygame.K_LEFT:
                    if selected == 0:
                        if screenWidth == 1600:
                            screenWidth = 1200
                            screenHeight = 900
                        elif screenWidth == 1200:
                            screenWidth = 800
                            screenHeight = 600
                        elif screenWidth == 800:
                            screenWidth = 600
                            screenHeight = 450
                        elif screenWidth == 600:
                            screenWidth = 400
                            screenHeight = 300
                if event.key == pygame.K_RIGHT:
                    if selected  == 0:
                        if screenWidth == 400:
                            screenWidth = 600
                            screenHeight = 450
                        elif screenWidth == 600:
                            screenWidth = 800
                            screenHeight = 600
                        elif screenWidth == 800:
                            screenWidth = 1200
                            screenHeight = 900
                        elif screenWidth == 1200:
                            screenWidth = 1600
                            screenHeight = 1200
        gameDisplay.fill((194, 178, 128))
        
        for i in range(0, len(objList)-1):
            objList[i].update()
            if(objList[i].type == "horse"):
                gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            elif(objList[i].type == "wolf"):
                gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
        gameDisplay.blit(wanted, (450, 100))    
        text("Spurrs", (0, 0, 0), 20, 20, 60)
        text("WanteD", (0, 0, 0), 470, 120, 50)
        text("v-Alpha", (0, 0, 0), 60, 85, 15)
        text("Press SPACE to create a new map...", (0, 0, 0), 20, 565, 15)
        text("Press ENTER to open an old map", (0, 0, 0), 20, 540, 15)
        if selected == 0:
            text("Display: " + str(screenWidth) + " x " + str(screenHeight), (255, 255, 0), 490, 200, 18, font="fonts/normal.ttf")
        else:
            text("Display: " + str(screenWidth) + " x " + str(screenHeight), (0, 0, 0), 490, 200, 18, font="fonts/normal.ttf")
        if selected == 1:
            text("Music: ON", (255, 255, 0), 490, 240, 18, font="fonts/normal.ttf")
        else:
            text("Music: ON", (0, 0, 0), 490, 240, 18, font="fonts/normal.ttf")
        if selected == 2:
            text("Sound Effects: ON", (255, 255, 0), 490, 280, 18, font="fonts/normal.ttf")
        else:
            text("Sound Effects: ON", (0, 0, 0), 490, 280, 18, font="fonts/normal.ttf")
        pygame.display.update()
        
    while not setupExit:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    creatingMap = True
                    loadingMap = False
                    setupExit = True
                if event.key == pygame.K_RETURN:
                    setupExit = True
                    loadingMap = True
                
        gameDisplay.fill((194, 178, 128))
        
        for i in range(0, len(objList)-1):
            objList[i].update()
            if(objList[i].type == "horse"):
                gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            elif(objList[i].type == "wolf"):
                gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            
        text("Spurrs", (0, 0, 0), 20, 20, 60)
        text("v-Alpha", (0, 0, 0), 60, 85, 15)
        text("Press SPACE to create a new map...", (0, 0, 0), 20, 565, 15)
        text("Press ENTER to open an old map", (0, 0, 0), 20, 540, 15)
        pygame.display.update()

    selected = 0
    files = glob.glob("maps/*.json")
    print(len(files))
    while loadingMap:
        for  event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gamePlay = False
                    setupExit = False
                    loadingMap = False
                    creatingMap = False
                if event.key == pygame.K_RETURN:
                    gamePlay = True
                    filePlaying = files[selected]
                    loadingMap = False
                    creatingMap = False
                    loadFile(filePlaying)
                if event.key == pygame.K_DOWN:
                    if selected == len(files)-1:
                        selected = 0
                    else:
                        selected += 1
                if event.key == pygame.K_UP:
                    if selected == 0:
                        selected = len(files)-1
                    else:
                        selected -= 1
        gameDisplay.fill((194, 178, 128))
        for i in range(0, len(objList)-1):
            if not gamePlay:
                objList[i].update()
            if(objList[i].type == "horse"):
                gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            elif(objList[i].type == "wolf"):
                gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
        
        gameDisplay.blit(wanted, (450, 100))
        text("Spurrs", (0, 0, 0), 20, 20, 60)
        text("v-Alpha", (0, 0, 0), 60, 85, 15)
        text("WanteD", (0, 0, 0), 470, 120, 50)
        text("Press ESC to cancel...", (0, 0, 0), 20, 565, 15)
        text("Press ENTER to OPEN the map", (0, 0, 0), 20, 540, 15)
        for i in range(0, len(files)):
            if (selected == i):
                text(str(files[i]), (255, 255, 0), 490, 200+(40*i), 20, font="fonts/normal.ttf")
            else:
                text(str(files[i]), (0, 0, 0), 490, 200+(40*i), 20, font="fonts/normal.ttf")
        pygame.display.update()
        
    string = "Map-Name-Here"
    while creatingMap:
        for  event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selected == 0:
                        selected = 1
                    elif selected == 1:
                        selected = 2
                    elif selected == 2:
                        selected = 0
                if event.key == pygame.K_UP:
                    if selected == 1:
                        selected = 0
                    elif selected == 0:
                        selected = 2
                    elif selected == 2:
                        selected = 1
                if event.key == pygame.K_LEFT:
                    if selected == 1 and mapHeight > 4:
                        mapHeight -= 2
                    if selected == 0 and mapWidth > 4:
                        mapWidth -= 2
                if event.key == pygame.K_RIGHT:
                    if selected == 1 and mapHeight < 40:
                        mapHeight += 2
                    if selected == 0 and mapWidth < 40:
                        mapWidth += 2
                if event.key == pygame.K_BACKSPACE:
                    if string != "":
                        string = string[:-1]
                if event.key == pygame.K_ESCAPE:
                    setupExit = False
                    creatingMap = False
                if event.key == pygame.K_RETURN:
                    charTile(screenObjX, screenObjY, screenImg, string, mapWidth, mapHeight)
                    setupExit = False
                    creatingMap = False
        gameDisplay.fill((194, 178, 128))
        for i in range(0, len(objList)-1):
            objList[i].update()
            if(objList[i].type == "horse"):
                gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
            elif(objList[i].type == "wolf"):
                gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
        if selected == 2:
            time.sleep(0.1)
            press=pygame.key.get_pressed()
            for i in range( pygame.K_a, pygame.K_z + 1 ): 
                if press[i] == True:
                    name=pygame.key.name(i)
                    string += name
        
        gameDisplay.blit(wanted, (450, 100))
        text("Spurrs", (0, 0, 0), 20, 20, 60)
        text("v-Alpha", (0, 0, 0), 60, 85, 15)
        text("WanteD", (0, 0, 0), 470, 120, 50)
        text("Press ESC to cancel...", (0, 0, 0), 20, 565, 15)
        text("Press ENTER to CREATE the map", (0, 0, 0), 20, 540, 15)
        if selected == 0:
            text("Map Width: < " + str(mapWidth) + " >", (255, 255, 0), 490, 200, 20, font="fonts/normal.ttf")
        else:
            text("Map Width: < " + str(mapWidth) + " >", (0, 0, 0), 490, 200, 20, font="fonts/normal.ttf")
        if selected == 1:
            text("Map Height: < " + str(mapHeight) + " >", (255, 255, 0), 490, 240, 20, font="fonts/normal.ttf")
        else:
            text("Map Height: < " + str(mapHeight) + " >", (0, 0, 0), 490, 240, 20, font="fonts/normal.ttf")
        if selected == 2:
            text("Name: < " + string + " >", (255, 255, 0), 490, 280, 20, font="fonts/normal.ttf")
        else:
            text("Name: < " + string + " >", (0, 0, 0), 490, 280, 20, font="fonts/normal.ttf")
        pygame.display.update()
    
    if gamePlay:
        player = Player()
        renderTiles(filePlaying)
        time.sleep(1)
    objList =  []
    while gamePlay:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xTrans = -1                    #disables diagonal movement
                    player.direction = "left"
                    if player.state == "mounted":
                        xTrans = -2
                        if len(objList) > player.horseMounted:
                            objList[player.horseMounted].direction = "left"
                if event.key == pygame.K_RIGHT:
                    xTrans = 1
                    player.direction = "right"
                    if player.state == "mounted":
                        xTrans = 2
                        if len(objList) > player.horseMounted:
                            objList[player.horseMounted].direction = "right"
                if event.key == pygame.K_UP:
                    yTrans = -1
                    player.direction = "up"
                    if player.state == "mounted":
                        yTrans = -2
                if event.key == pygame.K_DOWN:
                    yTrans = 1
                    player.direction = "down"
                    if player.state == "mounted":
                        yTrans = 2
                if event.key == pygame.K_z:
                    if player.pistol.find("Pistol") > -1 or player.pistol == "pistol":
                        if (player.spriteDisplay == 0 or player.spriteDisplay == 1 or player.spriteDisplay == 2):
                            bullet = Bullet(player.x + 15, player.y + 10, 0, -3, "player")
                        elif player.spriteDisplay == 6 or player.spriteDisplay == 7 or player.spriteDisplay == 8:
                            bullet = Bullet(player.x + 15, player.y + 10, 0, 3, "player")
                        elif (player.spriteDisplay == 9 or player.spriteDisplay == 10 or player.spriteDisplay == 11):
                            bullet = Bullet(player.x + 10, player.y + 25, -3, 0, "player")
                        elif player.spriteDisplay == 3 or player.spriteDisplay == 4 or player.spriteDisplay == 5:
                            bullet = Bullet(player.x + 10, player.y + 25, 3, 0, "player")
                        bulletList.append(bullet)
                    elif player.pistol == "Dynamite":
                        dynamite = Dynamite(player.x+player.xDisp, player.y+player.yDisp, 10)
                        objList.append(dynamite)
                if event.key == pygame.K_e:
                    for i in range(len(objList)):
                        if objList[i].type != "Dynamite":
                            objList[i].interact()
                    for i in range(len(charList)):
                        charList[i].interact()
                if event.key == pygame.K_m:
                    mapTrue = True
                    drawMap(filePlaying)
                    mapImg = pygame.image.load("tileSprites/wantedMap.png")
                    hat = pygame.image.load("itemSprites/hat.png")
                    scaleX = int(600/mapWidth)
                    scaleY = int(425/mapHeight)
                    while mapTrue:
                        for  event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE or event.key == pygame.K_m:
                                    mapTrue = False
                        
                        gameDisplay.blit(mapImg, (0, 0))
                        for i in range(0, len(mapType)):
                            if mapType[i] == "path":
                                pygame.draw.rect(gameDisplay, (101, 67, 33), (110+mapX[i]*scaleX, 100+mapY[i]*scaleY, scaleX/2, scaleY/2))
                            elif mapType[i] == "bank":
                                pygame.draw.rect(gameDisplay, (255, 255, 0), ((110+mapX[i]*scaleX)-scaleX/4, (100+mapY[i]*scaleY)-scaleY/4, scaleX, scaleY))
                            elif mapType[i] == "camp":
                                pygame.draw.rect(gameDisplay, (0, 255, 255), ((110+mapX[i]*scaleX)-scaleX/4, (100+mapY[i]*scaleY)-scaleY/4, 15, 15))
                        gameDisplay.blit(hat, ((110+player.quadX*scaleX)-scaleX/4, (100+player.quadY*scaleY)-scaleY/4))
                        #text("Map", (0, 0, 0), 100, 90, 40)
                        pygame.display.update()
                        
                if event.key == pygame.K_TAB:
                    invTrue = True
                    loadInv()
                    mapImg = pygame.image.load("tileSprites/wantedInv.png")
                    selected = 0
                    while invTrue:
                        for  event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE or event.key == pygame.K_TAB:
                                    invTrue = False
                                if event.key == pygame.K_UP and selected >= 5:
                                    selected -= 5
                                if event.key == pygame.K_DOWN and selected <= len(invItems)-6:
                                    selected += 5
                                if event.key == pygame.K_RIGHT and selected <= len(invItems)-2:
                                    selected += 1
                                if event.key == pygame.K_LEFT and selected >= 1:
                                    selected -= 1
                                if event.key == pygame.K_z:
                                    if invItems[selected].find("hat") > -1:
                                        with open("charSprites/player.json", "r") as jsonFile:
                                            data = json.load(jsonFile)
                                        if data[0]["hat"] != "null":
                                            data[0]["items"].append(data[0]["hat"])
                                            try:
                                                invNum[invItems.index(data[0]["hat"])] += 1
                                            except ValueError:
                                                invItems.append(data[0]["hat"])
                                                invNum.append(1)
                                        data[0]["items"].remove(invItems[selected])
                                        data[0]["hat"] = invItems[selected]
                                        invNum[selected] -= 1
                                        player.hat = data[0]["hat"]
                                        with open('charSprites/player.json', 'w') as outfile:  
                                            json.dump(data, outfile)
                                    elif invItems[selected] == "pistol" or invItems[selected] == "Better Pistol" or invItems[selected] == "Best Pistol" or invItems[selected] == "Dynamite":
                                        with open("charSprites/player.json", "r") as jsonFile:
                                            data = json.load(jsonFile)
                                        if data[0]["gun"] != "null":
                                            data[0]["items"].append(data[0]["gun"])
                                            try:
                                                invNum[invItems.index(data[0]["gun"])] += 1
                                            except ValueError:
                                                invItems.append(data[0]["gun"])
                                                invNum.append(1)
                                        data[0]["items"].remove(invItems[selected])
                                        data[0]["gun"] = invItems[selected]
                                        invNum[selected] -= 1
                                        player.pistol = data[0]["gun"]
                                        with open('charSprites/player.json', 'w') as outfile:  
                                            json.dump(data, outfile)
                                    elif invItems[selected].find("Spurrs") > -1:
                                        with open("charSprites/player.json", "r") as jsonFile:
                                            data = json.load(jsonFile)
                                        if data[0]["spurrs"] != "null":
                                            data[0]["items"].append(data[0]["spurrs"])
                                            try:
                                                invNum[invItems.index(data[0]["spurrs"])] += 1
                                            except ValueError:
                                                invItems.append(data[0]["spurrs"])
                                                invNum.append(1)
                                        data[0]["items"].remove(invItems[selected])
                                        data[0]["spurrs"] = invItems[selected]
                                        invNum[selected] -= 1
                                        player.spurrs = data[0]["spurrs"]
                                        with open('charSprites/player.json', 'w') as outfile:  
                                            json.dump(data, outfile)
                                    
                        
                        gameDisplay.blit(mapImg, (0, 0))
                        for i in range(0, int(len(invItems)/5)+1):
                            for j in range(0, 5):
                                if len(invItems) > (i*5)+j:
                                    image = pygame.image.load("itemSprites/" + invItems[(i*5)+j] + ".png")
                                    image = pygame.transform.scale(image, (55, 55))
                                    if (i*5)+j == selected:
                                        pygame.draw.rect(gameDisplay, (255, 255, 0), (349+(j*70), 98+(i*70), 55, 55))
                                    gameDisplay.blit(image, (349+(j*70), 98+(i*70)))
                                    text(str(invNum[(i*5)+j]), (255, 255, 255), 349+(j*70)+3, 98+(i*70)+3, 20, font="fonts/normal.ttf")
                        text("Health: " + str(player.health),(0,0,0) ,150 , 390, 16, font="fonts/normal.ttf")
                        itemInfo(invItems, selected)
                        if player.pistol != "null":
                            image = pygame.image.load("itemSprites/" + player.pistol + ".png")
                            image = pygame.transform.scale(image, (45, 45))
                            gameDisplay.blit(image, (283, 313))
                        if player.hat != "null":
                            image = pygame.image.load("itemSprites/" + player.hat + ".png")
                            image = pygame.transform.scale(image, (45, 45))
                            gameDisplay.blit(image, (124, 313))
                        if player.vest != "null":
                            image = pygame.image.load("itemSprites/" + player.vest + ".png")
                            image = pygame.transform.scale(image, (45, 45))
                            gameDisplay.blit(image, (177, 313))
                        if player.spurrs != "null":
                            image = pygame.image.load("itemSprites/" + player.spurrs + ".png")
                            image = pygame.transform.scale(image, (45, 45))
                            gameDisplay.blit(image, (230, 313))
                        pygame.display.update()
                        
            if event.type == pygame.KEYUP:                  #Stops rect from moving forever
                player.direction = "null"
                if(player.state == "mounted"):
                    if event.key == pygame.K_RIGHT:
                        xTrans = 0
                        player.spriteDisplay = 3
                    if event.key == pygame.K_LEFT:
                        xTrans = 0
                        player.spriteDisplay = 9
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        yTrans = 0
                    
                    if (len(objList) > player.horseMounted):
                        objList[player.horseMounted].direction = "null"
                else:
                    if event.key == pygame.K_RIGHT:
                        xTrans = 0
                        player.spriteDisplay = 3
                    if event.key == pygame.K_LEFT:
                        xTrans = 0
                        player.spriteDisplay = 9
                    if event.key == pygame.K_UP:
                        yTrans = 0
                        player.spriteDisplay = 0
                    if event.key == pygame.K_DOWN:
                        yTrans = 0
                        player.spriteDisplay = 6
                    
        if player.direction != "null":
            player.walk()

        if player.xDisp < 400 and player.xDisp > -400 and player.yDisp < 300 and player.yDisp > -300:
            player.xDisp += xTrans
            player.yDisp += yTrans
        else:
            if player.xDisp >= 400:
                player.quadX +=1
                player.xDisp = -399 #(player.xDisp * -1) + 1
                for i in range(0, len(objList)):
                    if objList[i].state != "mounted" or objList[i].npc == -1:
                        objList[i].x -= 800
                for i in range(0, len(charList)):
                    charList[i].x -= 800
                for i in range(0, len(explosions)):
                    explosions[i].x -= 800
            elif player.xDisp <= -400:
                player.quadX -=1
                player.xDisp = 399 #(player.xDisp * -1) - 1
                for i in range(0, len(objList)):
                    if objList[i].state != "mounted" or objList[i].npc == -1:
                        objList[i].x += 800
                for i in range(0, len(charList)):
                    charList[i].x += 800
                for i in range(0, len(explosions)):
                    explosions[i].x += 800
            elif player.yDisp >= 300:
                player.quadY +=1
                player.yDisp = -299#(player.yDisp * -1) + 1
                for i in range(0, len(objList)):
                    if objList[i].state != "mounted" or objList[i].npc == -1:
                        objList[i].y -= 600
                for i in range(0, len(charList)):
                    charList[i].y -= 600
                for i in range(0, len(explosions)):
                    explosions[i].y -= 600
            elif player.yDisp <= -300:
                player.quadY -=1
                player.yDisp = 299#(player.yDisp * -1) - 1
                for i in range(0, len(objList)):
                    if objList[i].state != "mounted" or objList[i].npc == -1:
                        objList[i].y += 600
                for i in range(0, len(charList)):
                    charList[i].y += 600
                for i in range(0, len(explosions)):
                    explosions[i].y += 600
            renderTiles(filePlaying)

        if player.state == "mounted":
            if player.direction == "left":
                player.spriteDisplay = 9
                if (len(objList) > player.horseMounted):
                    if objList[player.horseMounted].type == "horse":
                        objList[player.horseMounted].x = 363+screenDisp[0]
                        objList[player.horseMounted].direction = "left"
            elif player.direction == "right":
                player.spriteDisplay = 3
                if (len(objList) > player.horseMounted):
                    if objList[player.horseMounted].type == "horse":
                        objList[player.horseMounted].x = 372+screenDisp[0]
                        objList[player.horseMounted].direction = "right"
            if (len(objList) > player.horseMounted):
                objList[player.horseMounted].y = 297+screenDisp[1]
                
        for i in range(0, len(charList)):
            if charList[i].state == "mounted":
                if charList[i].direction == "left":
                    #charList[i].spriteDisplay = 9
                    if (len(objList) > charList[i].horseMounted):
                        if objList[charList[i].horseMounted].type == "horse":
                            objList[charList[i].horseMounted].x = charList[i].x - 36
                            objList[charList[i].horseMounted].direction = "left"
                elif charList[i].direction == "right":
                    #charList[i].spriteDisplay = 3
                    if (len(objList) > charList[i].horseMounted):
                        if objList[charList[i].horseMounted].type == "horse":
                            objList[charList[i].horseMounted].x = charList[i].x -28
                            objList[charList[i].horseMounted].direction = "right"
                if (len(objList) > charList[i].horseMounted):
                    objList[charList[i].horseMounted].y = charList[i].y
            
        gameDisplay.fill((194, 178, 128))
        #Display all of rendered screenObjects
        for i in range(0, len(screenObjects)-1):
            #DISPLAY RENDERED OBJECTS
            if screenQuadX[i] == player.quadX:
                if screenQuadY[i] == player.quadY:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+screenDisp[0], screenObjY[i]-player.yDisp+screenDisp[1]))
                    #CHECK FOR OBJECT COLLISION
                    #if (screenDimX[i] != 0):
                    #    if (player.x == screenObjX[i]-player.xDisp and player.y >= screenObjY[i]-player.yDisp and player.y <= screenObjY[i]-player.yDisp + screenDimY[i]):
                    #        xTrans = 0
                    #    elif (player.x == screenObjX[i]-player.xDisp+screenDimX[i] and player.y >= screenObjY[i]-player.yDisp and player.y <= screenObjY[i]-player.yDisp + screenDimY[i]):
                    #        xTrans = 0
                    #    elif (player.y == screenObjY[i]-player.yDisp and player.x >= screenObjX[i]-player.xDisp and player.x <= screenObjX[i]-player.xDisp+screenDimX[i]):
                    #        yTrans = 0
                    #    elif (player.y == screenObjY[i]-player.yDisp+screenDimY[i] and player.x >= screenObjX[i]-player.xDisp and player.x <= screenObjX[i]-player.xDisp+screenDimX[i]):
                    #        yTrans = 0
                elif screenQuadY[i] == player.quadY-1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+screenDisp[0], screenObjY[i]-player.yDisp+(screenDisp[1]-600)))
                elif screenQuadY[i] == player.quadY+1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+screenDisp[0], screenObjY[i]-player.yDisp+(screenDisp[1]+600)))
            elif screenQuadX[i] == player.quadX-1:
                if screenQuadY[i] == player.quadY:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]-800), screenObjY[i]-player.yDisp+screenDisp[1]))
                elif screenQuadY[i] == player.quadY-1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]-800), screenObjY[i]-player.yDisp+(screenDisp[1]-600)))
                elif screenQuadY[i] == player.quadY+1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]-800), screenObjY[i]-player.yDisp+(screenDisp[1]+600)))
            elif screenQuadX[i] == player.quadX+1:
                if screenQuadY[i] == player.quadY:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]+800), screenObjY[i]-player.yDisp+screenDisp[1]))
                elif screenQuadY[i] == player.quadY-1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]+800), screenObjY[i]-player.yDisp+(screenDisp[1]-600)))
                elif screenQuadY[i] == player.quadY+1:
                    gameDisplay.blit(screenImg[i], (screenObjX[i]-player.xDisp+(screenDisp[0]+800), screenObjY[i]-player.yDisp+(screenDisp[1]+600)))
        player.update()
        
        for i in range(0, len(objList)-1):
            if (objList[i].x-player.x > screenWidth*2 or objList[i].x-player.x < -screenWidth*2 or objList[i].y-player.y > screenHeight*2 or objList[i].y-player.y < -screenHeight*2):
                objDelList.append(i)
            else:
                objList[i].update()
                if (objList[i].type == "horse"):
                    if (objList[i].state != "mounted"):
                        gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x-player.xDisp, objList[i].y-player.yDisp))
                    else:
                        gameDisplay.blit(horseSprites[objList[i].spriteDisplay], (objList[i].x, objList[i].y))
                elif (objList[i].type == "wolf"):
                    gameDisplay.blit(wolfSprites[objList[i].spriteDisplay], (objList[i].x-player.xDisp, objList[i].y-player.yDisp))
                elif (objList[i].type == "hawk"):
                    gameDisplay.blit(hawkSprites[objList[i].spriteDisplay], (objList[i].x-player.xDisp, objList[i].y-player.yDisp))
                elif (objList[i].type == "Dynamite"):
                    image = pygame.transform.scale(tntSprites[objList[i].spriteDisplay], (36, 36))
                    gameDisplay.blit(image, (objList[i].x-player.xDisp, objList[i].y-player.yDisp))
        if len(charList) > 0:
            for i in range(0, len(charList)-1):
                if (charList[i].x-player.xDisp-player.x > screenWidth*2 or charList[i].x-player.xDisp-player.x < -screenWidth*2 or charList[i].y-player.yDisp-player.y > screenHeight*2 or charList[i].y-player.yDisp-player.y < -screenHeight*2):
                    charDelList.append(i)
                else:
                    charList[i].update()
                    gameDisplay.blit(npcSprites[charList[i].type][charList[i].spriteDisplay], (charList[i].x-player.xDisp, charList[i].y-player.yDisp))
                    if charList[i].looted == False:
                        image = pygame.transform.scale(hats[charList[i].hat], (25, 25))
                        gameDisplay.blit(image, (charList[i].x-player.xDisp, charList[i].y-player.yDisp-8))

        if len(charDelList) > 0:
            listToDel = list(reversed(charDelList))
            charDelList.sort(reverse=True)
            for i in range(0, len(listToDel)-1):
                del charList[listToDel[i]]
            listToDel = []
            charDelList = []
         
        if (len(objDelList) > 0):
            objDelList.sort(reverse=True)
            for i in range(0, len(objDelList)):
                for j in range(0, len(charList)):
                    if charList[j].horseMounted > objDelList[i]:
                        charList[j].horseMounted -= 1
                if (objList[objDelList[i]].state != "mounted"):
                    del objList[objDelList[i]]
            objDelList = []
        
        if (len(bulletList) > 0):
            for i in range(0, len(bulletList)-1):
                if (bulletList[i].x-player.x > screenWidth/2 or bulletList[i].x-player.x < -screenWidth/2 or bulletList[i].y-player.y > screenHeight/2 or bulletList[i].y-player.y < -screenHeight/2):
                    delList.append(i)
                else:
                    bulletList[i].update()
                    if bulletList[i].owner == "player":
                        pygame.draw.rect(gameDisplay, (0,0,0), (bulletList[i].x, bulletList[i].y, 5,5))
                    else:
                        if bulletList[i].owner < len(charList):
                            if bulletList[i].speedX > 0:
                                if bulletList[i].speedY > 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (bulletList[i].x+charList[bulletList[i].owner].x-player.xDisp, charList[bulletList[i].owner].y+bulletList[i].y-player.yDisp, 5,5))
                                elif bulletList[i].speedY < 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (bulletList[i].x+charList[bulletList[i].owner].x-player.xDisp, charList[bulletList[i].owner].y+bulletList[i].y-player.yDisp, 5,5))
                                elif bulletList[i].speedY == 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (bulletList[i].x+charList[bulletList[i].owner].x-player.xDisp, charList[bulletList[i].owner].y-player.yDisp, 5,5))
                            elif bulletList[i].speedX < 0:
                                if bulletList[i].speedY > 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (charList[bulletList[i].owner].x-bulletList[i].x-player.xDisp, charList[bulletList[i].owner].y+(charList[bulletList[i].owner].height/2)-bulletList[i].y-player.yDisp, 5,5))
                                elif bulletList[i].speedY < 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (charList[bulletList[i].owner].x-bulletList[i].x-player.xDisp, charList[bulletList[i].owner].y+(charList[bulletList[i].owner].height/2)-bulletList[i].y-player.yDisp, 5,5))
                                elif bulletList[i].speedY == 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (charList[bulletList[i].owner].x-bulletList[i].x-player.xDisp, charList[bulletList[i].owner].y+(charList[bulletList[i].owner].height/2)-player.yDisp, 5,5))
                            elif bulletList[i].speedX == 0:
                                if bulletList[i].speedY > 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (charList[bulletList[i].owner].x-player.xDisp, charList[bulletList[i].owner].y+(charList[bulletList[i].owner].height/2)-bulletList[i].y-player.yDisp, 5,5))
                                elif bulletList[i].speedY < 0:
                                    pygame.draw.rect(gameDisplay, (0,0,0), (charList[bulletList[i].owner].x-player.xDisp, charList[bulletList[i].owner].y+(charList[bulletList[i].owner].height/2)+bulletList[i].y-player.yDisp, 5,5))
        for i in range(0, len(charList)):
            if charList[i].state == "dead" and charList[i].looted == False:
                if (player.x > charList[i].x - player.xDisp and player.x < charList[i].x - player.xDisp + 95 and player.y > charList[i].y - player.yDisp and player.y < charList[i].y - player.yDisp + 81 or charList[i].x-player.xDisp > player.x-50 and charList[i].x-player.xDisp < player.x+50 and charList[i].y-player.yDisp > player.y-50 and charList[i].y-player.yDisp < player.y+50):
                    text("Press E to loot Body", (0, 0, 0), 20, 564, 16, font="fonts/normal.ttf")
        for i in range(0, len(objList)):
            if objList[i].state == "dead" and objList[i].looted == False:
                if (player.x > objList[i].x - player.xDisp and player.x < objList[i].x - player.xDisp + 95 and player.y > objList[i].y - player.yDisp and player.y < objList[i].y - player.yDisp + 81 or objList[i].x-player.xDisp > player.x-50 and objList[i].x-player.xDisp < player.x+50 and objList[i].y-player.yDisp > player.y-50 and objList[i].y-player.yDisp < player.y+50):
                    text("Press E to loot Body", (0, 0, 0), 20, 564, 16, font="fonts/normal.ttf")
                    
        if (len(delList) > 0):
            delList.sort(reverse=True)
            for i in range(0,len(delList)-1):
                if len(bulletList)-1 > delList[i]:
                    del bulletList[delList[i]]
            listToDel = []
            delList = []
        
        gameDisplay.blit(playerSprites[player.spriteDisplay], (player.x, player.y))
        image = pygame.image.load("itemSprites/" + player.hat + ".png")
        image = pygame.transform.scale(image, (25, 25))
        gameDisplay.blit(image, (player.x+2, player.y-8))
        
        if collTrue == True and len(collItems) > 0:
            for i in range(0, len(collItems)):
                if collTime[i] > 0:
                    collTime[i] -= 1
                    image = pygame.image.load("itemSprites/" + collItems[i] + ".png")
                    image = pygame.transform.scale(image, (16, 16))
                    gameDisplay.blit(image, (20, 20+i*16))
                    text("x" + collNum[i] + " " + collItems[i], (0, 0, 0), 40, 20+i*16, 16, font="fonts/normal.ttf")
                else:
                    collDel.append(i)
        else:
            collTrue = False

        if len(expDel) > 0:
            #expDel.sort(reverse=True)
            for i in range(0, len(expDel)-1):
                del explosions[expDel[i]]
            expDel = []
        
        if len(explosions) > 0 :
            for i in range(0, len(explosions)):
                explosions[i].update()
                if (explosions[i].x-player.x > 600 or explosions[i].x-player.x < -600 or explosions[i].y-player.y > 450 or explosions[i].y-player.y < -450):
                    delList.append(i)
            
        if len(collDel) > 0:
            collDel.sort(reverse=True)
            for i in range(0, len(collDel)):
                collItems.pop(collDel[i])
                collTime.pop(collDel[i])
                collNum.pop(collDel[i])
            collDel = []
        
        pygame.display.update()
        clock.tick(240)

pygame.quit()
quit()
        















        
