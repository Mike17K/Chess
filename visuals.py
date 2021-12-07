from typing import final
import pygame
import globalVariables

def loadImages():
    iconsName = ['wp','bp','wR','wB','wN','wQ','wK','bR','bB','bN','bQ','bK']
    pngs = {}
    for i in iconsName:
        pngs.update({i: pygame.image.load('icons/'+i+".png")})
    return pngs

icon = loadImages()

def drawBoard(screen,args={}):
    sq = globalVariables.squareDimentions
    color = [globalVariables.black_color,globalVariables.white_color]
    for y in range(8):
        for x in range(8):
            finalColor = color[(y+x+1)%2]
            if args['highlightedSquares']!=None:
                if [y,x] in args['highlightedSquares']: finalColor = globalVariables.highlightColor #draw high lighted squares
            if args['view']==1: #draw the squares
                pygame.draw.rect(screen,finalColor,(y*sq[0],x*sq[0],sq[0],sq[1]))
            else:
                pygame.draw.rect(screen,finalColor,((7-y)*sq[0],(7-x)*sq[0],sq[0],sq[1]))

            


            if args['gameState'][x][y]!="--": #draw the pieces
                disp_icon = icon[args['gameState'][x][y]]
                if args['clickSignal'][1] and args['clickSignal'][0]==[y,x]: continue
                if args['view']==1:
                    screen.blit(pygame.transform.scale(disp_icon,(sq[0],sq[0])), (y*sq[0],x*sq[0]))
                else:
                    screen.blit(pygame.transform.scale(disp_icon,(sq[0],sq[0])), ((7-y)*sq[0],(7-x)*sq[0]))
            
    if args['clickSignal'][1]: #draw drowing piece
        disp_icon = icon[args['gameState'][args['clickSignal'][0][1]][args['clickSignal'][0][0]]]
        screen.blit(pygame.transform.scale(disp_icon,(sq[0],sq[0])), [pygame.mouse.get_pos()[0]-sq[0]/2,pygame.mouse.get_pos()[1]-sq[1]/2])
            
            


    pygame.display.flip()

def createWindow():    
    screen = pygame.display.set_mode(globalVariables.windowDimentions)
    screen.fill(globalVariables.background_colour)
    pygame.display.set_caption(globalVariables.captionText)
    return screen
    


