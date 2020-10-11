#file that contains molecule class and subclass playerMolecule


import pygame
import random
import math
from shapes import Polygon
from shapes import Circles

#taken from course website https://www.cs.cmu.edu/~112/notes/notes-variables-and-functions.html
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


#inspiration taken from http://blog.lukasperaza.com/getting-started-with-pygame/
class molecule(pygame.sprite.Sprite):
    def __init__(self, screenWidth, screenHeight, 
                scaleWidth, scaleHeight, image, circles, polygons, mass, name):
        super().__init__()
        self.name = name
        self.image = image
        oldWidth, oldHeight = self.image.get_size()
        self.image = pygame.transform.scale(self.image, 
                                           (scaleWidth, scaleHeight))
        self.width, self.height = scaleWidth, scaleHeight
        self.mass = mass
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.x = random.randint(0, self.screenWidth - self.width)
        self.y = random.randint(0, self.screenHeight - self.height)
        
        #self.speed represents the magnitude of the molecule's velocity
        #speed**2 = xVelocity**2 + yVelocity**2
        self.speed = random.randint(5,10)
        self.xVelocity = random.randint(0,5) * random.choice([-1,1])
        #random.choice([-1,1]) gives random direction
        self.yVelocity = random.choice([-1,1])
        self.yVelocity = self.getVelocityComponent(self.xVelocity, self.yVelocity, self.speed)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.circles = []
        for circle in circles:
            self.circles.append(Circles(circle, self.width, self.height,
                                        oldWidth, oldHeight, self.x, self.y))
        
        self.polygons = []
        for polygon in polygons:
            self.polygons.append(Polygon(polygon, self.width, self.height,
                                         oldWidth, oldHeight, self.x, self.y))


    #comp1 is the velocity component that you are changing
    #comp2 is the resulting component, keeping speed constant
    #speed**2 = comp1**2 + comp2**2          
    def getVelocityComponent(self, comp1, comp2, speed):
        if comp2 == 0:
            comp2Dir = 1
        else:
            comp2Dir = abs(comp2)/comp2
        comp2Magnitude = ((speed**2) - (comp1**2))**(0.5)
        return comp2Dir * comp2Magnitude
    
    #when you have adjusted the velocity components and need to find
    #the resulting speed 
    def setSpeed(self):
        self.speed = ((self.xVelocity ** 2) + (self.yVelocity ** 2)) ** (1/2)

    def update(self):
        self.x += self.xVelocity
        self.y += self.yVelocity
        if self.x < 0:
            self.x = 0
            self.xVelocity = -self.xVelocity
        elif self.x > (self.screenWidth - self.width):
            self.x = self.screenWidth - self.width
            self.xVelocity = -self.xVelocity
        if self.y < 0:
            self.y = 0
            self.yVelocity = -self.yVelocity
        elif self.y > (self.screenHeight- self.height):
            self.y = (self.screenHeight - self.height)
            self.yVelocity = -self.yVelocity
        self.getRect()

    def moveMolecule(self, x, y):
        self.x = x
        self.y = y
        self.getRect()

    def getRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class playerMolecule(molecule):
    def __init__(self, screenWidth, screenHeight, 
                scaleWidth, scaleHeight, image, circles, polygons, mass, name):
        super().__init__(screenWidth, screenHeight, scaleWidth, scaleHeight, 
                        image, circles, polygons, mass, name)
        self.speed = 15
        self.x = self.screenWidth //2 - (self.width//2)
        self.y = self.screenHeight - 2 *(self.height)
        self.xVelocity = 0
        self.yVelocity = -self.speed #start with molecule moving up
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def changeDir(self, key):
        self.speed = 15
        self.xVelocity = roundHalfUp(self.xVelocity)
        self.yVelocity = roundHalfUp(self.yVelocity)
        if key == pygame.K_UP:
            #moving up is equivalent to decreasing self.y
            self.xVelocity = 0
            self.yVelocity = -self.speed
        elif key == pygame.K_DOWN: 
            #moving down is equivalent to increasing self.y
            self.xVelocity = 0
            self.yVelocity = self.speed
        elif key == pygame.K_LEFT:
            #moving left is equivalent to decreasing self.x
            self.xVelocity = -self.speed
            self.yVelocity = 0
        elif key == pygame.K_RIGHT:
            #moving right is equivalent to increasing self.x
            self.xVelocity = self.speed
            self.yVelocity = 0


    
