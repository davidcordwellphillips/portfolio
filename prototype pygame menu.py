import pygame as py
py.init()

window_w = 1920
window_h = 1080
brown = (185,122,87)
brown_hover = (193,137,106)
white = (255,255,255)
title_beige = (239,228,176)

def text_objects(text, font):
    textSurface = font.render(text, True, title_beige)
    return textSurface, textSurface.get_rect()

screen = py.display.set_mode((window_w,window_h))

bg = py.image.load("bg.png")

clock = py.time.Clock()

done = False
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
    screen.blit(bg,(0,0))
    
    mouse = py.mouse.get_pos()
    if 600+200 > mouse[0] > 600 and 650+100 > mouse[1] > 650:
        py.draw.rect(screen, brown_hover, (600, 650, 200, 100))
    else:
            py.draw.rect(screen, brown, (600, 650, 200, 100))

    if 1300+200 > mouse[0] > 1300 and 650+100 > mouse[1] > 650:
        py.draw.rect(screen, brown_hover, (1300, 650, 200, 100))
    else:
        py.draw.rect(screen, brown, (1300, 650, 200, 100))
        
    if 950+200 > mouse[0] > 950 and 650+100 > mouse[1] > 650:
        py.draw.rect(screen, brown_hover, (950, 650, 200, 100))
    else:
        py.draw.rect(screen, brown, (950, 650, 200, 100))

    menuText = py.font.Font("freesansbold.ttf", 26)
    textSurf, textRect = text_objects("START", menuText)
    textRect.center = ((600+(200/2)), (650+(100/2)))
    screen.blit(textSurf, textRect)

    menuText = py.font.Font("freesansbold.ttf", 26)
    textSurf, textRect = text_objects("STORY", menuText)
    textRect.center = ((950+(200/2)), (650+(100/2)))
    screen.blit(textSurf, textRect)

    menuText = py.font.Font("freesansbold.ttf", 26)
    textSurf, textRect = text_objects("CONTROLS", menuText)
    textRect.center = ((1300+(200/2)), (650+(100/2)))
    screen.blit(textSurf, textRect)


    
    py.display.flip()
    
    clock.tick(60)



py.quit()
