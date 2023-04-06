import pygame as pg
import random
import sys
pg.init()

W, H = 600, 500
w_b, h_b = 30, 30
w_h,h_h = 80, 80

count_life = 10
coins = 0


FPS = 180
timer_spawn = 2
timer_bonus = timer_spawn * FPS / 3 

bonus_box = 0

image_life = pg.image.load("life.png")
image_life = pg.transform.scale(image_life,(w_b * 2, h_b * 2))


sound_coin = pg.mixer.Sound("audio/zvon-brosanija-monet.wav")
#pg.mixer.music.load("audio/zvon-brosanija-monet.wav")
#pg.mixer.music.play()
sound_heart = pg.mixer.Sound("audio/jg-032316-sfx-video-game-game-over-3.wav")

root = pg.display.set_mode((W, H))

image_bg = pg.transform.scale( pg.image.load('Bg000.png'), (W,H) )
clock = pg.time.Clock()

images_hero_idle = []
for i in range(0,13,3):
    im = pg.image.load(f"Transparent/02_idle/skeleton-02_idle_{str(i).zfill(2)}.png")
    im = pg.transform.scale(im, (w_h, h_h))
    images_hero_idle.append(im)

images_hero = []
for j in range(0, 13, 3):
    r_im = pg.image.load(f"Transparent/03_run/skeleton-03_run_{str(j).zfill(2)}.png")
    r_im = pg.transform.scale(r_im, (w_h, h_h))
    images_hero.append(r_im)

bonus_list = pg.sprite.Group()

run = True


class Bonus(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.type = random.choice(["life", "death","coin"])
        image = pg.image.load(self.type + ".png")
        self.image = pg.transform.scale(image, (w_b, h_b))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w_b // 2, W -(w_b + w_b // 2))
        self.rect.y = 5
        self.speed = random.randrange(1, 5)
        
        
class Hero:

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = images_hero[0]
        self.frame = 0

        self.rect = self.image.get_rect()
        self.rect.x = (W// 2)
        self.rect.y = H -100
        self.left = False
        self.right = False

    def move(self, k_k):
        if k_k[pg.K_LEFT] and self.rect.x > 0:
            
            self.left = True
            self.right = False
            FPS = 60
            self.rect.x -= 3
            
            
        elif k_k[pg.K_RIGHT] and self.rect.x < W - w_h:
            
            self.left = False
            self.right = True
            FPS = 60
            self.rect.x += 3
        else:
            self.left = False
            self.right = False
            FPS = 10

    


    def draw(self):

        #we take suits po ocheredi from ssuit list
        #i razmeschaem v coordinatu self.rect

        if self.left:
            image = pg.transform.flip(images_hero[self.frame],1,0)
            root.blit(image, self.rect)
            self.frame = (self.frame + 1) % self.count_frame
            #print(1)
        elif self.right:
            image = images_hero[self.frame]
            self.frame = (self.frame + 1) % self.count_frame
            root.blit(image, self.rect)
            #print(2)
        else:
            image = images_hero_idle[self.frame]
            self.frame = (self.frame + 1) % self.count_frame
            root.blit(image, self.rect)
            #print(3)


def text_draw(my_text,coords, size, color):
    font = pg.font.Font(None, size)
    text = font.render(my_text, True, color)
    root.blit(text, coords)


def draw():
    root.blit(image_bg, (0,0))
    text_draw(str(coins), (10,10), 30, (255,  6, 3))
    Joker.draw()
    #root.blit(Joker.image, Joker.rect)
    bonus_list.draw(root)

    #for bonus in bonus_list:
     #   bonus.rect.y += bonus.speed
    
    for i in range(count_life):
        x = W - w_b * 2 - w_b * 2 * i
        
        y = 10
        root.blit(image_life ,(x, y))
        
    text_draw("Space - to buy 1 life for 10 coins", (W / 20, H - 40), 50, (255,255,0))    

    pg.display.flip()
    
Joker = Hero()
Joker.count_frame = len(images_hero)
Joker.count_frame_idle = len(images_hero_idle)
while run:
    clock.tick(FPS)

    keys_klava = pg.key.get_pressed()
    Joker.move(keys_klava)

    grab_bonuses = pg.sprite.spritecollide(Joker, bonus_list, True)

    for el in grab_bonuses:
        if el.type == "death":
            count_life -= 1
        elif el.type == "coin":
            sound_coin.play()
            coins += 1
        #elif el.type =="life":
         #   count_life += 1
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    timer_bonus -= 1
    if timer_bonus == 0:
        if bonus_box > 10:
            timer_spawn -= 1 / (100 + bonus_box)
            
        timer_bonus = timer_spawn * FPS / 3
        bonus = Bonus()
        bonus_list.add(bonus)
   

    for bonus in bonus_list:
        bonus.rect.y += bonus.speed
        if bonus.rect.y > H - 10:
            if bonus.type == "life":
                count_life -= 1
            bonus.kill()
    if keys_klava[pg.K_SPACE]:
    if coins >= 10:
        sound_heart.play()
        coins -= 10
        count_life += 1
            
    draw()

    if count_life <= 0:
        break
    
for i in range(H // 2):
    root.blit(image_bg, (0,0))
    text_draw("Game is over", (200, i), 70, (255,0,0))
    pg.display.flip()

pg.time.wait(1000)    

pg.quit()
