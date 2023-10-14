import pygame

pygame.font.init()  # initializes fonts
pygame.init()


win = pygame.display.set_mode((540, 960))  # window size - 1080p but halved to make it fit. iphone 15 is only 1179 so 1080 is about right for most phones
pygame.display.set_caption("Teacher app thing")  # window title - to be changed
testFont = pygame.font.Font(None, 50)  # defines font style



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
    pygame.draw.rect(win, (0, 0, 0), ((270 - 2, 900 - 25), (4, 50)),border_radius=2)  # -2 and -25 are used to position lines to centered in the circle
    pygame.draw.rect(win, (0, 0, 0), ((270 - 25, 900 - 2), (50, 4)), border_radius=2)

    # icon #4 -
    #pygame.draw.circle(win, (0, 0, 0), (370, 900), 35, width=4)
    pygame.draw.rect(win, (0, 0, 0), ((370 - 5, 900-5), (25, 35)), border_radius=2)

    pygame.draw.rect(win, (250,250,250), ((370 - 24, 900 - 25), (32, 46)), border_radius=2, width=2)
    pygame.draw.rect(win, (0, 0, 0), ((370 - 20, 900 - 21), (26, 40)), border_radius=2)

    # icon #5 - account settings
    pygame.draw.circle(win, (0, 0, 0), (470, 900), 22)
    pygame.draw.circle(win, (250, 250, 250), (470, 900+20), 15)
    pygame.draw.circle(win, (250, 250, 250), (470, 900 - 6), 7)
    pygame.draw.circle(win, (0, 0, 0), (470, 900), 22, width = 4)


win.fill((250, 250, 250))
initOptionIcons()

running = True
while running:
    pygame.time.delay(10)  # time between frames (in ms)

    for event in pygame.event.get():  # when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # all pressed keys

    pygame.draw.rect(win, (250, 250, 250), ((0, 0), (540, 840)))



    pygame.mouse.set_cursor(pygame.cursors.arrow)  # messes with mouse style




    if keys[pygame.K_SPACE]:
        pass  # key input for space bar. K_a, K_b, K_c etc

    pygame.display.flip()
pygame.quit()  # when the loop ends it closes the window
# heyo
# test
