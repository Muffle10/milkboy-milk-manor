import pygame
import sprite
import game
# pygame setup
pygame.init()
pygame.font.init()

#===Game Info
width, height = (800,600)
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True



#===Drawing Info
frame_time = 0
my_font = pygame.font.SysFont('Comic Sans MS', 30)


#===Sprite Definitions
milkboy = sprite.AnimSprite("assets/milkboy.png", (4,1, 80))
rock = sprite.AnimSprite("assets/rock.png", (2,1, 80))
rock.index += 1
tree = sprite.AnimSprite("assets/tree.png", (1,1, 80))

background = sprite.Background("assets/map.png", (0,0), (width * 3, height * 3))
minimap = game.Map(pygame.Vector2(0,0), background, [tree.frame, rock.frame])
speed = pygame.Vector2(500,500)
while running:
        dt = clock.tick(60)/1000
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a]:
                milkboy.rect.x -= speed.x * dt
        if keys[pygame.K_d]:
                milkboy.rect.x += speed.x *dt
        if keys[pygame.K_w]:
                milkboy.rect.y -= speed.y *dt
        if keys[pygame.K_s]:
                milkboy.rect.y += speed.y *dt
        
        frame_time += 1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
        screen.fill("black")


        #frame_debug = my_font.render(f'{frame_time}', False, (100, 100, 100))
        #frame_text = my_font.render(f'{milkboy.index}', False, (100, 100, 100))
        #screen.blit(frame_debug, (40,50))
        #screen.blit(frame_text, (80, 50))

        minimap.update(milkboy)
        minimap.draw(screen)
        milkboy.animate(frame_time, 5)
        milkboy.draw(screen)
        pygame.draw.rect(screen, "black", (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 100,100))
        pygame.display.flip()
        clock.tick(60)
pygame.quit()