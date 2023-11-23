import pygame

class Pixel():

    def __init__(self, pos = (0,0), size = 5, color = ('teal')):
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
    donut_list = []
    running = True
    bg_color = 'black'
    color = 'teal'

    green_donut = pygame.image.load('pixel_art/green_cat_doughnut.png').convert_alpha()

    while running:
        for event in pygame.event.get():
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                create_list_of_pos(pixel_pos_list, mouse_pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pygame.display.toggle_fullscreen()
                if event.key == pygame.K_1:
                    color = pygame.Color('lightcoral')
                if event.key == pygame.K_2:
                    color = pygame.Color('darkgoldenrod1')    
                if event.key == pygame.K_3:
                    color = pygame.Color('seagreen1')
                if event.key == pygame.K_4:
                    color = pygame.Color('teal')
                if event.key == pygame.K_5:
                    color = pygame.Color('orchid3')            
                if event.key == pygame.K_c:
                    create_list_of_pos(circle_pos_list, mouse_pos)
                if event.key == pygame.K_w:
                    bg_color = pygame.Color('antiquewhite')
                if event.key == pygame.K_b:
                    bg_color = pygame.Color('black')
                if event.key == pygame.K_d:
                    create_list_of_pos(donut_list, mouse_pos)
                
        screen.fill(bg_color)
        for pos in donut_list:
            screen.blit(green_donut, (pos))
        for pos in pixel_pos_list:
            pixel.pos = pos
            pixel.draw(screen)
        for pos in circle_pos_list:
            pygame.draw.circle(screen, color, pos, 5)
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()

#create pixel sticker class
#add Pixel sticker at random based on mouse pos