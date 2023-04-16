import pygame
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Heli")
clock = pygame.time.Clock()
screen_width = size[0]
screen_height = size[1]
heli_right = pygame.image.load("heli_right.png")
heli_right = pygame.transform.scale(heli_right, (screen_width//10, screen_width//10))
heli_left = pygame.image.load("heli_left.png")
heli_left = pygame.transform.scale(heli_left, (screen_width//10, screen_width//10))

background_image = pygame.image.load("plx-5.png")
background_image = pygame.transform.scale(background_image, size)

x = screen_width // 2 - screen_width//20
y = screen_height // 2 - screen_width//20
flying = False
heading_right = True
background_x = 0

dx = 0
dy = 0
platforms = list()
brick_size = size[1] // 7
level = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
for i in range(len(level)):
    for j in range(len(level[i])):
        if level[i][j] == 1:
            platforms.append(pygame.Rect(j*brick_size, i*brick_size, brick_size, brick_size))
game_over = False
while not game_over:
    if flying:
        dy -= 1
    else:
        dy += 0.5
    x = x + dx
    heli_rect = pygame.Rect(x, y, screen_width//10, screen_width//12)
    for platform in platforms:
        if heli_rect.colliderect(platform):
            x = x - dx

    y = y + dy
    heli_rect = pygame.Rect(x, y, screen_width//10, screen_width//12)
    for platform in platforms:
        if heli_rect.colliderect(platform):
            y = y - dy
            dy = 0

    if x + background_x > size[0] * 3/4:
        background_x = size[0] * 3/4 - x
    if x + background_x < size[0] * 1/4:
        background_x = size[0] * 1/4 - x

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                heading_right = True
                dx = 7
            if event.key == pygame.K_LEFT:
                heading_right = False
                dx = -7
            if event.key == pygame.K_UP:
                flying = True
            if event.key == pygame.K_DOWN:
                dy = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if dx > 0:
                    dx = 0
            if event.key == pygame.K_LEFT:
                if dx < 0:
                    dx = 0
            if event.key == pygame.K_UP:
                if dy < 0:
                    dy = 0
                flying = False
            if event.key == pygame.K_DOWN:
                if dy > 0:
                    dy = 0
    screen.fill((255, 255, 255))
    screen.blit(background_image, (background_x % size[0], 0))
    screen.blit(background_image, (background_x % size[0] - size[0], 0))
    for platform in platforms:
        pygame.draw.rect(screen, (120, 0, 0), (
            platform.x + background_x,
            platform.y,
            platform.width,
            platform.height,
        ))
    if heading_right:
        screen.blit(heli_right, (x + background_x, y))
    else:
        screen.blit(heli_left, (x + background_x, y))
    pygame.display.flip()
    clock.tick(20)

pygame.quit()