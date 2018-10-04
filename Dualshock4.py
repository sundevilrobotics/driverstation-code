import pygame

class Dualshock4:
    def __init__(self):
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def getCross(self):
        pass

    def getSquare(self):
        pass

    def getTriangle(self):
        pass

    def getCircle(self):
        pass

    def getL1(self):
        pass

    def getL2(self):
        pass

    def getL3(self):
        pass

    def getR1(self):
        pass

    def getR2(self):
        pass

    def getR3(self):
        pass

    def getSelect(self):
        pass

    def getStart(self):
        pass
    
    def getLeftStick(self):
        pass

    def getRightStick(self):
        pass