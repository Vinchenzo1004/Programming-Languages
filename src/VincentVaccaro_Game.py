# MyPygame
# Vincent Vaccaro
# ProgLang
# 9/25/24

import pygame
import sys

from scripts.utilities import load_image, load_images
from scripts.entities import PhysicsEntity

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Vince\'s Game')

        scr_res = (640, 480)
        self.screen = pygame.display.set_mode(scr_res)

        self.clock = pygame.time.Clock()

        self.display_res = (320, 240)
        self.display = pygame.Surface(self.display_res)

        self.square_size = 50

        total_square_width = self.square_size * 3
        remaining_space = self.display_res[0] - total_square_width
        self.gap = remaining_space // 4

        self.movement = [False, False, False, False]

        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        self.square = [
            {'rect': pygame.Rect(self.gap, 95, self.square_size, self.square_size), 'planted': False, 'growth': 0, 'growing': False},
            {'rect': pygame.Rect(self.gap * 2 + self.square_size, 95, self.square_size, self.square_size), 'planted': False, 'growth': 0, 'growing': False},
            {'rect': pygame.Rect(self.gap * 3 + self.square_size * 2, 95, self.square_size, self.square_size), 'planted': False, 'growth': 0, 'growing': False}
        ]

        self.assets = {
            'player': load_image('entities/Fall.png'),
            'cursor': pygame.transform.scale(load_image('utils/watering_can.png'), (64, 72))
        }

        self.cursor_rect = self.assets['cursor'].get_rect()
        pygame.mouse.set_visible(False)

    def run(self):
        while True:

            self.display.fill((255, 255, 255))

            for square in self.square:
                pygame.draw.rect(self.display, (150, 75, 0), square['rect'])

                if self.player.rect.colliderect(square['rect']) and not square['planted']:
                    square['planted'] = True
                    square['growth'] = 10
                    print(f"Planted a square at {square['rect'].topleft}")

                if square['growing'] and square['growth'] < self.square_size:
                    square['growth'] += 0.01     #You're welcome

                if square['planted'] and square['growth'] >= self.square_size:
                    if self.player.rect.colliderect(square['rect']):
                        square['planted'] = False
                        square['growth'] = 0
                        square['growing'] = False
                        print(f"Collected a plant at {square['rect'].topleft}")

                if square['planted']:
                    growth_size = square['growth']
                    growth_rect = pygame.Rect(
                        square['rect'].x + (self.square_size - growth_size) // 2,
                        square['rect'].y + (self.square_size - growth_size) // 2,
                        growth_size,
                        growth_size
                    )
                    pygame.draw.rect(self.display, (0, 255, 0), growth_rect)

            x = self.movement[1] - self.movement[0]
            y = self.movement[3] - self.movement[2]
            self.player.update((x, y))
            self.player.render(self.display)

            self.cursor_rect.topleft = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    scaled_mouse_pos = (
                        mouse_pos[0] * self.display_res[0] // self.screen.get_width(),
                        mouse_pos[1] * self.display_res[1] // self.screen.get_height()
                    )

                    for square in self.square:
                        if square['planted'] and square['rect'].collidepoint(scaled_mouse_pos):
                            square['growing'] = True
                            print(f"Started growing at {square['rect'].topleft}")

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            self.screen.blit(self.assets['cursor'], self.cursor_rect.topleft)
            pygame.display.update()
            self.clock.tick(60)

Game().run()
