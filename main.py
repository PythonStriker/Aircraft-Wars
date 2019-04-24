__author__ = 'PythonStriker'

import pygame
import sys
import traceback
import myplane
import enemy
import bullet
import supply
import threading
from pygame.locals import *
from random import *
from tkinter import *
from PIL import Image,ImageTk
import pay.pay
import pay.self_Alipay
import time

APPID = 2016092600601253
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA0ZmM9+lQRa0VkHsUTywF0msOVUrXIupBIp0f3T6TPT/tGrHfut3VtiO/c3Ota8YnaqxFfXui4rF5DtidOs32bJdvq4L0aOnOSeE9g/JDwG7X+GeQ3e0pzfNxLhEFlULt8ks+N4A+mVH+E1Fdy07FnyEF/JmuPjIq/2SfbgwghOgda5dP3rKE5VeOlgUL2pJWA2ZbzMZHQ+iAsQKfx2NzIRiygo89GFE8knOKweWqHYFMiZ2y2J9QYMyBJrBIGh+PRiswMfBS6xpfupAf2u+8BTGMxhj+I6zs5JBP1upngD0YhpPifU+SSK3SjKF19dJImJWqhaZD0vQdXzNJRkCMcQIDAQABAoIBAQC5+YrRNd2Z1Tf7GJounZsU1xTCrUMyobPlqJDrWGiAwkX5l7YyMj87+4AWSp+nrwyuY+jMrHUcu+f0OlNYKAPs2nmlLu76X+pAN3DDsKRZDIDo0cwCfjrHmKfl/gh8JgTHJegwisQAenX8YgfdKynCRiTvutSWLyFjtr6XgH8iLM8tYxkG8MYDuhpsPJ3ToZi17WZtGMduolOWMwBtYx3IfzukOTJnEsIMPLFl/zqw5/1700vm4MvMIalQ2eiU13WGfRywMyd/u4ISQJ6V4HNgbr7RRFBitt/bCMF+3rBd4mDSv9+iamzyYP0sjaSk3PZVxViIEHTfYJ8htVl8UShZAoGBAO1QH3tzq3KHOQ84i9FDSzyZG1tKcyvzAcb5bTXJTmHHsMW7zTtuWTe8Ki1eeoh9USHY+v5jFG+Kyt4ej2Yez9UT8wlYvHOspkKx1TZb/3cYQ8txQkQKgb00XwRVzyqEia3jkgGTY8AVPdw9UZTIJ37Sj45gq0Wk8lcrzFFU2ornAoGBAOIaxXOA2MoYdHVRPTTHVkJ5YkoG7/0S9eCok+EVsKTJnm0VInXi5Uk+/72T8qbr1gw54/DlBqdEGGrWUHCmz7ro2tVInpQ0lnY8muTjhSu2o0CNV9VfAMDcyUgE7mhPJkx1Kplh1WypBqQTKalTxG5rm87eAB85lCSqi/8PCFrnAoGBAMVXFXbxTybj770KhqozzYLMxwT5OiDX6ShvDjPl/Lou9n7XlujO8H36iRBFOpv5qdf9uWqFNd8ziVOAEjsXcDh+aGHjWoLOlUts2iJkCmIc2XN58WLnYc/WlxThzm5K3LqvPSD2UcLPZyuYChkxADbkHeCF3qcBbUyz7SnM6BcNAoGAHpkq4W+tZuQaVooQ82SKiuJsZ8I6lhAL0ERgBtTtm89hLjfu+u8iwl/RMjGkY+yEghEPhNkpplczyrmIF0ar1AqRGs4CD+Jx/jxDZfhYXEsSGrlGCq0Zp//5CVMJhHo5n503j5xKyrKxIGErgSvB6IONiVhHwfID11ZxLao2Ij8CgYBUp6BHP2pS5gS/B421dWjrddVGUDzd5hws4FU3QzQOi1Wp4W2yTX7dhPC6MvpG4TikWN58eO2Jw1lIAF10ZBXwp6r6C0XKEwdrT9+xYen2fQLB9tZef/5eEe3tvxASP5eDBSL6c5+nIK/X6F+6KDtSwQXl0pI4ZvYvBaJcvYYmcw==
-----END RSA PRIVATE KEY-----
'''
public_key = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuNcQoWf8TzYF1fhtmcTSytdRNhV8P+GkSUrn9aq7SKdW7MrI3i6qKXweNBtakgQlMBDcOjYU9qq4QpzouIO92IpNr51+S92pUuFlVA+Dmmp1Gw2hf6EQihYkIvS6sNJ6u/dJj0+GLr3/JKXgw0AanvxFMyaca5GxsAk41g+h3nYPKVWrXpisEKwvnSFQxZ8+BHJYu9BRC3XLO+y82HP9Ay10hsU3m7WrMfSoY5p1TuUDWFPax7oMfvLcZDewSiTorkKOJX7Xej0S5Jfy5uImY5wf3VePxNgP1V32+BpEsHRO8bZjuFtCpx/pR6HSXOBvAUIIRIqQ31SKfhO8Z5dufwIDAQAB
-----END PUBLIC KEY-----
'''

Pay_or_not = False
thread = False

pygame.init()
pygame.mixer.init()

bg_size=width,height=400,700
screen=pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")


global background
background=pygame.image.load("images/background1.png").convert()
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
WHITE=(255,255,255)

# 载入游戏音乐
pygame.mixer.music.load("sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def add_small_enemies(group1,group2,num):
    for i in range(num):
        e1=enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1,group2,num):
    for i in range(num):
        e2=enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)

def add_big_enemies(group1,group2,num):
    for i in range(num):
        e3=enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)

def inc_speed(target,inc):
    for each in target:
        each.speed+=inc


def main():
    global background
    background = pygame.image.load("images/background1.png").convert()
    pygame.mixer.music.play(-1)
    #生成我方飞机
    me=myplane.MyPlane(bg_size)

    #中弹图片索引
    e1_destroy_index=0
    e2_destroy_index=0
    e3_destroy_index=0
    me_destroy_index=0
    
    enemies=pygame.sprite.Group()
    #生成敌方小型飞机
    small_enemies=pygame.sprite.Group()
    add_small_enemies(small_enemies,enemies,15)
    #生成敌方中型飞机
    mid_enemies=pygame.sprite.Group()
    add_mid_enemies(mid_enemies,enemies,4)
    #生成敌方大型飞机
    big_enemies=pygame.sprite.Group()
    add_big_enemies(big_enemies,enemies,2)

    #统计得分
    score=0
    score_font=pygame.font.Font("font/font.ttf",36)

    #标志是否暂停游戏
    paused=False
    paused_nor_image=pygame.image.load("images/pause_nor.png").convert_alpha()
    paused_pressed_image=pygame.image.load("images/pause_pressed.png").convert_alpha()
    resume_nor_image=pygame.image.load("images/resume_nor.png").convert_alpha()
    resume_pressed_image=pygame.image.load("images/resume_pressed.png").convert_alpha()
    paused_rect=paused_nor_image.get_rect()
    paused_rect.left,paused_rect.top=width-paused_rect.width-10,10
    paused_image=paused_nor_image

    #游戏结束画面
    gameover_font = pygame.font.Font("font/font.TTF", 48)
    again_image = pygame.image.load("images/again.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("images/gameover.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    #设置难度级别
    level=3

    #全屏炸弹
    bomb_image=pygame.image.load("images/bomb.png").convert_alpha()
    bomb_rect=bomb_image.get_rect()

    bomb_font=pygame.font.Font("font/font.ttf",48)
    bomb_num=3

    #超级子弹定时器
    DOUBLE_BULLET_TIME=USEREVENT+1

    #解除我方无敌状态定时器
    INVINCIBLE_TIME=USEREVENT+2    

    #标志是否使用超级子弹
    is_double_bullet=False
    

    #每15秒发送一个补给包
    bullet_supply=supply.Bullet_Supply(bg_size)
    bomb_supply=supply.Bomb_Supply(bg_size)
    SUPPLY_TIME=USEREVENT
    pygame.time.set_timer(SUPPLY_TIME,15*1000)
    
    

    #生成普通子弹
    bullet1=[]
    bullet1_index=0
    BULLET1_NUM=4
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(me.rect.midtop))

     #生成超级子弹
    bullet2=[]
    bullet2_index=0
    BULLET2_NUM=8
    for i in range(BULLET2_NUM):
        bullet2.append(bullet.Bullet2((me.rect.centerx-33,me.rect.centery)))
        bullet2.append(bullet.Bullet2((me.rect.centerx+30,me.rect.centery)))
    
                
    clock=pygame.time.Clock()

    #用于替换图片
    switch_image=True

    #用于延迟
    delay=100

    running=True

    #生命数量
    life_image=pygame.image.load("images/life.png").convert_alpha()
    life_rect=life_image.get_rect()
    life_num=3

    #用于限制重复打开记录文件
    recorded=False

    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONDOWN:
                if event.button==1 and paused_rect.collidepoint(event.pos):
                    paused=not paused
                    if paused:
                        pygame.time.set_timer(SUPPLY_TIME,0)
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.time.set_timer(SUPPLY_TIME,30*1000)
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    if bomb_num>0:
                        bomb_num-=1
                        bomb_sound.play()
                        for each in enemies:
                            if each.rect.bottom>0:
                                each.active=False
                    else:
                        pass
            elif event.type==SUPPLY_TIME:
                supply_sound.play()
                if choice([True, False]):
                    bomb_supply.reset()
                else:
                    bullet_supply.reset()

            elif event.type==DOUBLE_BULLET_TIME:
                is_double_bullet=False
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)
            elif event.type==INVINCIBLE_TIME:
                me.invincible=False
                pygame.time.set_timer(INVINCIBLE_TIME,0)
                            
            elif event.type==MOUSEMOTION:
                if paused_rect.collidepoint(event.pos):
                    if paused:
                        paused_image=resume_pressed_image
                    else:
                        paused_image=paused_pressed_image
                else:
                    if paused:
                        paused_image=resume_nor_image
                    else:
                        paused_image=paused_nor_image

        #根据用户的得分增加难度
        if level==1 and int(score)>50000:
            level=2
            background = pygame.image.load("images/background3.png").convert()
            upgrade_sound.play()
            #增加3加小型敌机、2加中型敌机、1加大型敌机
            add_small_enemies(small_enemies,enemies,3)
            add_mid_enemies(mid_enemies,enemies,2)
            add_big_enemies(big_enemies,enemies,1)
            #提升小型敌机的速度
            inc_speed(small_enemies,1)
        elif level==2 and int(score)>300000:
            level=3
            background = pygame.image.load("images/background2.png").convert()
            upgrade_sound.play()
            #增加3加小型敌机、2加中型敌机、1加大型敌机
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            #提升小型敌机的速度
            inc_speed(small_enemies,1)
            inc_speed(mid_enemies,1)
        elif level==3 and int(score)>600000:
            level=4
            background = pygame.image.load("images/background4.png").convert()
            upgrade_sound.play()
            #增加3加小型敌机、2加中型敌机、1加大型敌机
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            #提升小型敌机的速度
            inc_speed(small_enemies,1)
            inc_speed(mid_enemies,1)
        elif level==4 and int(score)>1000000:
            level=5
            background = pygame.image.load("images/background1.png").convert()
            upgrade_sound.play()
            #增加3加小型敌机、2加中型敌机、1加大型敌机
            add_small_enemies(small_enemies,enemies,5)
            add_mid_enemies(mid_enemies,enemies,3)
            add_big_enemies(big_enemies,enemies,2)
            #提升小型敌机的速度
            inc_speed(small_enemies,1)
            inc_speed(mid_enemies,1)
        
        
        screen.blit(background,(0,0))
        if life_num and not paused:
            # 检测用户的键盘操作
            key_pressed=pygame.key.get_pressed()

            if key_pressed[K_w] or key_pressed[K_UP]:
                me.moveUp()
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.moveDown()
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.moveLeft()
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.moveRight()

            # 绘制全屏炸弹补给并检测是否获得
            if bomb_supply.active:
                bomb_supply.move()
                screen.blit(bomb_supply.image,bomb_supply.rect)
                if pygame.sprite.collide_mask(bomb_supply,me):
                    get_bomb_sound.play()
                    if bomb_num<3:
                        bomb_num+=1
                    bomb_supply.active=False

            # 绘制超级子弹补给并检测是否获得
            if bullet_supply.active:
                bullet_supply.move()
                screen.blit(bullet_supply.image,bullet_supply.rect)
                if pygame.sprite.collide_mask(bullet_supply,me):
                    get_bullet_sound.play()
                    #发射超级子弹
                    is_double_bullet=True
                    pygame.time.set_timer(DOUBLE_BULLET_TIME,18*1000)
                    bullet_supply.active=False
                    
            #发射子弹
            if not(delay%10):
                bullet_sound.play()
                if is_double_bullet:
                    bullets=bullet2
                    bullets[bullet2_index].reset((me.rect.centerx-33,me.rect.centery))
                    bullets[bullet2_index+1].reset((me.rect.centerx+30,me.rect.centery))
                    bullet2_index=(bullet2_index+2)%BULLET2_NUM
                else:
                    bullets=bullet1 
                    bullets[bullet1_index].reset(me.rect.midtop)
                    bullet1_index=(bullet1_index+1)%BULLET1_NUM


            #检测子弹是否击中敌机
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image,b.rect)
                    enemy_hit=pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)
                    if enemy_hit:
                        b.active=False
                        for e in enemy_hit:
                            if e in mid_enemies or e in big_enemies:
                                e.energy-=1
                                e.hit=True
                                if e.energy==0:
                                    e.active=False
                            else:
                                e.active=False

            #绘制大型敌机
            for each in big_enemies:
                if each.active:            
                    each.move()
                    if each.hit:
                        #绘制被打到的特效
                        screen.blit(each.image_hit,each.rect)
                        each.hit=False
                    else:    
                        if switch_image:
                            screen.blit(each.image1,each.rect)
                        else:
                            screen.blit(each.image2,each.rect)


                    #绘制血槽
                    pygame.draw.line(screen,BLACK,\
                                     (each.rect.left,each.rect.top-5),\
                                     (each.rect.right,each.rect.top-5),\
                                     2)
                    #当生命大于20%，显示绿色，否则显示红色
                    energy_remain=each.energy/enemy.BigEnemy.energy
                    if energy_remain>0.2:
                        energy_color=GREEN
                    else:
                        energy_color=RED
                    pygame.draw.line(screen,energy_color,\
                                     (each.rect.left,each.rect.top-5),\
                                     (each.rect.left+each.rect.width*energy_remain,each.rect.top-5),\
                                     2)
                        
                    #即将出现在画面中，播放音效
                    if each.rect.bottom==-50:
                        enemy3_fly_sound.play(-1)
                    
                else:
                    #毁灭
                    if not(delay%3):
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)
                        if e3_destroy_index==0:
                            enemy3_down_sound.play()
                        e3_destroy_index=(e3_destroy_index+1)%6
                        if e3_destroy_index==0:
                            each.reset()
                            score+=10000
                            enemy3_fly_sound.stop()
                        
            #绘制中型敌机
                for each in mid_enemies:
                    if each.active:
                        each.move()
                        if each.hit:
                            #绘制被打到的特效
                            screen.blit(each.image_hit,each.rect)
                            each.hit=False
                
                        else:
                            screen.blit(each.image,each.rect)
                        #绘制血槽
                        pygame.draw.line(screen,BLACK,\
                                         (each.rect.left,each.rect.top-5),\
                                         (each.rect.right,each.rect.top-5),\
                                         2)
                        #当生命大于20%，显示绿色，否则显示红色
                        energy_remain=each.energy/enemy.MidEnemy.energy
                        if energy_remain>0.2:
                            energy_color=GREEN
                        else:
                            energy_color=RED
                        pygame.draw.line(screen,energy_color,\
                                         (each.rect.left,each.rect.top-5),\
                                         (each.rect.left+each.rect.width*energy_remain,each.rect.top-5),\
                                         2)
                    else:
                        #毁灭
                        if not(delay%3):
                            if e2_destroy_index==0:
                                enemy2_down_sound.play()
                            screen.blit(each.destroy_images[e2_destroy_index],each.rect)
                            e2_destroy_index=(e2_destroy_index+1)%4
                            if e2_destroy_index==0:
                                score+=6000
                                each.reset()
                            
                                
             #绘制小型敌机
                for each in small_enemies:
                    if each.active:
                        each.move()
                        screen.blit(each.image,each.rect)
                    else:
                        #毁灭
                        if not(delay%3):
                            if e1_destroy_index==0:
                                enemy1_down_sound.play()
                            screen.blit(each.destroy_images[e1_destroy_index],each.rect)
                            e1_destroy_index=(e1_destroy_index+1)%4
                            if e1_destroy_index==0:
                                score+=1000
                                each.reset()
                                
            #检测我方飞机是否被撞
            enemies_down=pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)
            if enemies_down and not me.invincible:
                me.active=False
                for e in enemies_down:
                    e.active=False
            

            #绘制我方飞机
            if me.active:               
                if switch_image:
                    screen.blit(me.image1,me.rect)
                else:
                    screen.blit(me.image2,me.rect)
            else:
                #毁灭
                if not(delay%3):
                    screen.blit(me.destroy_images[me_destroy_index],me.rect)
                    if me_destroy_index==0:
                        me_down_sound.play()
                    me_destroy_index=(me_destroy_index+1)%4
                    if me_destroy_index==0:
                        life_num-=1
                        me.reset()
                        pygame.time.set_timer(INVINCIBLE_TIME,3*1000)
                        
                        
            # 绘制全屏炸弹数量
            bomb_text=bomb_font.render("× %d" % bomb_num,True,WHITE)
            text_rect=bomb_text.get_rect()
            screen.blit(bomb_image,(10,height-10-bomb_rect.height))
            screen.blit(bomb_text,(20+bomb_rect.width,height-5-bomb_rect.height))

            #绘制剩余生命数量
            if life_num:
                for i in range(life_num):
                    screen.blit(life_image,\
                                (width-10-(i+1)*life_rect.width,\
                                 height-10-life_rect.height))
            score_text=score_font.render("Score : %s"% str(score),True,WHITE)
            screen.blit(score_text,(10,5))

        #绘制游戏结束画面
        elif life_num==0:
            background = pygame.image.load("images/background5.png").convert()
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            pygame.time.set_timer(SUPPLY_TIME,0)
            #读取历史最高得分
            if not recorded:
                recorded=True
                score = str(score)
                break_flag = 0
                count = 0
                f = open("record.txt", "r", encoding="utf-8")
                lines = f.readlines()
                for i in range(len(lines)):
                    lines[i] = lines[i].replace('\n', '')
                if score not in lines:
                    for i in range(len(lines)):
                        if eval(lines[i]) < eval(score):
                            lines.insert(i, score)
                            break_flag = 1
                            i = i + 1
                            break
                        elif eval(lines[i]) == eval(score):
                            break_flag = 1
                            i = i+1
                            break
                if score not in lines:
                    if not break_flag:
                        lines.append(score)
                        i = len(lines)+1
                f.close()
                f = open("record.txt", "w", encoding="utf-8")
                for line in lines:
                    f.write(line + '\n')
                f.close()
            #绘制结束界面
            record_score_text = score_font.render("Rank : " , True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            record_score_text1 = score_font.render("1.%d" % int(lines[0]), True, (255, 255, 255))
            record_score_text1_rect = record_score_text1.get_rect()
            record_score_text1_rect.left,record_score_text1_rect.top= \
                            (width - record_score_text1_rect.width)//2,90
            screen.blit(record_score_text1,record_score_text1_rect)

            record_score_text2 = score_font.render("2.%d" % int(lines[1]), True, (255, 255, 255))
            record_score_text2_rect = record_score_text2.get_rect()
            record_score_text2_rect.left, record_score_text2_rect.top = \
                (width - record_score_text2_rect.width) // 2, record_score_text1_rect.bottom+10
            screen.blit(record_score_text2, record_score_text2_rect)

            record_score_text3 = score_font.render("3.%d" % int(lines[2]), True, (255, 255, 255))
            record_score_text3_rect = record_score_text3.get_rect()
            record_score_text3_rect.left, record_score_text3_rect.top = \
                (width - record_score_text3_rect.width) // 2, record_score_text2_rect.bottom + 10
            screen.blit(record_score_text3, record_score_text3_rect)

            record_score_text4 = score_font.render("." , True, (255, 255, 255))
            record_score_text4_rect = record_score_text4.get_rect()
            record_score_text4_rect.left, record_score_text4_rect.top = \
                (width - record_score_text4_rect.width) // 2, record_score_text3_rect.bottom
            screen.blit(record_score_text4, record_score_text4_rect)

            record_score_text5 = score_font.render("%d."%i + str(score), True, (255, 255, 255))
            record_score_text5_rect = record_score_text5.get_rect()
            record_score_text5_rect.left, record_score_text5_rect.top = \
                (width - record_score_text5_rect.width) // 2, record_score_text4_rect.bottom
            screen.blit(record_score_text5, record_score_text5_rect)

            gameover_text1 = gameover_font.render("Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                                 (width - gameover_text1_rect.width) // 2, height // 2
            screen.blit(gameover_text1, gameover_text1_rect)
            
            gameover_text2 = gameover_font.render(str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                                 (width - gameover_text2_rect.width) // 2, \
                                 gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                             (width - again_rect.width) // 2, \
                             gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                                (width - again_rect.width) // 2, \
                                again_rect.bottom +10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                   again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    pay_page()
                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                     gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()


        #绘制暂停按钮
        screen.blit(paused_image,paused_rect)
                
        if not(delay%5):
            switch_image=not switch_image
            
        delay-=1

        if not delay:
            delay=100
            
        pygame.display.flip()

        clock.tick(60)

def pay_page():
    global Pay_or_not
    global thread
    if (not Pay_or_not) and (not thread) :
        root = Tk()
        root.geometry('170x170+800+400')
        root.resizable(width=False, height=False)
        # -------------------------------------------------------------------------------------------------------------------#
        alipay = pay.self_Alipay.alipay(APPID, private_key, public_key)
        orderNumber = increase_OrderNumber()
        payer = pay.pay.pay(out_trade_no=orderNumber, total_amount=6, subject="relive", timeout_express='5m')
        dict = alipay.trade_pre_create(out_trade_no=payer.out_trade_no, total_amount=payer.total_amount,
                                       subject=payer.subject, timeout_express=payer.timeout_express)
        payer.get_qr_code(dict['qr_code'])
        # -------------------------------------------------------------------------------------------------------------------#
        load = Image.open('.\pay\qrcode_image\qr_test_ali.png')
        resized = load.resize((128, 128))
        resized.save(".\pay\qrcode_image\\test.png")
        load = Image.open('.\pay\qrcode_image\\test.png')
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        prompt = Label(root, text='支付宝扫码获得永久复活(6元)')
        prompt.grid(row=0, column=0)
        img.grid(row=1, column=0)
        root.title('飞机大战支付页面')
        def Pay_ensure(payer):
            global Pay_or_not
            for i in range(1, 100):
                print(i)
                time.sleep(10)
                print(payer.out_trade_no)
                Pay_or_not = payer.query_order(payer.out_trade_no)
                if Pay_or_not:
                    root.destroy()
                    main()
                    break
        thread = threading.Thread(target=Pay_ensure, args=(payer,))
        thread.start()
        root.mainloop()
    elif (not Pay_or_not) and thread:
        root = Tk()
        root.geometry('170x170+800+400')
        root.resizable(width=False, height=False)
        load = Image.open('.\pay\qrcode_image\\test.png')
        render = ImageTk.PhotoImage(load)
        img = Label(root, image=render)
        prompt = Label(root, text='支付宝扫码获得永久复活(6元)')
        prompt.grid(row=0, column=0)
        img.grid(row=1, column=0)
        root.title('飞机大战支付页面')
        root.mainloop()
    else:
        main()

def increase_OrderNumber():
    f = open('.\\pay\\PayDocument.txt', 'r')
    string = f.read()
    f.close()
    f = open('.\\pay\\PayDocument.txt', 'w')
    string = str(eval(string) + 1)
    f.write(str(string))
    f.close()
    f = open('.\\pay\\PayDocument.txt', 'r')
    string = f.read()
    f.close()
    return string

if __name__=="__main__":
    try:
       main()
    except SystemExit:
        pass
    except:
       traceback.print_exc()
       pygame.quit()
       input()
