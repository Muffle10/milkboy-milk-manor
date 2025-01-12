import sprite
import pygame
'''

Todo:
- make Player class with velocity
- make enemy class
- make objstacle class
'''
class ObjectType:
    Tree = 0
    Rock = 1
    Well = 2
    Fence = 3
    Bush = 4
'''
Layout system:
- list of tuples with 3 items:
    1: x position
    2: y position
    3: type
'''
class Map():
    def __init__(self, starting_index, background: sprite.Background, objects: list = [pygame.Surface((100,100))]):
        self.index = starting_index
        self.map = [[
            [[300, 300, ObjectType.Rock]], 
                    [[100,100,ObjectType.Tree]], 
                    [[100,100,ObjectType.Tree]]],
                    [[[100,100,ObjectType.Tree]], [[100,100,ObjectType.Tree]], [[100,100,ObjectType.Tree]]],
                    [[[100,100,ObjectType.Tree]], [[100,100,ObjectType.Tree]], [[100,100,ObjectType.Tree]]]]
        self.current_layout = [[300, 300, ObjectType.Rock], [350, 250, ObjectType.Rock]]
        #Maybe make it load at initialization: Did it
        #Object index:
        #input object mapping and the draw funtion uses enum to display it
        self.objects = objects
        self.background = background
        self.current_background = background.image.subsurface((starting_index.x * 800,starting_index.y *600, 800,600))
    def draw(self,screen):
        screen.blit(self.current_background, self.current_background.get_rect())
        for [x,y,obj] in self.current_layout:
            screen.blit(self.objects[obj], (x,y))
    def update(self, player):
        self.current_background = self.background.image.subsurface((self.index.x * 800,self.index.y * 600, 800,600))
        if self.index.x == 3:
                self.index.x = 0
        if player.rect.x > 800:
            self.index.x += 1
            player.rect.x = 0
            self.current_layout = self.map[int(self.index.x)][int(self.index.y)]
        if player.rect.x < -1 * player.rect.width:
            self.index.x -= 1
            player.rect.x = 800
            self.current_layout = self.map[int(self.index.x)][int(self.index.y)]
        if player.rect.y > 600:
            self.index.y +=1
            player.rect.y = 0
            self.current_layout = self.map[int(self.index.x)][int(self.index.y)]
        if player.rect.y < -1 * player.rect.height:
            self.index.y -= 1
            player.rect.y = 600
            self.current_layout = self.map[int(self.index.x)][int(self.index.y)]