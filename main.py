from pygame.constants import K_ESCAPE, K_LEFT, K_p, K_r, K_w
import engine
import fanctions
import visuals
import globalVariables
import pygame 
import time


pygame.init()
screen = visuals.createWindow()
clock = pygame.time.Clock()


gameState = [["bR","bN","bB","bQ","bK","bB","bN","bR",],
["bp","bp","bp","bp","bp","bp","bp","bp",],
["--","--","--","--","--","--","--","--"],
["--","--","--","--","--","--","--","--"],
["--","--","--","--","--","--","--","--"],
["--","--","--","--","--","--","--","--"],
["wp","wp","wp","wp","wp","wp","wp","wp"],
["wR","wN","wB","wQ","wK","wB","wN","wR"]]
    
args= { 'gameState' : gameState , 'view': 1 , 'clickSignal': [None,False] , 'highlightedSquares': [] , 'gameHistory': [], 'gameHistoryTrackMoves': [[None,None]]}

temp = []
for y in range(8): #adding the starting pos in the history
    temp.append([])
    for x in range(8):
        temp[y].append(args['gameState'][y][x])
args['gameHistory'].append(temp)

#fps mezure
loops=0
startTime=time.time()

running = True

while running:
    

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_r: args['view'] *= -1
            if event.key == K_LEFT: fanctions.undoMove(args) #undoes a move and del from history
            if event.key == K_p: # by pressing "P" it prints the history of the moves
                print(len(args['gameHistory']))
                for i in args['gameHistory']:
                    fanctions.printBoard(i)

        if (event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP) and event.button==1: #left click handle
            args['clickSignal'] = fanctions.clickHandler(args,event,pygame.mouse.get_pos())
            #print(args['highlightedSquares'])


    visuals.drawBoard(screen,args)

    loops+=1
    if loops==100: 
        #print(100/(time.time()-startTime))
        loops=0
        startTime=time.time()

    clock.tick(400) #loop max limit of the program is around 400 by now