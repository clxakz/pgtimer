import pygame
from pgtimer.pgtimer import Timer

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


class Cube():
    def __init__(self, x, y):
        self.surface = pygame.Surface((100,100))
        self.surface.fill((255,255,255))

        self.rect = self.surface.get_frect(center=(x, y))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)

cube = Cube(100, 100)


def animate():
    Timer.tween(1, cube.rect.centerx, 400, lambda v: setattr(cube.rect, "centerx", v), "easeInOutQuad", lambda:             # Tween x position from 100 > 400
        Timer.tween(1, cube.rect.centery, 400, lambda v: setattr(cube.rect, "centery", v), "easeInOutQuad", lambda:         # Tween y position from 100 > 400
            Timer.tween(1, cube.rect.centerx, 100, lambda v: setattr(cube.rect, "centerx", v), "easeInOutQuad", lambda:     # Tween x position from 400 > 100
                Timer.tween(1, cube.rect.centery, 100, lambda v: setattr(cube.rect, "centery", v), "easeInOutQuad", animate # Tween y position from 400 > 100 and repeat
                )
            )
        )
    )

animate()



running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Timer.update(dt)
    cube.draw(screen)

    pygame.display.flip()
pygame.quit()