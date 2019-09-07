import os, sys
from overwatch import Overwatch
import time

import pygame

image_path = "src/icons/"

font_size=180
FULL_SCREEN = 0

timer_length = 300 #5 minutes


def main():

    #                   platform,region,account
    overwatch=Overwatch("","","")

    #overwatch.profile_to_json()

    pygame.init()

    #print(pygame.font.get_fonts())
    size = width, height = 1080, 720
    black = 0,0,0
    font = pygame.font.SysFont(None,font_size)

    if(FULL_SCREEN):
        screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)

    #Loop that fetches data and renders images



    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        elo = overwatch.get_rating()
        tank_rating=elo[0]
        damage_rating=elo[1]
        support_rating=elo[2]
        average_rating=elo[3]

        tank_rank = determine_rank(tank_rating)
        damage_rank = determine_rank(damage_rating)
        support_rank = determine_rank(support_rating)
        average_rank = determine_rank(average_rating)

        tank_text = font.render(str(tank_rating)+"-Tank",True,[255,255,255])
        damage_text = font.render(str(damage_rating)+"-Damage",True,[255,255,255])
        support_text = font.render(str(support_rating)+"-Support",True,[255,255,255])
        text = font.render(str(average_rating)+"-Average",True,[255,255,255])

        tank_image = pygame.image.load(image_path + tank_rank + ".png")
        damage_image = pygame.image.load(image_path + damage_rank + ".png")
        support_image = pygame.image.load(image_path + support_rank + ".png")
        rank_image = pygame.image.load(image_path + average_rank + ".png")

        tank_rect = tank_image.get_rect()
        damage_rect = damage_image.get_rect()
        support_rect = support_image.get_rect()
        rank_rect = rank_image.get_rect()

        tank_rect.x=0
        damage_rect.x=0
        support_rect.x=0
        tank_rect.x=0

        tank_rect.y=0
        damage_rect.y=150
        support_rect.y=300
        rank_rect.y=450

        tank_text_rect= tank_text.get_rect()
        damage_text_rect= damage_text.get_rect()
        support_text_rect= support_text.get_rect()
        text_rect= text.get_rect()

        tank_text_rect.x=220
        damage_text_rect.x=220
        support_text_rect.x=220
        text_rect.x=220


        tank_text_rect.y=50
        damage_text_rect.y=200
        support_text_rect.y=350
        text_rect.y=500

        screen.fill(black)

        screen.blit(tank_image,tank_rect)
        screen.blit(damage_image,damage_rect)
        screen.blit(support_image,support_rect)
        screen.blit(rank_image,rank_rect)

        screen.blit(tank_text,tank_text_rect)
        screen.blit(damage_text,damage_text_rect)
        screen.blit(support_text,support_text_rect)
        screen.blit(text,text_rect)

        pygame.display.flip()

        time.sleep(timer_length)

def determine_rank(elo):

    if(elo >= 4000):
        return "grandmaster"

    if(elo >= 3500):
        return "master"

    if(elo >= 3000):
        return "diamond"

    if(elo >= 2500):
        return "platinum"

    if(elo >= 2000):
        return "gold"

    if(elo >= 1500):
        return "silver"

    return "bronze"




if __name__ == '__main__':
    main()
