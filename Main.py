
import requests
import json
import os, sys
from threading import Timer
from _thread import *

import pygame

image_path = "src/icons/"

font_size=200
FULL_SCREEN = 0

def main():

    pygame.init()

    #print(pygame.font.get_fonts())
    size = width, height = 1080, 720
    black = 0,0,0
    font = pygame.font.SysFont(None,font_size)

    if(FULL_SCREEN):
        screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(size)

    #Loop that renders images
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        elo = 3521

        rank = determine_rank(elo)

        text = font.render(str(elo),True,[255,255,255])

        rank_image = pygame.image.load(image_path + rank + ".png")
        rank_rect = rank_image.get_rect()

        rank_rect.x=0
        rank_rect.y=200

        text_rect= text.get_rect()
        text_rect.x=220
        text_rect.y=265

        screen.fill(black)
        screen.blit(rank_image,rank_rect)
        screen.blit(text,text_rect)

        pygame.display.flip()

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

def data_fetch():
    account=""
    URL = "https://ow-api.com/v1/stats/pc/eu/"+account+"/profile"

    r=requests.get(url=URL,params="")
    data=r.json()

    with open("data.json","w")as f:
        f.write(json.dumps(data,indent=4,sort_keys=True))

    comp_stats=data['rating']
    print(account,comp_stats)

if __name__ == '__main__':
    main()
