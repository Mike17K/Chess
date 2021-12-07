from pygame.constants import MOUSEBUTTONDOWN
import globalVariables
import pygame

def translateMove(): #in chess language
    pass


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
    


def translateCursorPosToSquares(pos,view):
    sq = globalVariables.squareDimentions
    if view ==1:
        return [pos[0]//sq[0],pos[1]//sq[1]]
    else:
        return [7-pos[0]//sq[0],7-pos[1]//sq[1]]

def addMoveToPath(args,pieccePos,targetPos):
    gs=copyArray(args['gameState'])
    
    args['gameHistory'].append(gs)
    args['gameHistoryTrackMoves'].append([pieccePos,targetPos])
    
    
    args['info'].append([True,True,True,True,[]]) 
    args['info'][-1][0]=args['info'][-2][0]
    args['info'][-1][1]=args['info'][-2][1]
    args['info'][-1][2]=args['info'][-2][2]
    args['info'][-1][3]=args['info'][-2][3]
    piece = args['gameHistory'][-2][pieccePos[1]][pieccePos[0]]
    if piece[1]=='p' and abs(pieccePos[1]-targetPos[1])==2:
        args['info'][-1][4]=targetPos
    if piece == 'wK': 
        args['info'][-1][0]=False
        args['info'][-1][1]=False
    elif piece == 'bK':
        args['info'][-1][2]=False
        args['info'][-1][3]=False
    elif piece == 'wR' and pieccePos==[7,7]: args['info'][-1][0]=False
    elif piece == 'wR' and pieccePos==[0,7]: args['info'][-1][1]=False
    elif piece == 'bR' and pieccePos==[7,0]: args['info'][-1][2]=False
    elif piece == 'bR' and pieccePos==[0,0]: args['info'][-1][3]=False

    print(args['info'][-1])

    
    


def undoMove(args):
    if len(args['gameHistory'])>1:
        args['gameState']=copyArray(args['gameHistory'][-2])
        args['gameHistory'] = args['gameHistory'][:-1]
        args['highlightedSquares'] = args['gameHistoryTrackMoves'][-2]
        args['gameHistoryTrackMoves'] = args['gameHistoryTrackMoves'][:-1]
        args['info'] = args['info'][:-1]

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

def copyArray(arr):
    temp = []
    for y in range(8):
        temp.append(["","","","","","","",""])
        for x in range(8):
            temp[y][x] = arr[y][x]
    return temp
            

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
    

