import pygame
from GameFrame import RoomObject


class Player(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('player.png')
        self.set_image(image, 25, 32)
        self.depth = 5

        self.gravity = 0

        self.handle_key_events = True

        # -- Register the objects with which -- #
        # -- this object handles collisions  -- #
        self.register_collision_object('Block')
        self.register_collision_object('Goal')
        self.register_collision_object('Monster')

    def handle_collision(self, other):
        other_type = type(other).__name__
        if other_type == 'Block':
            self.blocked()
            if self.rect.centery < other.rect.top:
                self.y_speed = 0
                self.gravity = 0
                self.y = other.rect.top - self.height
        elif other_type == 'Goal':
            self.room.running = False
        elif other_type == 'Monster':
            self.room.update_score(-1)
            self.x = 18*32
            self.y = 15*32

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 4
            if not self.collides_at(self, 0, 4, 'Block'):
                self.gravity = 1
        elif key[pygame.K_RIGHT]:
            self.x += 4
            if not self.collides_at(self, 0, 4, 'Block'):
                self.gravity = 1
        if key[pygame.K_SPACE]:
            if self.collides_at(self, 0, 1, 'Block'):
                self.y_speed = -17
                self.gravity = 1
