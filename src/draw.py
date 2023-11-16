import pygame

class Pixel():

    def __init__(self, pos = (0,0), size = 5, color = ('aqua')):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(color)
        self.surface = self.update_surface()

        
    # def change_color(self):
    #     color_list = ['darkgoldenrod1', 'lightcoral', 
    #                   'seagreen1', 'teal', 'orchid3']
    #     for color in color_list:
    #         self.color = color
    #         print(self.color)


    def update_surface(self):
        surf = pygame.Surface((self.size, self.size))
        surf.fill(self.color)
        return surf

    def draw(self, surface):
        surface.blit(self.surface, self.pos)

def create_list_of_pos(list, pos):
    list.append(pos)
    return list
    

def main():
    pygame.init()
    pygame.display.set_caption("Pixel Draw")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    pixel = Pixel()
    pixel_pos_list = []
    color_list = ['aqua', 'darkgoldenrod1', 'lightcoral', 'seagreen1', 'teal', 'orchid3']

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                create_list_of_pos(pixel_pos_list, mouse_pos)
            # if event.type == pygame.KEYDOWN:
            #     pixel.change_color()      
        pixel.color = pygame.Color('pink')
        screen.fill('black')
        for pos in pixel_pos_list:
            pixel.pos = pos
            pixel.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()

#toggle screen from off white to black
#create shape class
#add shape to scren according to mouse pos on KEYDOWN
#create pixel sticker class
#add Pixel sticker at random based on mouse pos