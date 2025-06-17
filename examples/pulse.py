import pygame
from pytimerlib import Timer

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


surface = pygame.Surface((250, 250))
surface.fill((255,255,255))
alpha = 0

def set_alpha(value):
    global alpha
    alpha = value


def pulse():
    Timer.tween(1, 0, 255, set_alpha, "linear", lambda:         # Tween from 0 to 255
        Timer.after(1, lambda:                                  # Wait 1 second
            Timer.tween(1, 255, 0, set_alpha, "linear", pulse)  # Tween from 255 to 0 and repeat pulse
        )
    )

pulse()



running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Timer.update(dt)

    surface.set_alpha(alpha)
    screen.blit(surface, (125, 125))

    pygame.display.flip()
pygame.quit()