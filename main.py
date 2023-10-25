import pygame
import names

pygame.init()

width, height = 540, 940
# window size - 1080p but halved to make it fit. iphone 15 is only 1179 so 1080 is about right for most phones
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Teacher app thing")  # window title - to be changed

testingFont = pygame.font.Font(None, 50)  # defines font style
nameFont = pygame.font.Font(None, 40)
cardFont = pygame.font.Font(None, 25)





def demoRectangles():
    # This makes the rectangles on screen

    pygame.draw.rect(win, (0, 0, 0), ((15, 10), (75, 50)))
    # rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)))

    pygame.draw.rect(win, (0, 0, 0), ((15, 70), (75, 50)), border_radius=10)
    # rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)), rounded corners = x)

    pygame.draw.rect(win, (0, 0, 0), ((15, 130), (75, 50)), width=5)
    # rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)), side width = x)


def initOptionIcons():
    # following are stationary shapes that will always be present on the bottom of the screen
    pygame.draw.rect(win, (230, 230, 230), ((0, 840), (540, 2)))  # seperating line on the bottom

    # following icons are 100 apart

    # icon #1 - browse
    # pygame.draw.circle(win, (0, 0, 0), (70, 900), 35, width=4)
    # pygame.draw.circle(win, (0, 0, 0), (170, 900), 35, width=4)
    # pygame.draw.circle(win, (0, 0, 0), (270, 900), 35, width=4)
    # pygame.draw.circle(win, (0, 0, 0), (270, 900), 35, width=4)
    # pygame.draw.circle(win, (0, 0, 0), (270, 900), 35, width=4)

    pygame.draw.polygon(win, (0, 0, 0), (
        (70 - 25, 900 + 20), (70 - 25, 900 - 10), (70, 900 - 30), (70 + 25, 900 - 10), (70 + 25, 900 + 20),
        (70 + 5, 900 + 20), (70 + 5, 900 + 10), (70 - 6, 900 + 10), (70 - 6, 900 + 20)))
    pygame.draw.aalines(win, (0, 0, 0), True, (
        (70 - 25, 900 + 20), (70 - 25, 900 - 10), (70, 900 - 30), (70 + 25, 900 - 10), (70 + 25, 900 + 20),
        (70 + 5, 900 + 20), (70 + 5, 900 + 10), (70 - 6, 900 + 10), (70 - 6, 900 + 20)), blend=5)
    # aalines smoothens surfaces

    pygame.draw.circle(win, (250, 250, 250), (70, 910), 5)

    # icon #2 - chat

    pygame.draw.rect(win, (0, 0, 0), ((170 - 5, 900 - 10), (40, 26)), border_radius=12)
    pygame.draw.polygon(win, (0, 0, 0), ((170 + 12, 900 + 16), (170 + 22, 900 + 16), (170 + 25, 900 + 23)))
    pygame.draw.aalines(win, (0, 0, 0), True, ((170 + 12, 900 + 16), (170 + 22, 900 + 16), (170 + 25, 900 + 23)),
                        blend=5)

    pygame.draw.rect(win, (250, 250, 250), ((170 - 32, 900 - 22), (44, 30)), border_radius=14)
    pygame.draw.rect(win, (0, 0, 0), ((170 - 30, 900 - 20), (40, 26)), border_radius=12)
    pygame.draw.circle(win, (250, 250, 250), (170 - 20, 900 - 7), 4)
    pygame.draw.circle(win, (250, 250, 250), (170 - 10, 900 - 7), 4)
    pygame.draw.circle(win, (250, 250, 250), (170, 900 - 7), 4)
    pygame.draw.polygon(win, (0, 0, 0), ((170 - 17, 900 + 6), (170 - 7, 900 + 6), (170 - 20, 900 + 13)))
    pygame.draw.aalines(win, (0, 0, 0), True, ((170 - 17, 900 + 6), (170 - 7, 900 + 6), (170 - 20, 900 + 13)), blend=5)

    # icon #3 - new request - plus sign

    pygame.draw.circle(win, (0, 0, 0), (270, 900), 35, width=4)
    pygame.draw.rect(win, (0, 0, 0), ((270 - 2, 900 - 25), (4, 50)),
                     border_radius=2)  # -2 and -25 are used to position lines to centered in the circle
    pygame.draw.rect(win, (0, 0, 0), ((270 - 25, 900 - 2), (50, 4)), border_radius=2)

    # icon #4 -
    # pygame.draw.circle(win, (0, 0, 0), (370, 900), 35, width=4)
    pygame.draw.rect(win, (0, 0, 0), ((370 - 5, 900 - 5), (25, 35)), border_radius=2)

    pygame.draw.rect(win, (250, 250, 250), ((370 - 24, 900 - 25), (32, 46)), border_radius=2, width=2)
    pygame.draw.rect(win, (0, 0, 0), ((370 - 20, 900 - 21), (26, 40)), border_radius=2)

    # icon #5 - account settings
    pygame.draw.circle(win, (0, 0, 0), (470, 900), 22)
    pygame.draw.circle(win, (250, 250, 250), (470, 900 + 20), 15)
    pygame.draw.circle(win, (250, 250, 250), (470, 900 - 6), 7)
    pygame.draw.circle(win, (0, 0, 0), (470, 900), 22, width=4)


def iconEvents():
    mousePos = pygame.mouse.get_pos()
    mouseEvents = pygame.mouse.get_pressed()  # returns tuple of mouse events for each button
    # ex. : (True, False, False) for left click (Left click, Middle click, Right click)

    # following is only used to represent pushed mouse buttons as red/black squares
    # print(list)
    pygame.draw.rect(win, (255, 0, 0), ((20, 20), (30, 30)))
    if mouseEvents[0] == True:
        pygame.draw.rect(win, (0, 0, 0), ((20, 20), (30, 30)))

    pygame.draw.rect(win, (255, 0, 0), ((60, 20), (30, 30)))
    if mouseEvents[1] == True:
        pygame.draw.rect(win, (0, 0, 0), ((60, 20), (30, 30)))

    pygame.draw.rect(win, (255, 0, 0), ((100, 20), (30, 30)))
    if mouseEvents[2] == True:
        pygame.draw.rect(win, (0, 0, 0), ((100, 20), (30, 30)))

    # finds when bottom icons pressed
    if mouseEvents[0]:
        mousePos = pygame.mouse.get_pos()
        if 865 < mousePos[1] < 935:
            if 35 < mousePos[0] < 105:
                return 1
            if 135 < mousePos[0] < 205:
                return 2
            if 235 < mousePos[0] < 305:
                return 3
            if 335 < mousePos[0] < 405:
                return 4
            if 435 < mousePos[0] < 505:
                return 5


keys = pygame.key.get_pressed()  # all pressed keys

def screen1():
    win.blit(testingFont.render('---1---', True, (0, 0, 0)), (150, 18))


def screen2():
    win.blit(testingFont.render('---2---', True, (0, 0, 0)), (150, 18))


def screen3():
    win.blit(testingFont.render('---3---', True, (0, 0, 0)), (150, 18))

frameNum = 0 #used for swiping on screen 4 over multiple
accounts = names.makeNames() #calls from names.py
currentAccount = 0 #the card being viewed in list accounts
def screen4():
    #win.blit(testingFont.render('---4---', True, (0, 0, 0)), (150, 18))
    global currentAccount
    global frameNum

    cirRad = 65

    mousePos = pygame.mouse.get_pos()
    mouseEvents = pygame.mouse.get_pressed()
    pygame.draw.circle(win, (0, 255, 0), (360, 700), cirRad)
    pygame.draw.circle(win, (255, 0, 0), (180, 700), cirRad)
    pygame.draw.circle(win, (0, 0, 0), (360, 700), cirRad, width=5)
    pygame.draw.circle(win, (0, 0, 0), (180, 700), cirRad, width=5)

    if mouseEvents[0]:
        if 700-cirRad < mousePos[1] < 700+cirRad:
            if 180 - cirRad < mousePos[0] < 180 + cirRad and frameNum == 0:
                frameNum = -1
            if 360 - cirRad < mousePos[0] < 360 + cirRad and frameNum == 0:
                frameNum = 1

    if keys[pygame.K_LEFT] and frameNum == 0:
        frameNum = -1
    if keys[pygame.K_RIGHT] and frameNum == 0:
        frameNum = 1

    if frameNum < 0:
        frameNum -= 10

    if frameNum > 0:
        frameNum += 10

    if abs(frameNum) > 450:
        frameNum = 0
        currentAccount += 1
        currentAccount = currentAccount % len(accounts) #resets at end of list

    pygame.draw.rect(win, (130, 130, 130), ((3 + frameNum, 5), (540 - 6, 600)), border_radius=50)
    pygame.draw.rect(win, (0, 0, 0), ((3 + frameNum, 5), (540-6, 600)), border_radius=50, width=4)
    #pygame.draw.rect(win, (255, 255, 255), ((20 + frameNum, 25), (500, 500)), border_radius=35)

    win.blit(nameFont.render(accounts[currentAccount][0], True, (255, 255, 255)), (40 + frameNum, 540))
    win.blit(cardFont.render(accounts[currentAccount][1], True, (255, 255, 255)), (40 + frameNum, 570))
    win.blit(cardFont.render(accounts[currentAccount][2], True, (255, 255, 255)), (280 + frameNum, 550))
    win.blit(cardFont.render(accounts[currentAccount][3], True, (255, 255, 255)), (280 + frameNum, 570))
    try:
        win.blit(accounts[currentAccount][4], (20 + frameNum, 45))
    except: pass


tchrAcnts = [  # ['name', 'grade', 'district', 'school', 'years joined (int)', ]
    ['name', 'grade', 'district', 'school', ]
]
subAcnts = [
    []
]


def screen5():
    win.blit(testingFont.render('---5---', True, (0, 0, 0)), (150, 18))
    try:
        win.blit(names.drawDemoPic(), (170, 100))
    except: pass


lookup = {1: screen1, 2: screen2, 3: screen3, 4: screen4, 5: screen5}
def printScreen1to5(currentScreen):
    #print(currentScreen)
    lookup[currentScreen]()


currentScreen = 1
win.fill((250, 250, 250))
initOptionIcons()
pygame.mouse.set_cursor(pygame.cursors.arrow)  # messes with mouse style

running = True
while running:
    pygame.time.delay(10)  # time between frames (in ms)

    for event in pygame.event.get():  # when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(win, (250, 250, 250), ((0, 0), (540, 840)))
    pressedIcon = iconEvents()
    if pressedIcon:  # not directly defining currentScreen because it can return 'None'
        currentScreen = pressedIcon
    printScreen1to5(currentScreen)

    keys = pygame.key.get_pressed()  # all pressed keys
    if keys[pygame.K_SPACE]:
        pass  # key input for space bar. K_a, K_b, K_c etc

    pygame.display.flip()
pygame.quit()  # when the loop ends it closes the window
# heyo
# test
