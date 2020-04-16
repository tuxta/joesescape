import pygame
from GameFrame import RoomObject


class Player(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        player = self.load_image('player.png')
        self.player_left = self.load_image('player_left.png')
        self.player_right = self.load_image('player_right.png')
        self.set_image(player, 25, 32)
        self.depth = 5

        self.gravity = 0

        self.handle_key_events = True

        # -- Register the objects with which -- #
        # -- this object handles collisions  -- #
        self.register_collision_object('Block')
        self.register_collision_object('Goal')
        self.register_collision_object('Monster')
        self.register_collision_object('Monster2')

    def handle_collision(self, other, other_type):
        if other_type == 'Block':
            self.blocked()
            if self.rect.centery < other.rect.top:
                self.y_speed = 0
                self.gravity = 0
                self.y = other.rect.top - self.height
        elif other_type == 'Goal':
            self.room.running = False
        elif other_type == 'Monster' or other_type == 'Monster2':
            self.x = 64
            self.y = 15*32
            self.room.update_lives(-1)

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.move_right()
        elif key[pygame.K_RIGHT]:
            self.move_left()
        if key[pygame.K_SPACE]:
            self.jump()

    def joy_pad_signal(self, p1_buttons, p2_buttons):
        if p1_buttons[11] < -0.5:
            self.move_right()
        elif p1_buttons[11] > 0.5:
            self.move_left()
        if p1_buttons[2]:
            self.jump()

    def move_right(self):
        self.set_image(self.player_left, 25, 32)
        self.x -= 4
        if not self.collides_at(self, 0, 4, 'Block'):
            self.gravity = 1

    def move_left(self):
        self.set_image(self.player_right, 25, 32)
        self.x += 4
        if not self.collides_at(self, 0, 4, 'Block'):
            self.gravity = 1

    def jump(self):
        if self.collides_at(self, 0, 1, 'Block'):
            self.y_speed = -15
            self.gravity = 1