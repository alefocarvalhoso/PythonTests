import pygame
import os
from pygame.locals import *
import random
import time
import webbrowser

pygame.init()

screen = pygame.display.set_mode((582, 488))

#Ideia do jogo: controle o quadrado vermelho até o quadrado azsul, que estará fugindo constantemente, quando quadrado vermelho encostar no azul, aperte a tecla de espaço para marcar um ponto.

points = 0

Player_pos_y = 30
Player_pos_x = 30

player_speed = 2

BOT_SIZE = 23
bot_pos = pygame.Vector2(582/ 2, 488 / 2)
bot_target = pygame.Vector2(random.randint(0, 582 - BOT_SIZE), random.randint(0, 488 - BOT_SIZE))
bot_speed = 200 
wait_time = 1000
last_arrival_time = 0

clock = pygame.time.Clock()

url_1 = "https://music.youtube.com/watch?v=7Tzq6isGOjg&list=RDAMVM7Tzq6isGOjg"
url_2 = "https://ibb.co/mFrLwfRJ"

ChikenIcon = pygame.image.load('IconChiken.png')

while True:
    dt = clock.tick(60) / 1000
    screen.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == QUIT or pygame.key.get_pressed()[K_ESCAPE]:
            pygame.quit()
            exit()
        
  
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                if red_square.colliderect(blue_square):
                    bot_speed += 4
                    player_speed += 2
                    points += 1
                    print(bot_speed)
                    Player_pos_x = random.randrange(488, 582)
                    Player_pos_y = random.randrange(488, 582)
                else:
                    player_speed -= 2
                    points -= 1

    direction = (bot_target - bot_pos)
    distance = direction.length()

    if distance > 1:
        direction.normalize_ip()
        bot_pos += direction * bot_speed * dt
    else:
        
        if pygame.time.get_ticks() - last_arrival_time > wait_time:
            bot_target = pygame.Vector2(random.randint(0, 582 - BOT_SIZE), random.randint(0, 488 - BOT_SIZE))
            last_arrival_time = pygame.time.get_ticks()

    red_square = pygame.draw.rect(screen, (255, 0, 0), (Player_pos_x, Player_pos_y, 23, 23))
    blue_square = pygame.draw.rect(screen, (0, 0, 255), (bot_pos.x, bot_pos.y, 23, 23))


    if pygame.key.get_pressed()[K_s]:
        Player_pos_y += player_speed
    if pygame.key.get_pressed()[K_w]:
        Player_pos_y -= player_speed
    if pygame.key.get_pressed()[K_d]:
        Player_pos_x += player_speed
    if pygame.key.get_pressed()[K_a]:
        Player_pos_x -= player_speed
    
    Player_pos_x = max(0, min(Player_pos_x, 582 - 23))
    Player_pos_y = max(0, min(Player_pos_y, 488 - 23))



    pygame.display.update()
    pygame.display.set_caption(f"Chiken Runner-beta, Points: {points}")
    pygame.display.set_icon(ChikenIcon)

    if player_speed <= 0:
        pygame.quit()
    if points >= 1:
        webbrowser.open(url_1)
        webbrowser.open(url_2)
        pygame.quit()
       
    



