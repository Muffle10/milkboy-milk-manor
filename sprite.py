import pygame
class AnimSprite(pygame.sprite.Sprite):
    def __init__(self, image_src, size = (1,1,200)):
        '''
           @size:
                index 0: x-size
                index 1: y-size
                index 2: scale
        '''
        super()
        self.index = 0
        self.size = size
        self.image = pygame.image.load(image_src)
        self.image = pygame.transform.scale(self.image, (size[0] *size[2],size[1]*size[2]))
        self.frame = self.image.subsurface((self.index,0,size[1] * size[2], size[1] * size[2]))
        self.rect = self.frame.get_rect()
    def update_frame(self):
        self.frame = self.image.subsurface((self.index * self.size[2],0,self.size[1] * self.size[2], self.size[1] * self.size[2]))
    def animate(self, frames, speed):
        if (frames % speed == 0):
            self.index += 1
        if self.index > self.size[0] - 1:
            self.index = 0
        self.update_frame()
    def draw(self, surface):
        surface.blit(self.frame, self.rect)
class Background():
    def __init__(self, image_src, coordinate, scale):
        self.image = pygame.image.load(image_src)
        self.image = pygame.transform.scale(self.image, scale)
        self.coordinate = coordinate
    def draw(self, surface):
        surface.blit(self.image, self.image.get_rect())
