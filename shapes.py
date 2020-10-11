#file that contains shape classes Polygon and Circle

import math

class Polygon(object):
    #coordinates given with respect to surface it is drawn on
    def __init__(self, coordinates, scaleWidth, scaleHeight, 
                oldWidth, oldHeight, x, y):
        self.coordinates = coordinates
        self.scaleX = scaleWidth/oldWidth
        self.scaleY = scaleHeight/oldHeight
        self.edges = self.getEdges()  
        self.axes = self.getAxis() 
        self.coordinatesOrigin = None
        self.scaleCoordinates()
        self.coordinatesFromOrigin(x,y)
               

    #coordinates given with respect to original image
    #scaleCoordinates scales the coordinates to match with the new scaled image
    def scaleCoordinates(self):
        newCoordinates = []
        for coordinate in self.coordinates:
            oldX, oldY = coordinate
            newX = int(oldX * self.scaleX)
            newY = int(oldY * self.scaleY)
            newCoordinates.append((newX, newY))
        self.coordinates = newCoordinates

    #returns a list of the edges represented as vectors
    def getEdges(self):
        edges = []
        for point in range(len(self.coordinates)):
            if point == (len(self.coordinates) - 1): #if the point is the last one in the list
                dx = self.coordinates[point][0] - self.coordinates[0][0]
                dy = self.coordinates[point][1] - self.coordinates[0][1]
            else:
                dx = self.coordinates[point][0] - self.coordinates[point + 1][0]
                dy = self.coordinates[point][1] - self.coordinates[point + 1][1]
            edges.append((dx, dy))
        return edges

    @staticmethod
    #given a vector, returns a unit vector that is perpendicular to the given vector
    def findNormalUnitVector(vector):
        dx, dy = vector
        magnitude = ((dx ** 2) + (dy ** 2)) ** (0.5)
        normalUnitVector = (-dy/(magnitude), dx/magnitude)
        return normalUnitVector

    #returns a list of all the unit vectors perpendicular to every edge in the polygon
    def getAxis(self):
        axis = []
        for vector in self.edges:
            axis.append(Polygon.findNormalUnitVector(vector))
        return axis

    #sets coordinates of the polygon from the origin of the screen
    def coordinatesFromOrigin(self, x, y):
        newCoordinates = []
        for coordinate in self.coordinates:
            newX = coordinate[0] + x
            newY = coordinate[1] + y
            newCoordinates.append((newX, newY))
        self.coordinatesOrigin = newCoordinates

    #returns the projections of every point in a polygon on given axis
    def getProjections(self, axis):
        projections = []
        for point in self.coordinatesOrigin:
            projections.append(Polygon.dotProduct(point, axis))
        return projections

    @staticmethod
    def dotProduct(vector1, vector2):
        return ((vector1[0] * vector2[0]) + (vector1[1] * vector2[1]))

    def polygonCollision(self, other):
        totalAxes = self.axes + other.axes
        for axis in totalAxes:
            projections1 = self.getProjections(axis)
            projections2 = other.getProjections(axis)
            min1 = min(projections1)
            max1 = max(projections1)
            min2 = min(projections2)
            max2 = max(projections2)
            if ((min1 < min2) and (max1 <= min2)) or ((min2 < min1) and (max2 <= min1)):
                return False
        return True
        
class Circles(object):
    def __init__(self, circle, scaleWidth, scaleHeight, 
                 oldWidth, oldHeight, x, y):
        self.x, self.y = circle[0]
        self.r = circle[1]
        self.x = self.x * (scaleWidth/ oldWidth)
        self.y = self.y * (scaleHeight/ oldHeight)
        self.r = circle[1] * (scaleWidth/oldWidth)
        self.coordinatesOrigin = None
        self.coordinatesFromOrigin(x,y)
    
    def coordinatesFromOrigin(self, x, y):
        newX = self.x + x
        newY = self.y + y
        self.coordinatesOrigin = (newX, newY)

    @staticmethod
    def distance(x1, y1, x2, y2):
        distance = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (0.5)
        return distance

    #checking if the circle is colliding with a polygon
    def polygonCollision(self, polygon):
        for axis in polygon.axes:
            if (axis[0] == 0):
                angle = math.pi / 2
            else:
                angle = math.atan(axis[1] / axis[0])
            dx = self.r * math.cos(angle)
            dy = self.r * math.sin(angle)
            x, y = self.coordinatesOrigin
            point1 = (x - dx, y - dy)
            point2 = (x + dx, y + dy)
            projectionsCircle = [Polygon.dotProduct(point1, axis),
                                 Polygon.dotProduct(point2, axis)]
            projectionsPolygon = polygon.getProjections(axis)
            minCircle = min(projectionsCircle)
            maxCircle = max(projectionsCircle)
            minPolygon = min(projectionsPolygon)
            maxPolygon = max(projectionsPolygon)
            if (((minCircle < minPolygon) and (maxCircle <= minPolygon)) 
                or ((minPolygon < minCircle) and (maxPolygon <= minCircle))):
                return False
        return True



    def circleCollision(self, other):
        x, y = self.coordinatesOrigin
        otherX, otherY = other.coordinatesOrigin
        distance = Circles.distance(x, y, otherX, otherY)
        if (distance <= (self.r + other.r)):
            return True
        return False
        



    









