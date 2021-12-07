from pygame.constants import MOUSEBUTTONDOWN
import globalVariables
import pygame

def capture(args,target,pieccePos):
    #atomic rool
    
    for i in [[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1],[0,-1],[0,1]]:
        if target[1]+i[1]<8 and target[0]+i[0]<8 and target[1]+i[1]>=0 and target[0]+i[0]>=0:
            if args['gameState'][target[1]+i[1]][target[0]+i[0]] not in ['--','bp','wp']:
                args['gameState'][target[1]+i[1]][target[0]+i[0]]='--'
    args['gameState'][target[1]][target[0]] = '--'
    

    #normal chess
    #args['gameState'][target[1]][target[0]] = args['gameState'][pieccePos[1]][pieccePos[0]]
    
def move(args,pieccePos,targetPos):
    #add roke
    #unpasan
    #takes

    if args['gameState'][targetPos[1]][targetPos[0]]=='--': 
        args['gameState'][targetPos[1]][targetPos[0]]=args['gameState'][pieccePos[1]][pieccePos[0]]
    else:
        capture(args,targetPos,pieccePos)

    args['gameState'][pieccePos[1]][pieccePos[0]]='--'
    
    addMoveToPath(args,pieccePos,targetPos)
    

def translateMove(): #in chess language
    pass

def translateCursorPosToSquares(pos,view):
    sq = globalVariables.squareDimentions
    if view ==1:
        return [pos[0]//sq[0],pos[1]//sq[1]]
    else:
        return [7-pos[0]//sq[0],7-pos[1]//sq[1]]

def addMoveToPath(args,pieccePos,targetPos):
    gs = []
    for y in range(8):
        gs.append([])
        for x in range(8):
            gs[y].append("--")
            gs[y][x] = args['gameState'][y][x]
    args['gameHistory'].append(gs)

    args['gameHistoryTrackMoves'].append([pieccePos,targetPos])
    


def undoMove(args):
    if len(args['gameHistory'])>1:
        for y in range(8):
            for x in range(8):
                args['gameState'][y][x] = args['gameHistory'][-2][y][x]
        
        args['gameHistory'] = args['gameHistory'][:-1]
        args['highlightedSquares'] = args['gameHistoryTrackMoves'][-2]
        args['gameHistoryTrackMoves'] = args['gameHistoryTrackMoves'][:-1]

    if len(args['gameHistory'])==1:
        args['highlightedSquares']=[]



def truckAttackingSquares(array):
    pass

def printBoard(gs):
    for y in range(8):
        for x in range(8):
            print(gs[y][x],end = '  ')
        print()
    print()

def updateVariables():
    pass

def leagalMoves(move):
    print("A")
    pass

def posibleMoves(square): #has to contane a piece
    pass

def clickHandler(args,event,pos):
    beforeState = args['clickSignal']
    clickedSquare = translateCursorPosToSquares(pos,args['view'])

    if event.type == pygame.MOUSEBUTTONDOWN: 
        if beforeState[0] == None :
            if args['gameState'][clickedSquare[1]][clickedSquare[0]]=='--': return [None,False]
            args['highlightedSquares'].append(clickedSquare)
            return [clickedSquare,True]
        elif beforeState[0]!= None :
            if beforeState[0] == clickedSquare:
                args['highlightedSquares'] = args['highlightedSquares'][:-1]
                return [None,False]
            else:
                args['highlightedSquares'].append(clickedSquare)
                
                #move if is legal and if not set the array highlightedSquares to []
                move(args,beforeState[0],clickedSquare)

                if len(args['highlightedSquares'])>2:
                    args['highlightedSquares'] = args['highlightedSquares'][2:]
                return [None,False]
    else:   
        if beforeState[0]!= None :
            if beforeState[0] == clickedSquare: return [clickedSquare,False]
            else: 
                args['highlightedSquares'].append(clickedSquare)
                
                #move if is legal and if not set the array highlightedSquares to []
                move(args,beforeState[0],clickedSquare)

                if len(args['highlightedSquares'])>2:
                    args['highlightedSquares'] = args['highlightedSquares'][2:]
                return [None,False]
        else:
            return  [None,False]
    

