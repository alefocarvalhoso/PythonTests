import pygame as pg
from pygame.locals import *
import os
import sys



pg.init()


tela = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption("Cursor Position ")


font_path = os.path.join(os.path.dirname(__file__), 'FontePixel.ttf')
my_font = pg.font.Font(font_path, 15)

icon = pg.image.load('Icon.png')
pg.display.set_icon(icon)


col_yellow = (255, 0, 17)
col_red = (247, 250, 0)
col_blue = (0, 0, 255)
col_green = (0, 255, 0)
color_m1 = col_yellow  
color_m2 = col_yellow  


while True:
    tela.fill((0, 0, 0))  


    mouse_pos = pg.mouse.get_pos()
    mouse_pos_y = (mouse_pos[0], 0)
    mouse_pos_x = (0, mouse_pos[1])


    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 3: 
                color_m1 = col_red
            elif event.button == 1:
                color_m2 = col_red
            elif event.button == 4:
                color_m1 = col_blue
            elif event.button == 5:
                color_m1 = col_green
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 3: 
                color_m1 = col_yellow
            elif event.button == 1:
                color_m2 = col_yellow
     
      
      


    pg.draw.rect(tela, color_m1, (mouse_pos_y[0], 0, 13, 767))
    pg.draw.rect(tela, color_m2, (0, mouse_pos_x[1], 1365, 13))
    #pg.draw.rect(tela, color_m2, (0, 0, mouse_pos_y[0],mouse_pos_x[1]))


    text_surf = my_font.render(f"Mouse Position: {mouse_pos}", True, (255, 255, 255))
    tela.blit(text_surf, (20, 20))


    pg.mouse.set_visible(False)

    # Atualiza a tela
    pg.display.update()
