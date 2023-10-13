import pygame

pygame.font.init() #initializes fonts
pygame.init()

win = pygame.display.set_mode((1000, 500)) #window size
pygame.display.set_caption("pygame") #window title
testFont = pygame.font.Font(None, 50) #defines font type




running = True
while running:
    pygame.time.delay(60) #time between frames (in ms)

    for event in pygame.event.get(): #when close button pushed, loop ends
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() #all pressed keys

    win.fill((60, 60, 60)) #fills screen background





    #This makes the rectangles on screen

    pygame.draw.rect(win, (255, 255, 255), ((15, 10), (75, 50)))
    #rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)))


    pygame.draw.rect(win, (255, 255, 255), ((15, 70), (75, 50)), border_radius = 10)
    #rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)), rounded corners = x)


    pygame.draw.rect(win, (255, 255, 255), ((15, 130), (75, 50)), width = 5)
    #rect(window, color in rgb, ((xpos top left, ypostopleft), (x-width, y-height)), side width = x)



    if keys[pygame.K_SPACE]:
        pass #key input for space bar. K_a, K_b, K_c etc




    pygame.display.update()
pygame.quit() #when the loop ends it closes the window
#heyo
