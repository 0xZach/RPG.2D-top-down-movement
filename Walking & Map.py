import sys, pygame
from pygame.constants import QUIT
import pygame.locals
import numpy as np
import pathlib

__package__ = 'RPG'

from Classes import ClassMap
from Classes import PlayerMove
from maps import path_BrickTiles

#from RPG.Classes import ClassMap
#from RPG.maps import path_BrickTiles

# sys.path.append('./Classes')
# sys.path.append('./maps')

file_absolutePath = str(pathlib.Path('RPG').absolute())

# we get the path via the other file
map_n1 = path_BrickTiles.PATH


# the map is setup in an instance of the Class Map
zeMap = ClassMap.Map(1100,800, map_n1, file_absolutePath + '\maps\BrickTiles_surface_test.png')




# testing some methods
# ///////////////////////
# print(zeMap.getSizeTiles(),zeMap.getSizePx())
# 
# print(zeMap.toString())
# ///////////////////////

pygame.init()

MAX_FPS = 30 # self explanatory *cough*

# size of the window and a tile (temporary)
WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 1000,1000 # tuple to get a fixed size for the window
root = pygame.display.set_mode(WIN_SIZE) # this creates the window

TILE_SIZE = TILE_HEIGHT, TILE_WIDTH = (WIN_HEIGHT/10),(WIN_WIDTH/10)

# size of the player (temporary)
PLAYER_SIZE = PLAYER_HEIGHT,PLAYER_WIDTH = 100,74

# old way to get the coordinates of the player
# coord_x = (TILE_WIDTH*3)
# coord_y = (TILE_HEIGHT*6)
# row = 3
# line = 6

# new way
# the movement of the player is setup in an instance of the Class Player_Moving
zePlayerMove = PlayerMove.Player_Moving(np.array([TILE_WIDTH*1,1]),np.array([TILE_HEIGHT*1,1]),True)

# How to load an image and scale it
map = pygame.image.load(zeMap.getfileImage()).convert()
map = pygame.transform.scale(map,(1100,800))

# arrays to contain the different sprites
player = np.array([

pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 1-1.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)), # face north

pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 1-2.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)), # face left

pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 1-3.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)), # face right

pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 1-4.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)) # face south
])

player_walk = np.array([
    [
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-1.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)),
    
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-2.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)) 
    ], # up walk
    
    [
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-4.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)),
    
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-3.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)) 
    ], # left walk

    [
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-5.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)),
    
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-6.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)) 
    ], # right walk
    
    [
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-7.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT)),
    
    pygame.transform.scale(pygame.image.load(file_absolutePath + '\character\Sprite 2-8.png').convert_alpha(), (PLAYER_WIDTH,PLAYER_HEIGHT))
    ] # down walk
])


# TODO: fuck we'll quickly need those classes


# How to make a walking square
# 6th line, 3rd row so coordinates: 1000/8*6 = 750 and 1400/11*3 = 381.818181..

# TODO: make a function/method 'getCoordinates' that calculates this
# TODO: make a function 'move' that changes the place that we see and on the path
# it has to be based on the the path ofc, and on the size of 1 tile

#print(coord_x,coord_y)

# fills the background with black
root.fill((0,0,0))

# adds the image of the map **on top** of the other image(s), here it's only on top of the background
root.blit(map,map.get_rect())

# Display the character **after** the background, so it will be **on top**
root.blit(player[3], (zePlayerMove.getrealPos()[0], zePlayerMove.getrealPos()[1]))

#print(map_n1)
while True:
    key_pressed = pygame.key.get_pressed()
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        
        if event.type == QUIT or key_pressed[pygame.K_F4]:
            pygame.quit()
            sys.exit()

        
        if key_pressed[pygame.K_UP]:
            
            # new version

            # we need to convert these to ints because for god knows the reason it's just *always* taken as floats
            # in the instance of the object
            line = int(zePlayerMove.getmapPos()[1])
            row = int(zePlayerMove.getmapPos()[0])

            if map_n1[line-1][row] == 0:
            
                zePlayerMove.setmapPosY(line-1)


                for i in range(10):
                    
                    zePlayerMove.setrealPosY(zePlayerMove.getrealPos()[1]-TILE_HEIGHT/10)
                    
                    if i == 0 :
                        root.blit(map,map.get_rect())
                        root.blit(player[0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i >= 2 and i < 9 :
                        root.blit(map,map.get_rect())
                        if zePlayerMove.getLastMove() == True :
                            root.blit(player_walk[0][0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                            
                        elif zePlayerMove.getLastMove() == False :
                            root.blit(player_walk[0][1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i == 9 :
                        root.blit(map,map.get_rect())
                        root.blit(player[0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))

                    pygame.display.flip()
                    clock.tick(MAX_FPS)

                if zePlayerMove.getLastMove() == True :
                    zePlayerMove.setLastMove(False)

                elif zePlayerMove.getLastMove() == False :
                    zePlayerMove.setLastMove(True)
                
            else:
                root.blit(map,map.get_rect())
                root.blit(player[0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))

            """ # old version
            # if the path says it's ok to go there
            if map_n1[line-1][row] == 0:
                
                # we replace the tile the player is on with a 0
                map_n1[line][row] = 0

                # we move the player
                line -= 1

                # we replace the new tile with a 2
                map_n1[line][row] = 2

                # loop to smoothly erase and place a new draw of our player
                for i in range(10):
                    root.blit(map,map.get_rect()) # re-draws the background on top of the player
                    coord_y-=TILE_HEIGHT/10 # move by a bit
                    
                    # these if alternate between the left leg and right leg animation in the correct array
                    if(i%2 != 0):
                        root.blit(player_walk[0][0], (coord_x,coord_y))
                    elif(i%2 == 0 and i < 9):
                        root.blit(player_walk[0][1], (coord_x,coord_y))
                    
                    if(i == 9):
                        root.blit(map,map.get_rect())
                        root.blit(player[0], (coord_x,coord_y))
                    
                    #root.blit(player[0], (coord_x,coord_y)) # re-draws the player with the right direction and the new coordinates
                    pygame.display.flip() # updates it all
                    clock.tick(MAX_FPS) # the argument tells how many frames there is per second (here maximum of 15)
            else:
                root.blit(map,map.get_rect())
                root.blit(player[0], (coord_x,coord_y))
            """
            #print(map_n1)
        
        elif key_pressed[pygame.K_LEFT]:
            
            line = int(zePlayerMove.getmapPos()[1])
            row = int(zePlayerMove.getmapPos()[0])
            if map_n1[line][row-1] == 0:
            
                zePlayerMove.setmapPosX(row-1)


                for i in range(10):
                    
                    zePlayerMove.setrealPosX(zePlayerMove.getrealPos()[0]-TILE_WIDTH/10)
                    
                    if i == 0 :
                        root.blit(map,map.get_rect())
                        root.blit(player[1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i >= 2 and i < 9 :
                        root.blit(map,map.get_rect())
                        if zePlayerMove.getLastMove() == True :
                            root.blit(player_walk[1][0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                            
                        elif zePlayerMove.getLastMove() == False :
                            root.blit(player_walk[1][1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i == 9 :
                        root.blit(map,map.get_rect())
                        root.blit(player[1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))

                    pygame.display.flip()
                    clock.tick(MAX_FPS)

                if zePlayerMove.getLastMove() == True :
                    zePlayerMove.setLastMove(False)

                elif zePlayerMove.getLastMove() == False :
                    zePlayerMove.setLastMove(True)
                
            else:
                root.blit(map,map.get_rect())
                root.blit(player[1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
            #print(map_n1)

        elif key_pressed[pygame.K_RIGHT]:
            
            line = int(zePlayerMove.getmapPos()[1])
            row = int(zePlayerMove.getmapPos()[0])
            if map_n1[line][row+1] == 0:

                zePlayerMove.setmapPosX(row+1)


                for i in range(10):
                    
                    zePlayerMove.setrealPosX(zePlayerMove.getrealPos()[0]+TILE_WIDTH/10)
                    
                    if i == 0 :
                        root.blit(map,map.get_rect())
                        root.blit(player[2], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i >= 2 and i < 9 :
                        root.blit(map,map.get_rect())
                        if zePlayerMove.getLastMove() == True :
                            root.blit(player_walk[2][0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                            
                        elif zePlayerMove.getLastMove() == False :
                            root.blit(player_walk[2][1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i == 9 :
                        root.blit(map,map.get_rect())
                        root.blit(player[2], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))

                    pygame.display.flip()
                    clock.tick(MAX_FPS)

                if zePlayerMove.getLastMove() == True :
                    zePlayerMove.setLastMove(False)

                elif zePlayerMove.getLastMove() == False :
                    zePlayerMove.setLastMove(True)
                
            else:
                root.blit(map,map.get_rect())
                root.blit(player[2], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
            #print(map_n1)
        
        if key_pressed[pygame.K_DOWN]:
            line = int(zePlayerMove.getmapPos()[1])
            row = int(zePlayerMove.getmapPos()[0])
            if map_n1[line+1][row] == 0:
            
                zePlayerMove.setmapPosY(line+1)


                for i in range(10):
                    
                    zePlayerMove.setrealPosY(zePlayerMove.getrealPos()[1]+TILE_HEIGHT/10)
                    
                    if i == 0 :
                        root.blit(map,map.get_rect())
                        root.blit(player[3], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i >= 2 and i < 9 :
                        root.blit(map,map.get_rect())
                        if zePlayerMove.getLastMove() == True :
                            root.blit(player_walk[3][0], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                            
                        elif zePlayerMove.getLastMove() == False :
                            root.blit(player_walk[3][1], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
                    elif i == 9 :
                        root.blit(map,map.get_rect())
                        root.blit(player[3], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))

                    pygame.display.flip()
                    clock.tick(MAX_FPS)

                if zePlayerMove.getLastMove() == True :
                    zePlayerMove.setLastMove(False)

                elif zePlayerMove.getLastMove() == False :
                    zePlayerMove.setLastMove(True)
                
            else:
                root.blit(map,map.get_rect())
                root.blit(player[3], (zePlayerMove.getrealPos()[0],zePlayerMove.getrealPos()[1]))
            #print(map_n1)

        pygame.display.update()
        clock.tick(MAX_FPS)
        
        