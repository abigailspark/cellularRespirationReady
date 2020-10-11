#file that runs Cellular Respiration Ready

import pygame
import random
from molecule import molecule
from molecule import playerMolecule
from collisions import checkCollision
from collisions import moleculeCollide

pygame.init()

#inspiration taken from http://blog.lukasperaza.com/getting-started-with-pygame/
class CellularRespirationReady(object):
    def __init__(self, width, height):
        self.player = pygame.sprite.Group()
        self.others = pygame.sprite.Group()

        self.screenWidth = width
        self.screenHeight = height
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        
        self.fps = 100
        self.playing = True
        self.pause = True
        
        self.home = True
        self.homeScreen = pygame.image.load('images/home.png')
        
        self.messageStep = 0
        self.glycolysis = False
        self.citricAcid = False
        
        self.electronTransportChain = False
        self.electronTransition = False
     
        self.targetBox = pygame.image.load('images/targetBox.png')
        self.targetBox = pygame.transform.scale(self.targetBox, (215, 215))

    def createMolecules(self, n, group, screenWidth, screenHeight, 
                    scaleWidth, scaleHeight, image, circles, polygons, mass, name):
        for i in range(n):
            m = molecule(screenWidth, screenHeight, 
                        scaleWidth, scaleHeight, image, circles, polygons, mass, name)
            group.add(m)

    def createGlycolysisPlayerMolecules(self):
        glycolysisMolecules = []

        glycolysis0Image = pygame.image.load("images/glycolysis0.png")
        circles = []
        polygons = [(
            (325, 9), (959, 10), (1290, 568), (954, 1142), (323, 1133), (6, 578))
        ]

        glycolysis0 = playerMolecule(self.screenWidth, self.screenHeight, 
                        125, 112, glycolysis0Image, circles, polygons, 180, "glucose")
        glycolysisMolecules.append(glycolysis0)

        glycolysis1Image = pygame.image.load("images/glycolysis1.png")
        circles = [
            ((64, 61), 60)
        ]
        polygons = [
            ((287, 5), (534, 190), (439, 466), (141, 466), (48, 180))
        ]
        glycolysis1 = playerMolecule(self.screenWidth, self.screenHeight,
                         125, 112, glycolysis1Image, circles, polygons, 180, 'glucose6P')
        glycolysisMolecules.append(glycolysis1)

        glycolysis2Image = pygame.image.load("images/glycolysis2.png")
        circles = [
            ((61, 59), 60),
            ((509, 59), 60)
        ]
        polygons = [
            ((288, 1), (533, 184), (440, 462), (141, 465), (46, 179))
        ]
        glycolysis2 = playerMolecule(self.screenWidth, self.screenHeight, 
                        125, 112, glycolysis2Image, circles, polygons, 170, 'fructose6P')
        glycolysisMolecules.append(glycolysis2)

        glycolysis3Image = pygame.image.load('images/glycolysis3.png')
        circles = [
            ((175, 270), 130),
            ((440, 270), 130),
            ((680, 270), 130),
            ((680, 675), 130)
        ]
        polygons = []
        glycolysis3 = playerMolecule(self.screenWidth, self.screenHeight, 
                        130, 110, glycolysis3Image, circles, polygons, 90, 'G3P')
        glycolysisMolecules.append(glycolysis3)

        glycolysis4Image = pygame.image.load('images/glycolysis4.png')
        circles = [
            ((315, 130), 130),
            ((315, 485), 130),
            ((530, 485), 130),
            ((740, 485), 130),
            ((740, 840), 130)

        ]
        polygons = []
        glycolysis4 = playerMolecule(self.screenWidth, self.screenHeight,
                        150, 150, glycolysis4Image, circles, polygons, 90, '1,3-BG')
        glycolysisMolecules.append(glycolysis4)

        glycolysis5Image = glycolysis3Image
        circles = [
            ((175, 270), 130),
            ((440, 270), 130),
            ((680, 270), 130),
            ((680, 675), 130)
        ]
        polygons = []
        glycolysis5 = playerMolecule(self.screenWidth, self.screenHeight, 
                        130, 110, glycolysis5Image, circles, polygons, 90, '3-PG')
        glycolysisMolecules.append(glycolysis5)

        glycolysis6Image = pygame.image.load('images/glycolysis6.png')
        circles = [
            ((295, 350), 130),
            ((510, 350), 130),
            ((725, 350), 130),
            ((505, 700), 130)
        ]
        polygons = []
        glycolysis6 = playerMolecule(self.screenWidth, self.screenHeight, 
                        145, 130, glycolysis6Image, circles, polygons, 90, 'PEP')
        glycolysisMolecules.append(glycolysis6)

        glycolysis7Image = pygame.image.load('images/glycolysis7.png')
        circles = [
            ((270, 280), 130),
            ((490, 280), 130),
            ((700, 280), 130)
        ]
        polygons = []
        glycolysis7 = playerMolecule(self.screenWidth, self.screenHeight, 
                        130, 75, glycolysis7Image, circles, polygons, 90, 'pyruvate')
        glycolysisMolecules.append(glycolysis7)

        return glycolysisMolecules

    def createGlycolysisTargetMolecules(self):
        targetNames = []

        atpImage = pygame.image.load('images/atp.png')
        circles = [
            ((182, 280), 172),
            ((525, 280), 172),
            ((867, 280), 172)
        ]
        polygons = [
            ((1398, 379), (1635, 503), (1522, 709), (1275, 707), (1150, 499)),
            ((1635, 41), (1519, 181), (1635, 338), (1810, 291), (1810, 91)),
            ((2140, 95), (2140, 280), (1970, 370), (1810, 280), (1810, 95), (1970, 9))
        ]
        target0 = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           atpImage, circles, polygons, 507, 'atp')
        targetNames.append(target0.name)
        self.others.add(target0)


        target1 = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           atpImage, circles, polygons, 507, 'atp')
        targetNames.append(target1.name)
        self.others.add(target1)

        nadImage = pygame.image.load('images/nad+.png')
        circles = []
        polygons = [
            ((40, 20), (40, 470), (900, 470), (900, 20))
        ]
        target3 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, circles, polygons, 660, 'nad+')
        targetNames.append(target3.name)
        self.others.add(target3)

        adpImage = pygame.image.load('images/adp.png')
        circles = [
            ((175, 300), 172),
            ((534, 300), 172)
        ]
        polygons =[
            ((1043, 379), (793, 500), (921, 711), (1170, 711), (1286, 506)),
            ((1287, 40), (1167, 185), (1280, 340), (1458, 290), (1457, 93)),
            ((1784, 100), (1793, 277), (1618, 375), (1458, 290), (1457, 93), (1612, 8))
        ]
        target4 = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          adpImage, circles, polygons, 427, 'adp')
        targetNames.append(target4.name)
        self.others.add(target4)

        target5 = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          adpImage, circles, polygons, 427, 'adp')
        targetNames.append(target5.name)
        self.others.add(target5)

        return targetNames

    def createGlycolysisWasteMolecules(self):
        wasteMolecules = []

        waste0Image = pygame.image.load('images/adp.png')
        circles = [
            ((175, 300), 172),
            ((534, 300), 172)
        ]
        polygons =[
            ((1043, 379), (793, 500), (921, 711), (1170, 711), (1286, 506)),
            ((1287, 40), (1167, 185), (1280, 340), (1458, 290), (1457, 93)),
            ((1784, 100), (1793, 277), (1618, 375), (1458, 290), (1457, 93), (1612, 8))
        ]
        waste0 = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          waste0Image, circles, polygons, 427, 'adp')
        wasteMolecules.append(waste0)

        waste1 = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          waste0Image, circles, polygons, 427, 'adp')
        wasteMolecules.append(waste1)

        waste2Image = pygame.image.load('images/nadh.png')
        circles = []
        polygons = [
            ((40, 20), (40, 470), (900, 470), (900, 20))
        ]
        waste2 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                          waste2Image, circles, polygons, 660, 'nadh')
        wasteMolecules.append(waste2)

        waste3Image = pygame.image.load('images/atp.png')
        circles = [
            ((182, 280), 172),
            ((525, 280), 172),
            ((867, 280), 172)
        ]
        polygons = [
            ((1398, 379), (1635, 503), (1522, 709), (1275, 707), (1150, 499)),
            ((1635, 41), (1519, 181), (1635, 338), (1810, 291), (1810, 91)),
            ((2140, 95), (2140, 280), (1970, 370), (1810, 280), (1810, 95), (1970, 9))
        ]
        waste3 = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           waste3Image, circles, polygons, 507, 'atp')
        wasteMolecules.append(waste3)
    
        waste4Image = pygame.image.load('images/water.png')
        circles = [
            ((382, 261), 232),
            ((100, 92), 90),
            ((658, 92), 90)
        ]
        polygons = []
        waste4 = molecule(self.screenWidth, self.screenHeight, 51, 34, 
                          waste4Image, circles, polygons, 18, 'water')
        wasteMolecules.append(waste4)

        waste5Image = pygame.image.load('images/atp.png')
        circles = [
            ((182, 280), 172),
            ((525, 280), 172),
            ((867, 280), 172)
        ]
        polygons = [
            ((1398, 379), (1635, 503), (1522, 709), (1275, 707), (1150, 499)),
            ((1635, 41), (1519, 181), (1635, 338), (1810, 291), (1810, 91)),
            ((2140, 95), (2140, 280), (1970, 370), (1810, 280), (1810, 95), (1970, 9))
        ]
        waste5 = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           waste5Image, circles, polygons, 507, 'atp')
        wasteMolecules.append(waste5)

        return wasteMolecules

    def createGlycolysisOtherMolecules(self):
        waterImage = pygame.image.load('images/water.png')

        circles = [
            ((382, 261), 232),
            ((100, 92), 90),
            ((658, 92), 90)
        ]
        polygons = []
        self.createMolecules(5, self.others, self.screenWidth, self.screenHeight, 
                        51, 34, waterImage,circles, polygons, 18, 'water')
        
    def createGlycolysisMessages(self):
        glycolysisMessages = []

        message0 = pygame.image.load('images/glycolysisMessage0.png')
        message0 = pygame.transform.scale(message0,
                                        (int(message0.get_width() * 0.5), 
                                        int(message0.get_height() * 0.5)))
        glycolysisMessages.append(message0)

        message1 = pygame.image.load('images/glycolysisMessage1.png')
        message1 = pygame.transform.scale(message1,
                                        (int(message1.get_width() * 0.5), 
                                        int(message1.get_height() * 0.5)))
        glycolysisMessages.append(message1)

        message2 = pygame.image.load('images/glycolysisMessage2.png')
        message2 = pygame.transform.scale(message2,
                                        (int(message2.get_width() * 0.5), 
                                        int(message2.get_height() * 0.5)))
        glycolysisMessages.append(message2)

        message3 = pygame.image.load('images/glycolysisMessage3.png')
        message3 = pygame.transform.scale(message3,
                                        (int(message3.get_width() * 0.5), 
                                        int(message3.get_height() * 0.5)))
        glycolysisMessages.append(message3)

        message4 = pygame.image.load('images/glycolysisMessage4.png')
        message4 = pygame.transform.scale(message4,
                                        (int(message4.get_width() * 0.5), 
                                        int(message4.get_height() * 0.5)))
        glycolysisMessages.append(message4)

        message5 = pygame.image.load('images/glycolysisMessage5.png')
        message5 = pygame.transform.scale(message5,
                                        (int(message5.get_width() * 0.5), 
                                        int(message5.get_height() * 0.5)))
        glycolysisMessages.append(message5)

        return glycolysisMessages

    def createCitricAcidPlayerMolecules(self):
        molecules = []

        ca1Image = pygame.image.load('images/glycolysis7.png')
        circles = [
            ((270, 280), 130),
            ((490, 280), 130),
            ((700, 280), 130)
        ]
        polygons = []
        ca1 = playerMolecule(self.screenWidth, self.screenHeight, 
                        130, 75, ca1Image, circles, polygons, 90, 'pyruvate')
        molecules.append(ca1)

        ca2Image = pygame.image.load('images/ca2.png')
        circles = [
            ((280, 275,), 110),
            ((500, 275), 110)
        ]
        polygons = []
        ca2 = playerMolecule(self.screenWidth, self.screenHeight, 
                        115, 75, ca2Image, circles, polygons, 90, 'acetate')
        molecules.append(ca2)

        ca3Image = pygame.image.load('images/ca3.png')
        circles = [
            ((240, 250), 105),
            ((430, 250), 105)
        ]
        polygons = [
            ((535, 150), (830, 150), (830, 320), (535, 320))
        ]
        ca3 = playerMolecule(self.screenWidth, self.screenHeight, 
                        160, 75, ca3Image, circles, polygons, 800, 'acetylCoA')
        molecules.append(ca3)

        ca4Image = pygame.image.load('images/ca6.png')
        circles = [
            ((170, 170), 60),
            ((290, 170), 60),
            ((410, 170), 60),
            ((530, 170), 60),
            ((650, 170), 60),
            ((770, 170), 60)
        ]
        polygons = []
        ca4 = playerMolecule(self.screenWidth, self.screenHeight, 
                        240, 90, ca4Image, circles, polygons, 190, 'citrate')
        molecules.append(ca4)

        ca5Image = pygame.image.load('images/ca5.png')
        circles = [
            ((180, 190), 60),
            ((300, 190), 60),
            ((420, 190), 60),
            ((540, 190), 60),
            ((660, 190), 60)
        ]
        polygons = []
        ca5 = playerMolecule(self.screenWidth, self.screenHeight, 
                        230, 85, ca5Image, circles, polygons, 160, '5c')
        molecules.append(ca5)

        ca6Image = pygame.image.load('images/ca4.png')
        circles = [
            ((220, 200), 90),
            ((400, 200), 90),
            ((580, 200), 90),
            ((760, 200), 90)
        ]
        ca6 = playerMolecule(self.screenWidth, self.screenHeight,
                            185, 75, ca6Image, circles, polygons, 130, '4c')
        molecules.append(ca6)

        return molecules

    def createCitricAcidTargetMolecules(self):
        targetNames = []

        #the first target molecule is the transport protein, which is fixed
        image1 = self.CAbackground
        circles = []
        polygons = [
            ((160, 350), (140, 370), (160, 390))
        ]
        target1 = playerMolecule(self.screenWidth, self.screenHeight,
            self.screenWidth, self.screenHeight, image1, circles, polygons,
            1, 'transportProtein')
        target1.speed = 0
        target1.xVelocity = 0
        target1.yVelocity = 0
        self.others.add(target1)
        targetNames.append(target1.name)

        nadImage = pygame.image.load('images/nad+.png')
        nadcircles = []
        nadpolygons = [
            ((40, 20), (40, 470), (900, 470), (900, 20))
        ]
        target2 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, nadcircles, nadpolygons, 660, 'nad')
        self.others.add(target2)
        targetNames.append(target2.name)

        coAImage = pygame.image.load('images/coA.png')
        circles = []
        polygons = [
            ((25, 5), (860, 5), (860, 500), (25, 500))
        ]
        target3 = molecule(self.screenWidth, self.screenHeight, 65, 30,
                        coAImage, circles, polygons, 770, 'coA')
        self.others.add(target3)
        targetNames.append(target3.name)

        oxoloacetate = pygame.image.load('images/oxoloacetate.png')
        circles = [
            ((100, 110), 90),
            ((285, 110), 90),
            ((470, 110), 90),
            ((655, 110), 90)
        ]
        polygons = []
        target4 = molecule(self.screenWidth, self.screenHeight, 140, 40,
                    oxoloacetate, circles, polygons, 130, 'oxoloacetate')
        self.others.add(target4)
        targetNames.append(target4.name)


        target5 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, nadcircles, nadpolygons, 660, 'nad')
        self.others.add(target5)
        targetNames.append(target5.name)
    
        target6 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, nadcircles, nadpolygons, 660, 'nad')
        self.others.add(target6)
        targetNames.append(target6.name)

        #gdp is structurally similar enough to adp, that the same image will be used
        gdpImage = pygame.image.load('images/adp.png')
        circles = [
            ((175, 300), 172),
            ((534, 300), 172)
        ]
        polygons =[
            ((1043, 379), (793, 500), (921, 711), (1170, 711), (1286, 506)),
            ((1287, 40), (1167, 185), (1280, 340), (1458, 290), (1457, 93)),
            ((1784, 100), (1793, 277), (1618, 375), (1458, 290), (1457, 93), (1612, 8))
        ]
        target7 = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          gdpImage, circles, polygons, 427, 'gdp')
        targetNames.append(target7.name)
        self.others.add(target7)

        fadImage = pygame.image.load('images/fad.png')
        target8 = molecule(self.screenWidth, self.screenHeight, 90, 50, 
                       fadImage, nadcircles, nadpolygons, 660, 'fad')
        targetNames.append(target8.name)
        self.others.add(target8)

        target9 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, nadcircles, nadpolygons, 660, 'nad')
        self.others.add(target9)
        targetNames.append(target9.name)

        return targetNames

    def createCitricAcidWasteMolecules(self):
        molecules = []

        co2Image = pygame.image.load('images/co2.png')
        co2Circles = [
            ((110, 120), 100),
            ((260, 260), 100),
            ((430, 120), 100)
        ]
        co2Polygons = []
        waste1 = molecule(self.screenWidth, self.screenHeight, 90, 65,
                        co2Image, co2Circles, co2Polygons, 44, 'co2')
        molecules.append(waste1)

        nadhImage = pygame.image.load('images/nadh.png')
        nadhCircles = []
        nadhPolygons = [
            ((40, 20), (40, 470), (900, 470), (900, 20))
        ]
        waste2 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                          nadhImage, nadhCircles, nadhPolygons, 660, 'nadh')
        molecules.append(waste2)

        coAImage = pygame.image.load('images/coA.png')
        circles = []
        polygons = [
            ((25, 5), (860, 5), (860, 500), (25, 500))
        ]
        waste3 = molecule(self.screenWidth, self.screenHeight, 65, 30,
                        coAImage, circles, polygons, 770, 'coA')
        molecules.append(waste3)

        waste4 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                          nadhImage, nadhCircles, nadhPolygons, 660, 'nadh')
        molecules.append(waste4)

        waste5 = molecule(self.screenWidth, self.screenHeight, 90, 65,
                        co2Image, co2Circles, co2Polygons, 44, 'co2')
        molecules.append(waste5)

        waste6 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                          nadhImage, nadhCircles, nadhPolygons, 660, 'nadh')
        molecules.append(waste6)

        waste7 = molecule(self.screenWidth, self.screenHeight, 90, 65,
                        co2Image, co2Circles, co2Polygons, 44, 'co2')
        molecules.append(waste7)

        gtpImage = pygame.image.load('images/atp.png')
        circles = [
            ((182, 280), 172),
            ((525, 280), 172),
            ((867, 280), 172)
        ]
        polygons = [
            ((1398, 379), (1635, 503), (1522, 709), (1275, 707), (1150, 499)),
            ((1635, 41), (1519, 181), (1635, 338), (1810, 291), (1810, 91)),
            ((2140, 95), (2140, 280), (1970, 370), (1810, 280), (1810, 95), (1970, 9))
        ]
        waste8 = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           gtpImage, circles, polygons, 507, 'gtp')
        molecules.append(waste8)

        fadh2Image = pygame.image.load('images/fadh2.png')
        waste9 = molecule(self.screenWidth, self.screenHeight, 90, 50, 
                          fadh2Image, nadhCircles, nadhPolygons, 660, 'fadh2')
        molecules.append(waste9)

        waste10 = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                          nadhImage, nadhCircles, nadhPolygons, 660, 'nadh')
        molecules.append(waste10)

        return molecules

    def createCAMessages(self):
        messages = []

        message1 = pygame.image.load('images/caMessage1.png')
        message1 = pygame.transform.scale(message1,
                                        (int(message1.get_width() * 0.5), 
                                        int(message1.get_height() * 0.5)))
        messages.append(message1)

        message2 = pygame.image.load('images/caMessage2.png')
        message2 = pygame.transform.scale(message2,
                                        (int(message2.get_width() * 0.5), 
                                        int(message2.get_height() * 0.5)))
        messages.append(message2)

        message3 = pygame.image.load('images/caMessage3.png')
        message3 = pygame.transform.scale(message3,
                                        (int(message3.get_width() * 0.5), 
                                        int(message3.get_height() * 0.5)))
        messages.append(message3)

        message4 = pygame.image.load('images/caMessage4.png')
        message4 = pygame.transform.scale(message4,
                                        (int(message4.get_width() * 0.5), 
                                        int(message4.get_height() * 0.5)))
        messages.append(message4)

        message5 = pygame.image.load('images/caMessage5.png')
        message5 = pygame.transform.scale(message5,
                                        (int(message5.get_width() * 0.5), 
                                        int(message5.get_height() * 0.5)))
        messages.append(message5)

        message6 = pygame.image.load('images/caMessage6.png')
        message6 = pygame.transform.scale(message6,
                                        (int(message6.get_width() * 0.5), 
                                        int(message6.get_height() * 0.5)))
        messages.append(message6)

        message7 = pygame.image.load('images/caMessage7.png')
        message7 = pygame.transform.scale(message7,
                                        (int(message7.get_width() * 0.5), 
                                        int(message7.get_height() * 0.5)))
        messages.append(message7)

        message8 = pygame.image.load('images/caMessage8.png')
        message8 = pygame.transform.scale(message8,
                                        (int(message8.get_width() * 0.5), 
                                        int(message8.get_height() * 0.5)))
        messages.append(message8)

        message9 = pygame.image.load('images/caMessage9.png')
        message9 = pygame.transform.scale(message9,
                                        (int(message9.get_width() * 0.5), 
                                        int(message9.get_height() * 0.5)))
        messages.append(message9)

        message10 = pygame.image.load('images/caMessage10.png')
        message10 = pygame.transform.scale(message10,
                                        (int(message10.get_width() * 0.5), 
                                        int(message10.get_height() * 0.5)))
        messages.append(message10)

        return messages

    def createETCProteins(self):
        proteins = []

        adpImage = pygame.image.load('images/adp.png')
        circles = [
            ((175, 300), 172),
            ((534, 300), 172)
        ]
        polygons =[
            ((1043, 379), (793, 500), (921, 711), (1170, 711), (1286, 506)),
            ((1287, 40), (1167, 185), (1280, 340), (1458, 290), (1457, 93)),
            ((1784, 100), (1793, 277), (1618, 375), (1458, 290), (1457, 93), (1612, 8))
        ]
        adp = molecule(self.screenWidth, self.screenHeight, 145, 58, 
                          adpImage, circles, polygons, 427, 'adp')
        adp.moveMolecule(560, 350)
        proteins.append(adp)

        image = self.etcBackground

        circles = []
        polygons = [
            ((160, 230), (240, 230), (240, 360), (160, 360))
        ]
        complexI = molecule(self.screenWidth, self.screenHeight, self.screenWidth,
            self.screenHeight, image, circles, polygons, 1, 'complexI')
        proteins.append(complexI)
        self.targetMolecule.append(complexI)

        circles = []
        polygons = [
            ((290, 230), (370, 230), (370, 360), (290, 360))
        ]
        complexIII = molecule(self.screenWidth, self.screenHeight, self.screenWidth,
            self.screenHeight, image, circles, polygons, 1, 'complexIII')
        proteins.append(complexIII)
        self.targetMolecule.append(complexIII)

        circles = []
        polygons = [
            ((420, 230), (500, 230), (500, 360), (420, 360))
        ]
        complexIV = molecule(self.screenWidth, self.screenHeight, self.screenWidth,
            self.screenHeight, image, circles, polygons, 1, 'complexIV')
        proteins.append(complexIV)
        self.targetMolecule.append(complexIV)

        circles = [((760, 360), 60)]
        polygons = [
            ((720, 200), (720, 310), (800, 301), (800, 200))
        ]
        atpSynthase = molecule(self.screenWidth, self.screenHeight, self.screenWidth,
            self.screenHeight, image, circles, polygons, 1, 'atpSynthase')
        proteins.append(atpSynthase)
        self.targetMolecule.append(atpSynthase)

        polygons = [
                ((0, 245), (0, 350), (1000, 350), (1000, 245))
            ]
        membrane = molecule(self.screenWidth, self.screenHeight,
            self.screenWidth, self.screenHeight, self.etcBackground,
            [], polygons, 1, 'membrane')
        proteins.append(membrane)

        return proteins
        
    def createETCWaste(self):
        waste = []

        nadImage = pygame.image.load('images/nad+.png')
        nadcircles = []
        nadpolygons = [
            ((40, 20), (40, 470), (900, 470), (900, 20))
        ]
        nad = molecule(self.screenWidth, self.screenHeight, 100, 54, 
                       nadImage, nadcircles, nadpolygons, 1, 'nad')
        waste.append(nad)

        hImage = pygame.image.load('images/h+.png')
        hCircles = [
            ((375, 375), 375)
        ]
        polygons = []
        h1 = molecule(self.screenWidth, self.screenHeight, 40, 40, 
                       hImage, hCircles , polygons, 1, 'h+')
        waste.append(h1)

        h2 = molecule(self.screenWidth, self.screenHeight, 40, 40, 
                       hImage, hCircles , polygons, 1, 'h+')
        waste.append(h2)

        h3 = molecule(self.screenWidth, self.screenHeight, 40, 40, 
                       hImage, hCircles , polygons, 1, 'h+')
        waste.append(h3)

        h4 = molecule(self.screenWidth, self.screenHeight, 40, 40, 
                       hImage, hCircles , polygons, 1, 'h+')
        waste.append(h4)

        waterImage = pygame.image.load('images/water.png')
        circles = [
            ((382, 261), 232),
            ((100, 92), 90),
            ((658, 92), 90)
        ]
        polygons = []
        water = molecule(self.screenWidth, self.screenHeight, 51, 34, 
                          waterImage, circles, polygons, 18, 'water')
        waste.append(water)

        h5 = molecule(self.screenWidth, self.screenHeight, 40, 40, 
                       hImage, hCircles , polygons, 1, 'h+')
        waste.append(h5)

        

        atpImage = pygame.image.load('images/atp.png')
        circles = [
            ((182, 280), 172),
            ((525, 280), 172),
            ((867, 280), 172)
        ]
        polygons = [
            ((1398, 379), (1635, 503), (1522, 709), (1275, 707), (1150, 499)),
            ((1635, 41), (1519, 181), (1635, 338), (1810, 291), (1810, 91)),
            ((2140, 95), (2140, 280), (1970, 370), (1810, 280), (1810, 95), (1970, 9))
        ]
        atp = molecule(self.screenWidth, self.screenHeight, 175, 58, 
                           atpImage, circles, polygons, 507, 'atp')
        waste.append(atp)

        return waste

    def createETCOtherMolecules(self):
        hImage = pygame.image.load('images/h+.png')

        circles = [
            ((375, 375), 375)
        ]
        polygons = []
        self.createMolecules(4, self.others, self.screenWidth, self.screenHeight, 
                        40, 40, hImage ,circles, polygons, 1, 'h+')

        for molecule in self.others:
            while molecule.y < 450:
                molecule.y += 20
            molecule.getRect()

    def createETCPlayerMolecules(self):
        player = []

        nadhImage = pygame.image.load('images/nadhPlayer.png')
        nadhCircles = []
        nadhPolygons = [
            ((160, 160), (800, 160), (160, 500), (800, 500))
        ]
        nadh = playerMolecule(self.screenWidth, self.screenHeight, 120, 65, 
                        nadhImage, nadhCircles, nadhPolygons, 1, 'nadh')
        nadh.moveMolecule(self.screenWidth//2, self.screenHeight * 0.8)
        player.append(nadh)
        self.player.add(nadh)

        hImage = pygame.image.load('images/h+Player.png')
        hCircles = [
            ((400, 380), 240)
        ]
        polygons = []
        h1 = playerMolecule(self.screenWidth, self.screenHeight, 
                        60, 60, hImage ,hCircles, polygons, 1, 'h+')
        player.append(h1)
        
        h2 = playerMolecule(self.screenWidth, self.screenHeight, 
                        60, 60, hImage ,hCircles, polygons, 1, 'h+')
        player.append(h2)
        
        h3 = playerMolecule(self.screenWidth, self.screenHeight, 
                        60, 60, hImage ,hCircles, polygons, 1, 'h+')
        player.append(h3)
    

        return player

    def createETCMessages(self):
        messages = []

        message1 = pygame.image.load('images/etcMessage1.png')
        message1 = pygame.transform.scale(message1,
                                        (int(message1.get_width() * 0.4), 
                                        int(message1.get_height() * 0.4)))
        messages.append(message1)

        message2 = pygame.image.load('images/etcMessage2.png')
        message2 = pygame.transform.scale(message2,
                                        (int(message2.get_width() * 0.4), 
                                        int(message2.get_height() * 0.4)))
        messages.append(message2)

        message3 = pygame.image.load('images/etcMessage3.png')
        message3 = pygame.transform.scale(message3,
                                        (int(message3.get_width() * 0.4), 
                                        int(message3.get_height() * 0.4)))
        messages.append(message3)

        message4 = pygame.image.load('images/etcMessage4.png')
        message4 = pygame.transform.scale(message4,
                                        (int(message4.get_width() * 0.4), 
                                        int(message4.get_height() * 0.4)))
        messages.append(message4)

        message5 = pygame.image.load('images/etcMessage5.png')
        message5 = pygame.transform.scale(message5,
                                        (int(message5.get_width() * 0.4), 
                                        int(message5.get_height() * 0.4)))
        messages.append(message5)

        message6 = pygame.image.load('images/etcMessage6.png')
        message6 = pygame.transform.scale(message6,
                                        (int(message6.get_width() * 0.4), 
                                        int(message6.get_height() * 0.4)))
        messages.append(message6)

        message7 = pygame.image.load('images/etcMessage7.png')
        message7 = pygame.transform.scale(message7,
                                        (int(message7.get_width() * 0.4), 
                                        int(message7.get_height() * 0.4)))
        messages.append(message7)

        message8 = pygame.image.load('images/etcMessage8.png')
        message8 = pygame.transform.scale(message8,
                                        (int(message8.get_width() * 0.4), 
                                        int(message8.get_height() * 0.4)))
        messages.append(message8)

        message9 = pygame.image.load('images/etcMessage9.png')
        message9 = pygame.transform.scale(message9,
                                        (int(message9.get_width() * 0.4), 
                                        int(message9.get_height() * 0.4)))
        messages.append(message9)

        return messages

    def CACollisionWithBackground(self, background, group):
        for molecule in group:
            if molecule.x < 350:
                if checkCollision(background, molecule):
                    molecule.xVelocity = - molecule.xVelocity
                    while checkCollision(background, molecule):
                        molecule.update()
   
    def moveIntoMitochondria(self, group):
        for molecule in group:
            if molecule.name != 'transportProtein':
                while molecule.x < 350:
                    molecule.x += 20
                molecule.getRect()

    def etcCollideWithBackground(self, group):
        for protein in self.proteins:
            for molecule in group:
                if checkCollision(protein, molecule):
                    molecule.yVelocity = -molecule.yVelocity
                    while checkCollision(protein, molecule):
                        molecule.update()

    def collisions(self, group1, group2):
        collided = {}
        for molecule1 in group1:
            collided[molecule1] = []
            for molecule2 in group2:
                if molecule1 != molecule2:
                    if checkCollision(molecule1, molecule2):
                        collided[molecule1].append(molecule2)
                        moleculeCollide(molecule1, molecule2)
                        while checkCollision(molecule1, molecule2):
                            molecule1.update()
                            molecule2.update()
        return collided

    def updateTargetBox(self, target):
        for molecule in self.others:
            if molecule.name == target and molecule.name != 'transportProtein':
                targetImage = molecule.image
                targetWidth = targetImage.get_width()
                targetHeight = targetImage.get_height()
                boxWidth = self.targetBox.get_width()
                boxHeight = self.targetBox.get_height()
                x = (boxWidth // 2) - (targetWidth // 2)
                y = (boxHeight // 2) - (targetHeight // 2) + 15
                targetBox = self.targetBox.copy()
                targetBox.blit(targetImage, (x, y))
                self.screen.blit(targetBox, (20, self.screenHeight - boxHeight - 20))

    def drawElectron(self):
        if len(self.electronPositions) > 0:
            position = self.electronPositions[0]
            self.screen.blit(self.electronImage, position)

    def updateElectron(self):
        if len(self.electronPositions) > 0:
            self.pause = True
            self.messageStep += 1
            self.electronPositions.pop(0)
        else:
            self.electronTransition = False
       
    #if matrix = True, returns the x, y coordinate of a proton in the matrix
    #and replaces that proton with the player proton
    def findNextProton(self, matrix):
        if matrix == True:
            for molecule in self.others:
                if molecule.name == 'h+':
                    if molecule.y > 350:
                        x = molecule.x
                        y = molecule.y
                        self.others.remove(molecule)
                        return (x, y)
        elif matrix == False:
            for molecule in self.others:
                if molecule.name == 'h+':
                    if molecule.y < 245:
                        x = molecule.x
                        y = molecule.y
                        self.others.remove(molecule)
                        return (x, y)
        
    def updatePlayer(self):
        if len(self.playerMolecule) > 1:
            x = self.playerMolecule[0].x
            y = self.playerMolecule[0].y

            self.playerMolecule.pop(0)
            self.player.empty()
            
            self.playerMolecule[0].moveMolecule(x,y)
            self.player.add(self.playerMolecule[0])

    def updateWaste(self, x, y):
        self.others.add(self.wasteMolecule[0])
        self.wasteMolecule[0].moveMolecule(x, y)
        self.wasteMolecule.pop(0)

    def updateGlycolysis(self):
        self.player.update()
        self.others.update()
        collided = self.collisions(self.player, self.others)
        self.collisions(self.others, self.others)

        if len(self.targetMolecule) > 0:
            self.updateTargetBox(self.targetMolecule[0])

        playerX = self.playerMolecule[0].x
        playerY = self.playerMolecule[0].y

        #at this specific steps, player molecule does not need to collide with 
        #another molecule to proceed to next step (converting to G3P)
        if (self.playerMolecule[0].name == 'fructose6P'):
            self.updatePlayer()

        elif (self.playerMolecule[0].name == '3-PG'):
            x = self.playerMolecule[0].x
            y = self.playerMolecule[0].y
            self.updateWaste(x-50, y-50)
            self.updatePlayer()

        elif len(self.playerMolecule) > 0:
            for molecule in collided[self.playerMolecule[0]]:
                if len(self.targetMolecule) > 0:
                    if (molecule.name == self.targetMolecule[0]):
                        self.pause = True
                        self.targetMolecule.pop(0)
                        x = molecule.x
                        y = molecule.y
                        self.updateWaste(x, y)
                        molecule.remove(self.others)
                        self.updatePlayer()
                        self.messageStep += 1                  

    def updateCitricAcid(self):
        self.player.update()
        self.others.update()
        self.CACollisionWithBackground(self.mitochondria, self.others)
        self.CACollisionWithBackground(self.mitochondria, self.player)
        collided = self.collisions(self.player, self.others)
        self.collisions(self.others, self.others)

        if len(self.targetMolecule) > 0:
            self.updateTargetBox(self.targetMolecule[0])

        for molecule in collided[self.playerMolecule[0]]:
            if len(self.targetMolecule) > 0:
                if (molecule.name == self.targetMolecule[0]):
                    self.pause = True
                    self.targetMolecule.pop(0)
                    x = molecule.x
                    y = molecule.y

                    #player moved across membrane
                    if molecule.name == 'transportProtein':
                        self.updatePlayer()
                        self.playerMolecule[0].x += 200
                        self.playerMolecule[0].getRect()
                        self.updateWaste(self.playerMolecule[0].x + 50, self.playerMolecule[0].y + 50)
                        molecule.remove(self.others)
                    
                    #no waste produced in this step
                    elif molecule.name == 'coA':
                        self.updatePlayer()
                        molecule.remove(self.others)

                    #player molecule does not change at this step
                    elif ((self.playerMolecule[0].name == '4c') or 
                        ((molecule.name == 'nad') and (self.playerMolecule[0].name == 'acetate'))):
                        self.updateWaste(x, y)
                        molecule.remove(self.others)
                    
                    #two waste products produced at this step
                    elif((self.playerMolecule[0].name == 'citrate' or 
                          self.playerMolecule[0].name == '5c') and
                          molecule.name == 'nad'):
                        self.updateWaste(x, y)
                        self.updateWaste(x + 50, y + 50)
                        molecule.remove(self.others)
                        self.updatePlayer()

                    else:
                        self.updateWaste(x, y)
                        molecule.remove(self.others)
                        self.updatePlayer()
                    self.messageStep += 1

    def updateETC(self):
        if self.electronTransition == False:
            if self.playerMolecule[0].name == 'nadh':
                if checkCollision(self.playerMolecule[0], self.targetMolecule[0]):
                    self.pause = True
                    self.electronTransition = True
                    self.messageStep += 1
                    x = self.playerMolecule[0].x
                    y = self.playerMolecule[0].y
                    self.updateWaste( x, y + 50)
                    self.updateWaste(x- 45, y + 70)
                    self.updatePlayer()
                    (x, y) = self.findNextProton(True)
                    self.playerMolecule[0].moveMolecule(x, y)
                    return None
                   
        else:
            if len(self.electronPositions) % 2 == 1 or len(self.electronPositions) == 0:
                if checkCollision(self.playerMolecule[0], self.targetMolecule[0]):
                    x = self.playerMolecule[0].x
                    y = self.playerMolecule[0].y
                    if ((self.targetMolecule[0].name == 'complexI')
                         or self.targetMolecule[0].name == 'complexIII'):
                        self.updateWaste(x, y - 180)
                        self.updatePlayer()
                        (x, y) = self.findNextProton(True)
                        self.playerMolecule[0].moveMolecule(x, y)
                    elif (self.targetMolecule[0].name =='complexIV'):
                        self.updateWaste(x, y - 180)
                        self.updateWaste(500, 360)
                        self.updatePlayer()
                        (x, y) = self.findNextProton(False)
                        self.playerMolecule[0].moveMolecule(x, y)
                    else:
                        self.pause = True
                        self.messageStep += 1
                        self.updateWaste(x, y + 240)
                        self.updateWaste(550, 350)
                        self.player.empty()
                    self.updateElectron()
                    self.targetMolecule.pop(0)
                    return None
                    
        self.collisions(self.player, self.others)
        self.collisions(self.others, self.others)
        self.etcCollideWithBackground(self.others)
        self.etcCollideWithBackground(self.player)
        self.player.update()
        self.others.update()

    def keyPressed(self, key):
        if key == pygame.K_SPACE:
            self.pause = not self.pause
        elif key == pygame.K_h:
            self.__init__(self.screenWidth, self.screenHeight)
        elif key == pygame.K_e:
            if self.electronTransition == True:
                if (len(self.electronPositions) % 2 == 0):
                    self.updateElectron()
        else:
            self.playerMolecule[0].changeDir(key)
    
    def mousePressed(self, x, y):
        #mouse pressed inside glycolysis box
        if ((x > 29) and (x < 245) and (y > 349) and (y < 495)):
            self.glycolysis = True
            self.home = False
            self.playerMolecule = self.createGlycolysisPlayerMolecules()
            self.targetMolecule = self.createGlycolysisTargetMolecules()
            self.wasteMolecule = self.createGlycolysisWasteMolecules()
            self.messages = self.createGlycolysisMessages()
            self.createGlycolysisOtherMolecules()
            self.player.add(self.playerMolecule[0])
            self.collisions(self.player, self.others)
        
        #mouse pressed inside citric acid box
        elif ((x > 378) and (x < 595) and (y > 356) and (y < 497)):
            self.citricAcid = True
            self.home = False

            #treating the background as a molecule so that we can detect collisions with the edge of the mitochondria
            self.CAbackground = pygame.image.load('images/citricAcidBG.png')
            polygons = [
                ((290, 0), (350, 0), (250, 170), (195, 170)),
                ((250, 170), (195, 170), (165, 350), (210, 350)),
                ((160, 390), (210, 395), (180, 550), (225, 550)),
                ((180, 550), (225, 550), (280, 750), (330, 750)),
                ((210, 350), (240, 370), (210, 390))
            ]
            self.mitochondria = molecule(self.screenWidth, self.screenHeight, 
                self.screenWidth, self.screenHeight, self.CAbackground, [],
                polygons, 1, 'mitochondria')
            self.mitochondria.speed = 0
            self.mitochondria.XVelocity = 0
            self.mitochondria.YVelocity = 0

            self.messages = self.createCAMessages()
            self.playerMolecule = self.createCitricAcidPlayerMolecules()
            self.targetMolecule = self.createCitricAcidTargetMolecules()
            self.wasteMolecule = self.createCitricAcidWasteMolecules()
            self.player.add(self.playerMolecule[0])
            self.playerMolecule[0].moveMolecule(10, self.screenHeight//2 + 100)
            
            self.moveIntoMitochondria(self.others)    

        #mouse pressed inside electron transport chain
        elif ((x > 698) and (x < 913) and (y > 356) and (y < 497)):
            self.electronTransportChain = True
            self.electronTransition = False
            self.home = False
            self.etcBackground = pygame.image.load('images/etcBackground.png')
            self.playerMolecule = self.createETCPlayerMolecules()
            self.targetMolecule = []
            self.proteins = self.createETCProteins()
            self.electronImage = pygame.image.load('images/e-.png')
            self.electronImage = pygame.transform.scale(self.electronImage, (30, 30))
            self.electronPositions = [(160, 250), (245, 270), (290, 270),
                                      (370, 300), (420, 300), (500, 320)]
            self.wasteMolecule = self.createETCWaste()
            self.createETCOtherMolecules()
            self.messages = self.createETCMessages()
        
    def run(self):
        clock = pygame.time.Clock()
        time = clock.tick(100)

        while self.playing:
            self.screen.fill((255,255,255))
            if self.citricAcid == True:
                self.screen.blit(self.CAbackground, (0, 0))
            elif self.electronTransportChain == True:
                self.screen.blit(self.etcBackground, (0, 0))
                if len(self.targetMolecule) > 0:
                    self.screen.blit(self.proteins[0].image, (560, 350))
            
            time = clock.tick(self.fps)
        
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.home == True:
                        self.mousePressed(*(event.pos))
                        
                elif event.type == pygame.QUIT:
                    self.playing = False

                if self.home == False:
                    if event.type == pygame.KEYDOWN:
                        self.keyPressed(event.key)
  

            if self.home == True:
                self.screen.blit(self.homeScreen, (0,0))
            
            else:   
                self.others.draw(self.screen)
                self.player.draw(self.screen)
                if self.electronTransition == True:
                    self.drawElectron()

                if self.pause == False:
                    if self.glycolysis == True:
                        self.updateGlycolysis()

                    if self.citricAcid == True:
                        self.updateCitricAcid()
                    
                    if self.electronTransportChain == True:
                        self.updateETC()

                else:
                    self.screen.blit(self.messages[self.messageStep], 
                                (20, 20))
                    if self.electronTransportChain == False:
                        if len(self.targetMolecule) > 0:
                            self.updateTargetBox(self.targetMolecule[0])

            pygame.display.flip()

        pygame.quit()
    
game = CellularRespirationReady(1000, 750)
game.run()