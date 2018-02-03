from GameFrame import RoomObject


class Monster(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('monster.png')
        self.set_image(image, 32, 32)

        self.x_speed = -6

        self.register_collision_object('Block')

    def handle_collision(self, other):
        if type(other).__name__ == 'Block':
            self.x_speed *= -1
