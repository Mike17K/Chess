from os import pipe
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
                if args['gameState'][target[1]+i[1]][target[0]+i[0]][1]=='R':
                    if [target[1]+i[1],target[0]+i[0]]==[0,0]: args['info'][-1][3]=False
                    elif [target[1]+i[1],target[0]+i[0]]==[0,7]: args['info'][-1][2]=False
                    elif [target[1]+i[1],target[0]+i[0]]==[7,0]: args['info'][-1][1]=False
                    elif [target[1]+i[1],target[0]+i[0]]==[7,7]: args['info'][-1][0]=False
                args['gameState'][target[1]+i[1]][target[0]+i[0]]='--'
    args['gameState'][target[1]][target[0]] = '--'
    args['gameState'][pieccePos[1]][pieccePos[0]] = '--'
    

    #normal chess
    #args['gameState'][target[1]][target[0]] = args['gameState'][pieccePos[1]][pieccePos[0]]
    
def move(args,pieccePos,targetPos):
    
    piece = args['gameState'][pieccePos[1]][pieccePos[0]]
    #unpasan
    if piece=='wp' and len(args['info'][-1][4])!=0:
        if targetPos==[args['info'][-1][4][0],2]:
            args['gameState'][3][targetPos[0]]='--'     
            capture(args,[targetPos[0],3],pieccePos)
    if piece=='bp' and len(args['info'][-1][4])!=0:
        if targetPos==[args['info'][-1][4][0],5]:
            args['gameState'][4][targetPos[0]]='--'     
            capture(args,[targetPos[0],4],pieccePos)
    

    if args['gameState'][targetPos[1]][targetPos[0]]=='--': 
        args['gameState'][targetPos[1]][targetPos[0]]=args['gameState'][pieccePos[1]][pieccePos[0]]
    else:
        capture(args,targetPos)

    args['gameState'][pieccePos[1]][pieccePos[0]]='--'
    
    distaceX = pieccePos[0]-targetPos[0]
    if piece[1] == 'K' and abs(distaceX)==2: #roke
        if pieccePos[1] == 7:
            if distaceX>0: #big roke white
                args['gameState'][7][0]='--'
                args['gameState'][7][3]='wR'
            else:
                args['gameState'][7][7]='--'
                args['gameState'][7][5]='wR'
        if pieccePos[1] == 0:
            if distaceX>0: #big roke black
                args['gameState'][0][0]='--'
                args['gameState'][0][3]='bR'
            else:
                args['gameState'][0][7]='--'
                args['gameState'][0][5]='bR'


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
    
    
    args['info'].append([True,True,True,True,[]])  #the roke information and the unpasan
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


def leagalMoves(move):
    print("A")
    pass

def posibleMoves(args,pieccePos): #has to contane a piece
    posibleMove = []
    piece = args['gameState'][pieccePos[1]][pieccePos[0]]

    end=[False,False,False,False]
    if piece[1] in ['R','Q']:
        for i in range(1,7):
            if not end[0] and pieccePos[0]+i>=0 and pieccePos[0]+i<8: 
                if args['gameState'][pieccePos[1]][pieccePos[0]+i]=='--':
                    posibleMove.append([pieccePos[1],pieccePos[0]+i])
                elif args['gameState'][pieccePos[1]][pieccePos[0]+i][0]==piece[0]:
                    end[0]=True
                elif args['gameState'][pieccePos[1]][pieccePos[0]+i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1],pieccePos[0]+i])
                    end[0]=True
            
            if not end[1] and pieccePos[0]-i<8 and pieccePos[0]-i>=0: 
                if args['gameState'][pieccePos[1]][pieccePos[0]-i]=='--':
                    posibleMove.append([pieccePos[1],pieccePos[0]-i])
                elif args['gameState'][pieccePos[1]][pieccePos[0]-i][0]==piece[0]:
                    end[1]=True
                elif args['gameState'][pieccePos[1]][pieccePos[0]-i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1],pieccePos[0]-i])
                    end[1]=True
            
            if not end[2] and pieccePos[1]+i>=0 and pieccePos[1]+i<8: 
                if args['gameState'][pieccePos[1]+i][pieccePos[0]]=='--':
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]])
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]][0]==piece[0]:
                    end[2]=True
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]][0]!=piece[0]:
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]])
                    end[2]=True
            
            if not end[3] and pieccePos[1]-i<8 and pieccePos[1]-i>=0: 
                if args['gameState'][pieccePos[1]-i][pieccePos[0]]=='--':
                    posibleMove.append([pieccePos[1]-i,pieccePos[0]])
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]][0]==piece[0]:
                    end[3]=True
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]][0]!=piece[0]:
                    posibleMove.append([pieccePos[1]-i,pieccePos[0]])
                    end[3]=True

    end=[False,False,False,False]
    if piece[1] in ['B','Q']:
        for i in range(1,7):
            if not end[0] and pieccePos[0]+i>=0 and pieccePos[0]+i<8 and pieccePos[1]+i>=0 and pieccePos[1]+i<8: 
                if args['gameState'][pieccePos[1]+i][pieccePos[0]+i]=='--':
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]+i])
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]+i][0]==piece[0]:
                    end[0]=True
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]+i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]+i])
                    end[0]=True

            if not end[1] and pieccePos[0]-i>=0 and pieccePos[0]-i<8 and pieccePos[1]+i>=0 and pieccePos[1]+i<8: 
                if args['gameState'][pieccePos[1]+i][pieccePos[0]-i]=='--':
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]-i])
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]-i][0]==piece[0]:
                    end[1]=True
                elif args['gameState'][pieccePos[1]+i][pieccePos[0]-i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1]+i,pieccePos[0]-i])
                    end[1]=True
            
            if not end[2] and pieccePos[0]+i>=0 and pieccePos[0]+i<8 and pieccePos[1]-i>=0 and pieccePos[1]-i<8: 
                if args['gameState'][pieccePos[1]-i][pieccePos[0]+i]=='--':
                    posibleMove.append([pieccePos[1]-i,pieccePos[0]+i])
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]+i][0]==piece[0]:
                    end[2]=True
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]+i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1],pieccePos[0]+i])
                    end[2]=True
            
            if not end[3] and pieccePos[0]-i>=0 and pieccePos[0]-i<8 and pieccePos[1]-i>=0 and pieccePos[1]-i<8: 
                if args['gameState'][pieccePos[1]-i][pieccePos[0]-i]=='--':
                    posibleMove.append([pieccePos[1]-i,pieccePos[0]-i])
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]-i][0]==piece[0]:
                    end[3]=True
                elif args['gameState'][pieccePos[1]-i][pieccePos[0]-i][0]!=piece[0]:
                    posibleMove.append([pieccePos[1]-i,pieccePos[0]-i])
                    end[3]=True

    if piece[1] == 'N':
        for i in [[-2,1],[-2,-1],[-1,2],[-1,-2],[1,2],[1,-2],[2,1],[2,-1]]:
            if pieccePos[0] + i[0]>=0 and pieccePos[0] + i[0]<8 and pieccePos[1] + i[1]<8 and pieccePos[1] + i[1]>=0:
                if args['gameState'][pieccePos[1] + i[1]][pieccePos[0] + i[0]][0] != piece[0]:
                    posibleMove.append([pieccePos[1] + i[1],pieccePos[0] + i[0]])
    
    if piece[1] == 'p':
        if piece[0]=='w' :
            if pieccePos[1] == 6 and args['gameState'][5][pieccePos[0]] == '--' and args['gameState'][4][pieccePos[0]] == '--': posibleMove.append([4,pieccePos[0]])
            if pieccePos[1] >=1 and args['gameState'][pieccePos[1]-1][pieccePos[0]] == '--' : posibleMove.append([pieccePos[1]-1,pieccePos[0]])

            if pieccePos[0]+1<8 and pieccePos[1]>0:
                if args['gameState'][pieccePos[1]-1][pieccePos[0]+1][0] == 'b': posibleMove.append([pieccePos[1]-1,pieccePos[0]+1])
            if pieccePos[0]-1>=0 and pieccePos[1]>0:
                if args['gameState'][pieccePos[1]-1][pieccePos[0]-1][0] == 'b': posibleMove.append([pieccePos[1]-1,pieccePos[0]-1])

            if pieccePos[1]==3 and args['info'][-1][4]!=[]:
                posibleMove.append([2,args['info'][-1][4][0]])

        elif piece[0] == 'b':
            if pieccePos[1] == 1 and args['gameState'][2][pieccePos[0]] == '--' and args['gameState'][3][pieccePos[0]] == '--': posibleMove.append([3,pieccePos[0]])
            if pieccePos[1] <7 and args['gameState'][pieccePos[1]+1][pieccePos[0]] == '--' : posibleMove.append([pieccePos[1]+1,pieccePos[0]])

            if pieccePos[0]+1<8 and pieccePos[1]<7:
                if args['gameState'][pieccePos[1]+1][pieccePos[0]+1][0] == 'w': posibleMove.append([pieccePos[1]+1,pieccePos[0]+1])
            if pieccePos[0]-1>=0 and pieccePos[1]<7:
                if args['gameState'][pieccePos[1]+1][pieccePos[0]-1][0] == 'w': posibleMove.append([pieccePos[1]+1,pieccePos[0]-1])

            if pieccePos[1]==4 and args['info'][-1][4]!=[]:
                posibleMove.append([5,args['info'][-1][4][0]])
        
    if piece[1] == 'K':
        for i in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
            if pieccePos[0] +i[0]<8 and pieccePos[0] +i[0]>=0 and pieccePos[1] +i[1]<8 and pieccePos[1] +i[1]>=0:
                if args['gameState'][pieccePos[1] +i[1]][pieccePos[0] +i[0]][0] != piece[0]:
                    posibleMove.append([pieccePos[1] +i[1],pieccePos[0] +i[0]])

        if piece[0]=='w':
            if args['info'][-1][0] and args['gameState'][7][5]=='--' and args['gameState'][7][6]=='--': posibleMove.append([7,6])
            if args['info'][-1][1] and args['gameState'][7][1]=='--' and args['gameState'][7][2]=='--'and args['gameState'][7][3]=='--': posibleMove.append([7,2])
        if piece[0]=='b':
            if args['info'][-1][2] and args['gameState'][0][5]=='--' and args['gameState'][0][6]=='--': posibleMove.append([0,6])
            if args['info'][-1][3] and args['gameState'][0][1]=='--' and args['gameState'][0][2]=='--'and args['gameState'][0][3]=='--': posibleMove.append([0,2])
            

    #print(posibleMove)
    return posibleMove

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
                
                if [clickedSquare[1],clickedSquare[0]] in posibleMoves(args,beforeState[0]): #move if is legal and if not set the array highlightedSquares to []
                    move(args,beforeState[0],clickedSquare)

                    if len(args['highlightedSquares'])>2:
                        args['highlightedSquares'] = args['highlightedSquares'][2:]
                    return [None,False]
                else:
                    if len(args['highlightedSquares'])>2:
                        args['highlightedSquares'] = args['highlightedSquares'][:-2]
                    else:
                        args['highlightedSquares'] = []
                    return [None,False]
    else:   
        if beforeState[0]!= None :
            if beforeState[0] == clickedSquare: return [clickedSquare,False]
            else: 
                args['highlightedSquares'].append(clickedSquare)
                
                if [clickedSquare[1],clickedSquare[0]] in posibleMoves(args,beforeState[0]): #move if is legal and if not set the array highlightedSquares to []
                    move(args,beforeState[0],clickedSquare)

                    if len(args['highlightedSquares'])>2:
                        args['highlightedSquares'] = args['highlightedSquares'][2:]
                    return [None,False]
                else:
                    if len(args['highlightedSquares'])>2:
                        args['highlightedSquares'] = args['highlightedSquares'][:-2]
                    else:
                        args['highlightedSquares'] = []
                    return [None,False]
        else:
            return  [None,False]
    

