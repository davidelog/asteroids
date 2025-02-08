import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0
    
    user = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while 1>0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit game with x button
                return
        screen.fill((0, 0, 0))
        user.draw(screen)
        pygame.display.flip()
        dt = fps_clock.tick(60) / 1000

if __name__ == "__main__":
    main()