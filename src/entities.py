# MyPygame: entities
# Vincent Vaccaro
# ProgLang
# 9/26/24

import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.width, self.height = size
        self.velocity = [0,0]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def update(self, movement = (0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

        self.rect.topleft = (self.pos[0], self.pos[1])

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.rect.topleft)
