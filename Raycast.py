import pygame
import math
import sys

# Configurações da tela
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
HALF_HEIGHT = SCREEN_HEIGHT // 2
FOV = math.pi / 3
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(FOV / 2))
PROJ_COEFF = 3 * DIST * 40
SCALE = SCREEN_WIDTH // NUM_RAYS

# Mapa (1 = parede, 0 = espaço)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
TILE = 64

# Jogador
player_pos = [TILE + TILE // 2, TILE + TILE // 2]
player_angle = 0
player_pitch = 0  # ângulo vertical (pitch)

# Inicialização
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Ativa o controle por mouse
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

def mapping(x, y):
    return int(x // TILE), int(y // TILE)

def ray_casting(player_pos, player_angle, player_pitch):
    cur_angle = player_angle - FOV / 2
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = player_pos[0] + depth * cos_a
            y = player_pos[1] + depth * sin_a

            i, j = mapping(x, y)
            if 0 <= i < len(MAP[0]) and 0 <= j < len(MAP):
                if MAP[j][i] == 1:
                    depth *= math.cos(player_angle - cur_angle)
                    proj_height = min(int(PROJ_COEFF / (depth + 0.0001)), SCREEN_HEIGHT)
                    color = 255 / (1 + depth * depth * 0.0001)
                    vertical_offset = int(player_pitch * 150)  # controla olhar vertical
                    pygame.draw.rect(screen, (color, color, color),
                                     (ray * SCALE,
                                      HALF_HEIGHT - proj_height // 2 + vertical_offset,
                                      SCALE,
                                      proj_height))
                    break
        cur_angle += DELTA_ANGLE

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Movimento com W, A, S, D
    speed = 3
    dx = dy = 0
    if keys[pygame.K_w]:
        dx += speed * math.cos(player_angle)
        dy += speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        dx -= speed * math.cos(player_angle)
        dy -= speed * math.sin(player_angle)
    if keys[pygame.K_d]:
        dx -= speed * math.sin(player_angle)
        dy += speed * math.cos(player_angle)
    if keys[pygame.K_a]:
        dx += speed * math.sin(player_angle)
        dy -= speed * math.cos(player_angle)

    # Colisão com margem
    offset = 10
    next_x = player_pos[0] + dx
    next_y = player_pos[1] + dy

    ix, iy = int(player_pos[0] // TILE), int(player_pos[1] // TILE)
    nx, ny = int((next_x + offset * math.copysign(1, dx)) // TILE), iy
    if MAP[iy][nx] == 0:
        player_pos[0] = next_x

    nx, ny = ix, int((next_y + offset * math.copysign(1, dy)) // TILE)
    if MAP[ny][ix] == 0:
        player_pos[1] = next_y

    # Rotação com mouse (yaw e pitch)
    rel_x, rel_y = pygame.mouse.get_rel()
    player_angle += rel_x * 0.003

    player_pitch -= rel_y * 0.003
    player_pitch = max(-math.pi / 1, min(math.pi / 1, player_pitch))  # limita pitch

    # Desenho
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (100, 100, 100), (0, 0, SCREEN_WIDTH, HALF_HEIGHT))
    pygame.draw.rect(screen, (50, 50, 50), (0, HALF_HEIGHT, SCREEN_WIDTH, HALF_HEIGHT))

    ray_casting(player_pos, player_angle, player_pitch)
    pygame.display.flip()
    clock.tick(60)
