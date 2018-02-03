from GameFrame import RoomObject


class Block(RoomObject):
    def __init__(self, room, x, y, image):
        RoomObject.__init__(self, room, x, y)

        self.set_image(image, 32, 32)
