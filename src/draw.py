import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Pixel Draw")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        screen.fill('black')
    pygame.quit()

if __name__=="__main__":
    main()
#create main function with screen and exit
#create game loop
#toggle screen from off white to black
#create pixel class
#draw pixel to screen according to mouse position
#create shape class
#add shape to scren according to mouse pos on KEYDOWN
#create pixel sticker class
#add Pixel sticker at random based on mouse pos