from pygame import joystick, pygame

class Dualshock4:
    def __init__(self):
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def getCross(self):
        return self.controller.get_button(1)

    def getSquare(self):
        return self.controller.get_button(0)

    def getTriangle(self):
        return self.controller.get_button(3)

    def getCircle(self):
        return self.controller.get_button(2)

    def getL1(self):
        return self.controller.get_button(4)

    def getL2(self):
        return self.controller.get_button(6)

    def getL3(self):
        return self.controller.get_button(10)

    def getR1(self):
        return self.controller.get_button(5)

    def getR2(self):
        return self.controller.get_button(7)

    def getR3(self):
        return self.controller.get_button(11)
    
    def getLeftStick(self):
        return (self.controller.get_axis(0), self.controller.get_axis(1))  # Return value as (X,Y) tuple

    def getRightStick(self):
        return (self.controller.get_axis(2), self.controller.get_axis(3))  # Return value as (X,Y) tuple