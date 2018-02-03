from GameFrame import RoomObject


class BlockDoor(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('block.png')
        self.set_image(image, 32, 32)

        # - Set depth higher than the player so the player goes under the brick - #
        self.depth = 20
