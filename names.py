import pygame
demoPic = 0
adampic = 0
try:
    demoPic = pygame.transform.scale(pygame.image.load('photos/200x200.png'), (500, 475))
    adampic = pygame.transform.scale(pygame.image.load('photos/trumpshot.jpg'), (500, 475))
except: pass
def makeNames():
    accounts = [  # name, grade, date, school, photo
        ["Adam Wixom", "9th grade", "11/8", "EHS", adampic],
        ["Emree Smith", "8th grade", "12/5", "NWH", demoPic]
    ]
    return accounts

def drawDemoPic():
    return(demoPic, (170, 100))
