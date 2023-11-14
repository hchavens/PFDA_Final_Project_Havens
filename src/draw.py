import pygame

class Pixel():

    def __init__(self, pos = (0,0), size = 5, color = "red"):
        self.pos = pos
        self.size = size
        self.color = color
        self.surface = self.update_surface()

    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf
    
    def draw(self, surface):
        surface.blit(self.surface, self.pos)

def create_list_of_pos(list, pos):
    list.append(pos)
    print(list)
    return list
    

def main():
    pygame.init()
    pygame.display.set_caption("Pixel Draw")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    pixel = Pixel()
    pos_list = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                create_list_of_pos(pos_list, mouse_pos)

        screen.fill('black')
        for pos in pos_list:
            pixel.pos = pos
            pixel.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()

#toggle screen from off white to black
#draw pixel to screen according to mouse position
#create shape class
#add shape to scren according to mouse pos on KEYDOWN
#create pixel sticker class
#add Pixel sticker at random based on mouse pos