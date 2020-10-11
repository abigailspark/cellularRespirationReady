#file that deals with collisions

import math
import pygame

#takes two molecules and returns True if they collide and False otherwise
def checkCollision(molecule1, molecule2):
    #if the rectangles that contain each molecule do not overlap then there
    #is no chance that the molecules themselves could collide
    if molecule1.rect.colliderect(molecule2.rect):
        #check between polygons of each molecule
        for poly1 in molecule1.polygons:
            poly1.coordinatesFromOrigin(molecule1.x, molecule1.y)
            for poly2 in molecule2.polygons:
                poly2.coordinatesFromOrigin(molecule2.x, molecule2.y)
                if poly1.polygonCollision(poly2):
                    return True
        #check between circles of each molecule and circles and polygons
        for circle1 in molecule1.circles:
            circle1.coordinatesFromOrigin(molecule1.x, molecule1.y)
            for circle2 in molecule2.circles:
                circle2.coordinatesFromOrigin(molecule2.x, molecule2.y)
                if circle1.circleCollision(circle2):
                    return True
            for polygon in molecule2.polygons:
                polygon.coordinatesFromOrigin(molecule2.x, molecule2.y)
                if circle1.polygonCollision(polygon):
                    return True
        for circle2 in molecule2.circles:
            circle2.coordinatesFromOrigin(molecule2.x, molecule2.y)
            for polygon in molecule1.polygons:
                polygon.coordinatesFromOrigin(molecule1.x, molecule1.y)
                if circle2.polygonCollision(polygon):
                    return True
    else:
        return False

#finds the final velocity of molecules after a collision
def moleculeCollide(molecule1, molecule2):
    molecule1.xVelocity, molecule2.xVelocity = getSpeed(
        molecule1.xVelocity, molecule2.xVelocity,
        molecule1.mass, molecule2.mass)
    molecule1.yVelocity, molecule2.yVelocity = getSpeed(
        molecule1.yVelocity, molecule2.yVelocity,
        molecule1.mass, molecule2.mass)
    molecule1.setSpeed()
    molecule2.setSpeed()


#equations based on  https://en.wikipedia.org/wiki/Elastic_collision
def getSpeed(v1, v2, m1, m2):
    v1f = ((m1 - m2) * v1 / (m1 + m2)) + ((2 * m2 * v2) / (m1 + m2))
    v2f = ((2 * m1 * v1) / (m1 + m2)) + ((m2 - m1) * v2 / (m1 + m2))
    return v1f, v2f 




