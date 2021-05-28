from numpy import array
import pathlib
import pygame as pg
from Classes.PlayerMove import Player_Moving
from Classes.WinControl import WinRoot



# moves the character around
def move(map, mapImage, player: Player_Moving, direction: int, root: WinRoot, facing_sprites: array, walking_sprites: array):
    row = int(player.getmapPos()[0])
    line = int(player.getmapPos()[1])

    if(direction == 0):
        rowCheck = row
        lineCheck = line-1
        tileMove = (- root.getTileSize()[1])
    elif(direction == 1):
        rowCheck = row-1
        lineCheck = line
        tileMove = (- root.getTileSize()[0])
    elif(direction == 2):
        rowCheck = row+1
        lineCheck = line
        tileMove = (root.getTileSize()[0])
    elif(direction == 3):
        rowCheck = row
        lineCheck = line+1
        tileMove = (root.getTileSize()[1])

    if map[lineCheck][rowCheck] == 0:
    
        if(direction == 0 or direction == 3):
            player.setmapPosY(lineCheck)
        elif(direction == 1 or direction == 2):
            player.setmapPosX(rowCheck)

        for i in range(10):
            
            if(direction == 0 or direction == 3):
                player.setrealPosY(player.getrealPos()[1]+ tileMove/10)
            elif(direction == 1 or direction == 2):
                player.setrealPosX(player.getrealPos()[0]+ tileMove/10)
            
            if i == 0 :
                root.getRoot().blit(mapImage,mapImage.get_rect())
                root.getRoot().blit(facing_sprites[direction], (player.getrealPos()[0],player.getrealPos()[1]))
            elif i >= 2 and i < 9 :
                root.getRoot().blit(mapImage,mapImage.get_rect())
                if player.getLastMove() == True :
                    root.getRoot().blit(walking_sprites[direction][0], (player.getrealPos()[0],player.getrealPos()[1]))
                    
                elif player.getLastMove() == False :
                    root.getRoot().blit(walking_sprites[direction][1], (player.getrealPos()[0],player.getrealPos()[1]))
            elif i == 9 :
                root.getRoot().blit(mapImage,mapImage.get_rect())
                root.getRoot().blit(facing_sprites[direction], (player.getrealPos()[0],player.getrealPos()[1]))

            pg.display.flip()
            root.ticking(root.getFPS())

        if player.getLastMove() == True :
            player.setLastMove(False)

        elif player.getLastMove() == False :
            player.setLastMove(True)
        
    else:
        root.getRoot().blit(mapImage,mapImage.get_rect())
        root.getRoot().blit(facing_sprites[direction], (player.getrealPos()[0],player.getrealPos()[1]))









def loadImages(imagePath, width, height):

    # get absolute path to /RPG
    file_absolutePath = str(pathlib.Path('RPG').absolute())

    return pg.transform.scale(pg.image.load(file_absolutePath + imagePath).convert_alpha(), (width,height))
