from GameFrame import RoomObject


class Goal(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('goal.png')
        self.set_image(image, 32, 32)
