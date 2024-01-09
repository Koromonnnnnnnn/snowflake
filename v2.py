import pygame
pygame.init()
pygame.display.set_caption("snowfall")  # sets the window title
screen = pygame.display.set_mode((500, 500))  # creates game screen
screen.fill((0, 0, 0))
clock = pygame.time.Clock()  # set up clock


# set up variables for flake 1 position
flake1x = 20
flake1y = 600  # start above the screen

# set up variables for flake 2 position
flake2x = 300
flake2y = 550

flake3x = 255
flake3y = 675

flake4x = 200
flake4y = 730

flake5x = 290
flake5y = 945

flake6x = 195
flake6y = 860

flake7x = 225
flake7y = 625

flake8x = 175
flake8y = 670

flake9x = 240
flake9y = 515

flake10x = 265
flake10y = 895

flake11x = 235
flake11y = 970

flake12x = 200
flake12y = 790


while (1):  # omg game lup---------
    clock.tick(60)  # FPS

    # physics section----

    # move flakes
    flake1y -= 2  # this one moves faster
    flake2y -= 1.55
    flake3y -= 2.43
    flake4y -= 1.27
    flake5y -= 2.85
    flake6y -= 2.35
    flake7y -= 1.72
    flake8y -= 2
    flake9y -= 1.35
    flake10y -= 2.6
    flake11y -= 2.12
    flake12y -= 1.19

    # reset flakes to top of screen
    if flake1y < 0:
        flake1y = 500
    if flake2y > 500:
        flake2y = 580
    if flake3y < 0:
        flake3y = 675
    if flake4y < 0:
        flake4y = 850
    if flake5y < 0:
        flake5y = 715
    if flake6y < 0:
        flake6y = 920
    if flake7y < 0:
        flake7y = 735
    if flake8y < 0:
        flake8y = 620
    if flake9y < 0:
        flake9y = 875
    if flake10y < 0:
        flake10y = 790
    if flake11y < 0:
        flake11y = 985
    if flake12y < 0:
        flake12y = 750
    # render section---
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (flake1x, flake1y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake2x, flake2y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake3x, flake3y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake4x, flake4y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake5x, flake5y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake6x, flake6y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake7x, flake7y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake8x, flake8y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake9x, flake9y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake10x, flake10y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake11x, flake11y), 3)
    pygame.draw.circle(screen, (255, 255, 255), (flake12x, flake12y), 3)
    pygame.display.flip()  # this actually puts the pixel on the screen

pygame.quit()
