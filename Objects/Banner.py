from GameFrame import RoomObject


class Banner(RoomObject):
    def __init__(self, room, x, y):
        super().__init__(room, x, y)

        image = self.load_image('banner.png')
        self.set_image(image, 800, 56)
        self.depth = 100
