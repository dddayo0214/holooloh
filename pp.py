import pygame
import random
import os

FPS=60
W=1800
H=1000

pygame.init()
pygame.mixer.init()
full=True
screen = pygame.display.set_mode(((W,H)),pygame.FULLSCREEN)
pygame.display.set_caption("holooloh")

clock=pygame.time.Clock()

im_img=pygame.image.load(os.path.join("img","b4.jpg")).convert()
pygame.display.set_icon(im_img)
imimg=pygame.image.load(os.path.join("img","b1.png")).convert()
die_img=pygame.image.load(os.path.join("img","dd.png")).convert()
die_img.set_colorkey((255,255,255))
m_img=pygame.image.load(os.path.join("img","player.png")).convert()
mini_img=pygame.transform.scale(m_img,(100,120))
mini_img.set_colorkey((255,255,255))
mg=pygame.image.load(os.path.join("img","bullet.png")).convert()
boss_img=pygame.image.load(os.path.join("img","boss1.png")).convert()
p1=pygame.image.load(os.path.join("img","h1.png")).convert()
p2=pygame.image.load(os.path.join("img","h.png")).convert()
p3=pygame.image.load(os.path.join("img","he.png")).convert()
p4=pygame.image.load(os.path.join("img","hel.png")).convert()
p5=pygame.image.load(os.path.join("img","help.png")).convert()
p6=pygame.image.load(os.path.join("img","hh.png")).convert()
first=pygame.image.load(os.path.join("img","first.png")).convert()
www=pygame.image.load(os.path.join("img","win.png")).convert()
pa=pygame.image.load(os.path.join("img","pause.png")).convert()
go=pygame.image.load(os.path.join("img","go.png")).convert()

img=[]
for i in range(4):
    img.append(pygame.image.load(os.path.join("img",f"enemy{i}.png")).convert())

emg=[]
for i in range(4):
    emg.append(pygame.image.load(os.path.join("img",f"aenemy{i}.png")).convert())

expl_anim={}
expl_anim['lg']=[]
expl_anim['sm']=[]
expl_anim['player']=[]
for i in range(3):
    expl_img=pygame.image.load(os.path.join("img",f"d{i}.png")).convert()
    expl_img.set_colorkey((255,255,255))
    expl_anim['lg'].append(pygame.transform.scale(expl_img,(200,250)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img,(100,150)))
    
for i in range(5):
    player_expl_img=(pygame.image.load(os.path.join("img",f"dd.png")).convert())
    player_expl_img.set_colorkey((255,255,255))
    expl_anim['player'].append(player_expl_img)

p_imgs={}
p_imgs['shield']=pygame.image.load(os.path.join("img",f"power0.png")).convert()
p_imgs['gun']=pygame.image.load(os.path.join("img",f"power1.png")).convert()
p_imgs['tbul']=pygame.image.load(os.path.join("img",f"power2.png")).convert()

shoot=pygame.mixer.Sound(os.path.join("sound","sh.mp3"))
die_sound=pygame.mixer.Sound(os.path.join("sound","ro.mp3"))
expl_sounds=[
    pygame.mixer.Sound(os.path.join("sound","peko.mp3")),
    pygame.mixer.Sound(os.path.join("sound","shooooot.mp3")),
    pygame.mixer.Sound(os.path.join("sound","shooot.mp3")),
    pygame.mixer.Sound(os.path.join("sound","gawra.mp3"))]
pygame.mixer.music.load(os.path.join("sound","shot.mp3"))

font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,(0,0,153))
    text_rect=text_surface.get_rect()
    text_rect.centerx=x
    text_rect.top=y
    surf.blit(text_surface,text_rect)

def new_rock():
    r=P()
    all_sprites.add(r)
    rocks.add(r)

def new_r():
    ro=R()
    all_sprites.add(ro)
    rockss.add(ro)

def new_roc():
    roc=RO()
    all_sprites.add(roc)
    rocksss.add(roc)

def new_boss():
    all_sprites.add(boss)
    bosss.add(boss)

def draw_health(surf,hp,x,y):
    if hp<0:
        hp=0
    BAR_L=500
    BAR_H=50
    fill=(hp/100)*BAR_L
    outline_rect=pygame.Rect(x,y,BAR_L,BAR_H)
    fill_rect=pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,(0,255,0),fill_rect)
    pygame.draw.rect(surf,(255,255,255),outline_rect,2)

def draw_healths(surf,hp,x,y):
    if hp<0:
        hp=0
    BAR_L=500
    BAR_H=50
    fill=(hp/100)*BAR_L
    outline_rect=pygame.Rect(x,y,BAR_L,BAR_H)
    fill_rect=pygame.Rect(x,y,fill,BAR_H)
    pygame.draw.rect(surf,(255,0,0),fill_rect)
    pygame.draw.rect(surf,(255,255,255),outline_rect,2)    

def draw_lives(surf,lives,img,x,y):
    for i in range(lives):
        img_rect=img.get_rect()
        img_rect.x=x+200*i
        img_rect.y=y
        surf.blit(img,img_rect)

def draw_init():
    screen.blit(imimg,(0,0))
    pygame.mouse.set_visible(False)
    pygame.display.update()
    waiting=True
    while waiting:      
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
                return True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    waiting=False
                    return False
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                    pygame.quit()
                    return True
                if event.key==pygame.K_h:
                    help_init()
                    return 2
                #if event.key==pygame.K_DOWN:
                    #R1()
                    #return 2
            #elif event.type == pygame.MOUSEBUTTONDOWN :
                #if W/2.3 < pygame.mouse.get_pos()[0] < W/2.5 + 300 and H/2.5 < pygame.mouse.get_pos()[1] < H/2.5 + 90:
                    #help_init()
                    #return 2

def a_init():
    screen.blit(pa,(0,0))
    pygame.mouse.set_visible(True)
    pygame.display.update()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    waiting=False
                    pygame.mouse.set_visible(False)
                if event.key==pygame.K_ESCAPE:
                    waiting=False

def R1():    
    screen.blit(www,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    wait=True
    while wait:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    wait=False
                    pygame.quit()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    wait=False
                if event.key==pygame.K_LSHIFT:
                    wait=False
                if event.key==pygame.K_RSHIFT:
                    wait=False

def R2():    
    screen.blit(go,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waitin=True
    while waitin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    waitin=False
                    pygame.quit()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waitin=False
                if event.key==pygame.K_LSHIFT:
                    waitin=False
                if event.key==pygame.K_RSHIFT:
                    waitin=False 
        
def h1():   
    screen.blit(p3,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                elif event.key==event.key==pygame.K_RIGHT:
                    h()
                    waiting=False
    
def h():    
    screen.blit(p1,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                elif event.key==pygame.K_RIGHT:
                    he()
                    waiting=False
                elif event.key==pygame.K_LEFT:
                    h1()
                    waiting=False

def he():  
    screen.blit(p2,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                elif event.key==event.key==pygame.K_LEFT:
                    h()
                    waiting=False
                elif event.key==event.key==pygame.K_RIGHT:
                    hel()
                    waiting=False

def hel():   
    screen.blit(p5,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                elif event.key==event.key==pygame.K_LEFT:
                    he()
                    waiting=False
                elif event.key==event.key==pygame.K_RIGHT:
                    help()
                    waiting=False

def help():   
    screen.blit(p4,(0,0))
    pygame.display.update()
    clock.tick(FPS)
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                waiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_ESCAPE:
                    waiting=False
                elif event.key==event.key==pygame.K_LEFT:
                    hel()
                    waiting=False

def help_init():
    aiting=True
    screen.blit(p6,(0,0))
    pygame.display.update()    
    clock.tick(FPS)
    while aiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                aiting=False
                pygame.quit()
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_g:
                    aiting=False
                elif event.key==pygame.K_ESCAPE:
                    aiting=False
                elif event.key==pygame.K_RIGHT:
                    h1()
                    aiting=False
        
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=m_img
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.radius=80
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius)
        self.rect.center=(W/2,H-200)
        self.speedx=8
        self.speedy=8
        self.health=100
        self.lives=3
        self.hidden=False
        self.sh=1
        self.hide_time=0
        self.gun=1
        self.gunp=1
        self.gun_time=0
        self.gunp_time=0
        self.shoot_time=0

    def update(self):
        now=pygame.time.get_ticks()
        if self.gun>1 and now-self.gun_time>2000:
            self.gun-=1
            self.gun_time=now

        if self.gunp>1 and now-self.gunp_time>2000:
            self.gunp-=1
            self.gunp_time=now

        if self.hidden and now-self.hide_time>1500:
            self.hidden=False
            self.image=m_img
            #self.rect.centerx=W/2
            #self.rect.bottom=H-50
        
        if self.sh==2 and now-self.shoot_time>50:
            self.sh-=1

        akey_pressed=pygame.key.get_pressed()
        if akey_pressed[pygame.K_d]:
            self.rect.x+=self.speedx
        if akey_pressed[pygame.K_a]:
            self.rect.x-=self.speedx
        if akey_pressed[pygame.K_w]:
            self.rect.y-=self.speedy
        if akey_pressed[pygame.K_s]:
            self.rect.y+=self.speedy
        if akey_pressed[pygame.K_RIGHT]:
            self.rect.x+=self.speedx
        if akey_pressed[pygame.K_LEFT]:
            self.rect.x-=self.speedx
        if akey_pressed[pygame.K_UP]:
            self.rect.y-=self.speedy
        if akey_pressed[pygame.K_DOWN]:
            self.rect.y+=self.speedy
        if not full:
            if self.rect.right>W:
                self.rect.right=W
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.bottom>H:
                self.rect.bottom=H
            if self.rect.top<0:
                self.rect.top=0
        elif full:
            if self.rect.right>1950:
                self.rect.right=1950
            if self.rect.left<0:
                self.rect.left=0
            if self.rect.bottom>1100:
                self.rect.bottom=1100
            if self.rect.top<0:
                self.rect.top=0
        else:
            return 0

    def shoot(self):      
        if not(self.hidden) and self.sh==1:
            self.shoot_time=pygame.time.get_ticks()
            if self.gun==1:
                bullet=b(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot.play()
                self.sh=2
            elif self.gun==2:
                bullet1=b(self.rect.left, self.rect.centery)
                bullet2=b(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot.play()
                self.sh=2
            elif self.gun>2:
                bullet1=b(self.rect.left, self.rect.centery)
                bullet2=b(self.rect.right, self.rect.centery)
                bullet3=b(self.rect.centerx, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(bullet3)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
                shoot.play()
                self.sh=2
            if self.gunp==2:
                bulle=bu(self.rect.centerx, self.rect.top)
                bull=bul(self.rect.centerx, self.rect.top)
                all_sprites.add(bulle)
                all_sprites.add(bull)
                bullets.add(bulle)
                bullets.add(bull)
                self.sh=2
            '''''
            if self.gunp==3:
                bulle1=bu(self.rect.centerx-10, self.rect.left)
                bulle2=bu(self.rect.centerx-20, self.rect.left)
                bull1=bul(self.rect.centerx-10, self.rect.right)
                bull2=bul(self.rect.centerx-20, self.rect.right)
                all_sprites.add(bulle1)
                all_sprites.add(bulle2)
                all_sprites.add(bull1)
                all_sprites.add(bull2)
                bullets.add(bulle1)
                bullets.add(bulle2)
                bullets.add(bull1)
                bullets.add(bull2)
            
            if self.gunp>3:
                bulle1=bu(self.rect.centerx-10, self.rect.left)
                bulle2=bu(self.rect.centerx-20, self.rect.left)
                bulle3=bu(self.rect.centerx-30, self.rect.left)
                bull1=bul(self.rect.centerx-10, self.rect.right)
                bull2=bul(self.rect.centerx-20, self.rect.right)
                bull3=bul(self.rect.centerx-30, self.rect.right) 
                all_sprites.add(bulle1)
                all_sprites.add(bulle2)
                all_sprites.add(bulle3)
                all_sprites.add(bull1)
                all_sprites.add(bull2)
                all_sprites.add(bull3)
                bullets.add(bulle1)
                bullets.add(bulle2)
                bullets.add(bulle3)
                bullets.add(bull1)
                bullets.add(bull2)
                bullets.add(bull3)
                '''
    def hide(self):
        self.hidden=True
        self.image=die_img
        self.hide_time=pygame.time.get_ticks()
        self.rect.center=(W/2,H-200)
    
    def gup(self):
        self.gun+=1
        self.gun_time=pygame.time.get_ticks()
    
    def gupp(self):
        self.gunp+=1
        self.gunp_time=pygame.time.get_ticks()

class P(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori=random.choice(img)
        self.image_ori.set_colorkey((255,255,255))
        self.image=self.image_ori.copy()
        self.rect=self.image.get_rect() 
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image,(0,255,255),self.rect.center,self.radius)
        self.rect.x=random.randrange(0,W-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(1,10)
        self.speedx=random.randrange(-15,15)
        self.total_degree=0
        self.rot_degree=random.randrange(-3,3)

    def rotate(self):
        self.total_degree+=self.rot_degree
        self.total_degree=self.total_degree%360
        self.image=pygame.transform.rotate(self.image_ori,self.total_degree)
        center=self.rect.center
        self.rect=self.image.get_rect()
        self.rect.center=center

    def update(self):
        self.rotate()
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>H or self.rect.left>W or self.rect.right<0:
            self.rect.x=random.randrange(0,W-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedy=random.randrange(1,10)
            self.speedx=random.randrange(-15,15)

class R(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori=random.choice(emg)
        self.image_ori.set_colorkey((255,255,255))
        self.image=self.image_ori.copy()
        self.rect=self.image.get_rect() 
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius)
        self.rect.x=random.randrange(-150,-40)
        self.rect.y=random.randrange(0,H-self.rect.height)
        self.speedy=random.randrange(-15,15)
        self.speedx=random.randrange(1,10)
        self.total_degree=0
        self.rot_degree=random.randrange(-3,3)

    def rotate(self):
        self.total_degree+=self.rot_degree
        self.total_degree=self.total_degree%360
        self.image=pygame.transform.rotate(self.image_ori,self.total_degree)
        center=self.rect.center
        self.rect=self.image.get_rect()
        self.rect.center=center

    def update(self):
        self.rotate()
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>H or self.rect.bottom<0 or self.rect.left>W:
            self.rect.x=random.randrange(-100,-40)
            self.rect.y=random.randrange(0,H-self.rect.height)
            self.speedy=random.randrange(-15,15)
            self.speedx=random.randrange(1,10)

class RO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori=random.choice(emg)
        self.image_ori.set_colorkey((255,255,255))
        self.image=self.image_ori.copy()
        self.rect=self.image.get_rect() 
        self.radius=int(self.rect.width/2)
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius)
        self.rect.x=random.randrange(2000,2500)
        self.rect.y=random.randrange(0,H-self.rect.height)
        self.speedy=random.randrange(-15,15)
        self.speedx=random.randrange(-10,0)
        self.total_degree=0
        self.rot_degree=random.randrange(-3,3)

    def rotate(self):
        self.total_degree+=self.rot_degree
        self.total_degree=self.total_degree%360
        self.image=pygame.transform.rotate(self.image_ori,self.total_degree)
        center=self.rect.center
        self.rect=self.image.get_rect()
        self.rect.center=center

    def update(self):
        self.rotate()
        self.rect.y+=self.speedy
        self.rect.x+=self.speedx
        if self.rect.top>H or self.rect.bottom<0 or self.rect.right<0:
            self.rect.x=random.randrange(2000,2500)
            self.rect.y=random.randrange(0,H-self.rect.height)
            self.speedy=random.randrange(-15,15)
            self.speedx=random.randrange(-10,0)

class B(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori=boss_img
        self.image_ori.set_colorkey((255,255,255))
        self.image=self.image_ori.copy()
        self.rect=self.image.get_rect() 
        self.radius=int(self.rect.width/2.5)
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius)
        self.rect.x=W/20
        self.rect.y=random.randrange(-100,-40)
        self.speedy=5
        self.health=100

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top>H:
            self.rect.x=W/2
            self.rect.y=random.randrange(-100,-40)
            self.speedy=5

class b(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=mg
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/1.5
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius) 
        self.rect.centerx=x
        self.rect.bottom=y
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

class bu(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=mg
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/1.5
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius) 
        self.rect.centerx=x
        self.rect.bottom=y
        self.speedx=-10

    def update(self):
        self.rect.x+=self.speedx
        if self.rect.right<0:
            self.kill()

class bul(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=mg
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.radius=self.rect.width/1.5
        #pygame.draw.circle(self.image,(0,0,0),self.rect.center,self.radius) 
        self.rect.centerx=x
        self.rect.bottom=y
        self.speedx=10

    def update(self):
        self.rect.x+=self.speedx
        if self.rect.left>W:
            self.kill()

class e(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=expl_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50
    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(expl_anim[self.size]):
                self.kill()
            else:
                self.image=expl_anim[self.size][self.frame]
                center=self.rect.center
                self.rect=self.image.get_rect()
                self.rect.center=center

class Pow(pygame.sprite.Sprite):

    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type=random.choice(['shield','gun','tbul'])
        self.image=p_imgs[self.type]
        self.image.set_colorkey((0,0,0))
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.speedy=5

    def update(self):
        self.rect.y+=self.speedy
        if self.rect.top>H:
            self.kill()

all_sprites=pygame.sprite.Group()
rocks=pygame.sprite.Group()
rockss=pygame.sprite.Group()
rocksss=pygame.sprite.Group()
bosss=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player1=Player1()
boss=B()
power=pygame.sprite.Group()
all_sprites.add(player1)

for i in range(20):
    new_rock()

score=0
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

show_init=True
running=True
while running:
    if show_init: 
        close=draw_init()
        if close==True:
            break
        elif close==False:
            show_init=False
        elif close==2:
            show_init=True
            continue
        pygame.mouse.set_visible(False) 
        all_sprites=pygame.sprite.Group()
        rocks=pygame.sprite.Group()
        rockss=pygame.sprite.Group()
        rocksss=pygame.sprite.Group()
        bosss=pygame.sprite.Group()
        bullets=pygame.sprite.Group()
        player1=Player1()
        boss=B()
        power=pygame.sprite.Group()
        all_sprites.add(player1)
        for i in range(20):
            new_rock()
        ro=True
        rocc=True
        bo=True
        score=0

    FPS=60
    FPS*=1.00005
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player1.shoot()
            if event.key==pygame.K_KP_ENTER:
                a=True
                if a:
                    a_init()
                    a=False
                    '''''
            if event.key==pygame.K_F11:
                if not full:
                    screen = pygame.display.set_mode((30000,2000),pygame.FULLSCREEN)
                    full=True
                elif full:
                    screen = pygame.display.set_mode((W,H),pygame.RESIZABLE)
                    full=False
                    '''
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_ESCAPE:
                show_init=True

    all_sprites.update()

    
    hits=pygame.sprite.groupcollide(rocks,bullets,True,True,pygame.sprite.collide_circle)
    hit=pygame.sprite.groupcollide(rockss,bullets,True,True,pygame.sprite.collide_circle)
    it=pygame.sprite.groupcollide(rocksss,bullets,True,True,pygame.sprite.collide_circle)
    itbo=pygame.sprite.groupcollide(bosss,bullets,False,True,pygame.sprite.collide_circle)
    for t in hits:
        random.choice(expl_sounds).play()
        if score<10000 or boss.health==0:
            score+=t.radius-40
        expl=e(t.rect.center,'lg')
        all_sprites.add(expl)
        if random.random()>0.9:
            pow=Pow(t.rect.center)
            all_sprites.add(pow)
            power.add(pow) 
        new_rock()
        
    for t in hit:
        random.choice(expl_sounds).play()
        if score<10000 or boss.health==0:
            score+=t.radius-40
        expl=e(t.rect.center,'lg')
        all_sprites.add(expl)
        if random.random()>0.9:
            pow=Pow(t.rect.center)
            all_sprites.add(pow)
            power.add(pow)
        new_r()

    for t in it:
        random.choice(expl_sounds).play()
        if score<10000 or boss.health==0:
            score+=t.radius-40
        expl=e(t.rect.center,'lg')
        all_sprites.add(expl)
        if random.random()>0.9:
            pow=Pow(t.rect.center)
            all_sprites.add(pow)
            power.add(pow) 
        new_roc()

    for t in itbo:
        random.choice(expl_sounds).play()
        boss.health-=1
        if boss.health<0:
            boss.health=0
            die=e(boss.rect.center,'player')
            all_sprites.add(die)
            die_sound.play()
            boss.kill()

    hitssss=pygame.sprite.spritecollide(player1,rocks,True,pygame.sprite.collide_circle)
    hitsss=pygame.sprite.spritecollide(player1,rockss,True,pygame.sprite.collide_circle)
    hitss=pygame.sprite.spritecollide(player1,rocksss,True,pygame.sprite.collide_circle)
    hitbo=pygame.sprite.spritecollide(player1,bosss,False,pygame.sprite.collide_circle)
    for t in hitssss:
        new_rock()
        if not player1.hidden:
            player1.health-=t.radius-30
            if random.random()>0.99:
                pow=Pow(t.rect.center)
                all_sprites.add(pow)
                power.add(pow)

    for t in hitsss:
        new_r()
        if not player1.hidden:
            player1.health-=t.radius-30
            if random.random()>0.99:
                pow=Pow(t.rect.center)
                all_sprites.add(pow)
                power.add(pow)
        
    for t in hitss:
        new_roc()
        if not player1.hidden:
            player1.health-=t.radius-30
            if random.random()>0.99:
                pow=Pow(t.rect.center)
                all_sprites.add(pow)
                power.add(pow)

    for t in hitbo:
        player1.health-=90
        boss.rect.x=W/20
        boss.rect.y=random.randrange(-100,-40)         


    if score>=3000 and score<4000 and ro==True:
        for i in range(10):
            new_r()
        ro=False
    elif score>=4000 and score<5000 and rocc==True:
        for i in range(10):
            new_roc()
        rocc=False
    elif score>=10000 and bo==True:
        score=10000  
        new_boss()
        bo=False
        
        
    if player1.health<=0:
        die=e(player1.rect.center,'player')
        all_sprites.add(die)
        die_sound.play()
        player1.lives-=1
        player1.health=100
        player1.hide()
        pygame.time.wait(200)


    hi=pygame.sprite.spritecollide(player1,power,True)
    for hi in hi:
        if hi.type=='shield':
            player1.health+=20
            if player1.health>100:
                player1.health=100
        elif hi.type=='gun':
            player1.gup()
        elif hi.type=='tbul':
            player1.gupp()

    if player1.lives==0 and not (die.alive()):
        pygame.mouse.set_visible(False)
        if score<=10000:
            R2()
            show_init=True
        elif score>10000:
            R1()
            show_init=True

    screen.fill((255,0,0))
    screen.blit(im_img,(0,0))
    all_sprites.draw(screen)
    draw_text(screen,str(score),50,W/2,10)
    draw_health(screen,player1.health,5,10)
    draw_healths(screen,boss.health,5,100) 
    draw_lives(screen,player1.lives,mini_img,W-650,15)
    pygame.display.update()

pygame.quit()