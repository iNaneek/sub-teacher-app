import pygame
demoPic = 0
adampic = 0
try:
    bigPic1 = pygame.transform.scale(pygame.image.load('photos/trumpshot.jpg'), (500, 475))
    bigPic2 = pygame.transform.scale(pygame.image.load('photos/CA - 2.jpg'), (500, 475))
    bigPic3 = pygame.transform.scale(pygame.image.load('photos/CA - 3.jpg'), (500, 475))
    bigPic4 = pygame.transform.scale(pygame.image.load('photos/CA - 4.jpg'), (500, 475))
    bigPic5 = pygame.transform.scale(pygame.image.load('photos/CA - 5.jpg'), (500, 475))




except: pass




def makeNames():
    accounts = [  # name, grade, date, school, photo
        ["Adam Wixom", "9th grade", "11/8", "EHS", bigPic1],
        ["Samantha Pine", "8th grade", "12/5", "NWHS", bigPic2],
        ["Emree Smith", "12th grade", "11/09", "BHS", bigPic3],
        ["Sasha Bruins", "10th grade", "11/25", "MVHS", bigPic5],
        ["Candace Fields", "9th grade", "11/28", "LPHS", bigPic4]
    ]
    return accounts

def drawDemoPic():
    return(demoPic, (170, 100))

def listOfChats():
    chats = [ # name, last chat, account photo
        [],
        [],
        []
    ]
    return chats