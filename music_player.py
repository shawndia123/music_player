import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_LEFT, K_RIGHT, Rect
from random import randint

pygame.init()
pygame.mixer.init()
pygame.key.set_repeat(10,10)
FPSCLOCK = pygame.time.Clock()
SURFACE = pygame.display.set_mode((800,800))


def main():
    music_play = False
    music1_play = False
    Me = [400,400]
    font1 = pygame.font.SysFont(None,36)
    message_music1 = font1.render("Dream Lantern", True, (100,200,200))
    message_music1_rect = message_music1.get_rect()
    message_music1_rect.center = (200,200)
    
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    Me[1] -= 15 
                elif event.key == K_DOWN:
                    Me[1] += 15 
                elif event.key == K_LEFT:
                    Me[0] -= 15 
                elif event.key == K_RIGHT:
                    Me[0] += 15
        if not music_play:
            if music1_play == False:
                if (Me[0]-200)**2 + (Me[1]-200)**2 <= 110**2:
                    pygame.mixer.music.load("꿈의 등불.mp3")
                    pygame.mixer.music.play()
                    music_play = True
            elif music1_play == True:
                if (Me[0]-200)**2 + (Me[1]-200)**2 <= 110**2:
                    pygame.mixer.music.unpause()
                    music_play = True
        if music_play:
            if (Me[0]-200)**2 + (Me[1]-200)**2 > 110**2:
                pygame.mixer.music.pause()
                music1_play = True
                music_play = False
        
                    
                    
        SURFACE.fill((255,255,255))
        SURFACE.blit(message_music1, message_music1_rect)
        pygame.draw.circle(SURFACE, (100,200,200),(200,200),100,2)
        pygame.draw.circle(SURFACE, (153,255,255),Me,10)

        


        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()
