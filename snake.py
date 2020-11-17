import pygame
import time
pygame.init()

# Sets and updates Display
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Jonathan')

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

# Main
game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


# Defines message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # Game Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True

    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(snake_speed)

message('You lost', red)
pygame.display.update()
time.sleep(1.5)

pygame.quit()
quit()
