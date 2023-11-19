import pygame
import random

class Pixel():

    def __init__(self, pos = (0,0), size = 5, color = ('aqua')):
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
    return list


def main():
    pygame.init()
    pygame.display.set_caption("Pixel Draw")
    resolution = (800, 800)
    screen = pygame.display.set_mode(resolution)
    pixel = Pixel()
    pixel_pos_list = []
    circle_pos_list = []
    color_list = ['aqua', 'darkgoldenrod1', 'lightcoral', 'seagreen1', 'teal', 'orchid3']
    running = True
    color = 'lightcoral'
    while running:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_list_of_pos(pixel_pos_list, mouse_pos)
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_1:
                #     color = pygame.Color('lightcoral')
                #     return color
                if event.key == pygame.K_c:
                    create_list_of_pos(circle_pos_list, mouse_pos)
                
        screen.fill('black')
        for pos in pixel_pos_list:
            pixel.pos = pos
            pixel.draw(screen)
        for pos in circle_pos_list:
            pygame.draw.circle(screen, color, pos, 5)
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()

#toggle screen from off white to black
#create shape class
#add shape to scren according to mouse pos on KEYDOWN
#create pixel sticker class
#add Pixel sticker at random based on mouse pos