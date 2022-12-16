import copy
from collections import defaultdict

def ActionPuzzel(puzzel,action,blankposition):
    if action == "up" : 
        puzzel[blankposition[0]-1][blankposition[1]] , puzzel[blankposition[0]][blankposition[1]] = puzzel[blankposition[0]][blankposition[1]] , puzzel[blankposition[0]-1][blankposition[1]]
        return puzzel
    if action == "down" : 
        puzzel[blankposition[0]+1][blankposition[1]] , puzzel[blankposition[0]][blankposition[1]] = puzzel[blankposition[0]][blankposition[1]] , puzzel[blankposition[0]+1][blankposition[1]]
        return puzzel
    if action == "left" : 
        puzzel[blankposition[0]][blankposition[1]-1] , puzzel[blankposition[0]][blankposition[1]] = puzzel[blankposition[0]][blankposition[1]] , puzzel[blankposition[0]][blankposition[1]-1]
        return puzzel
    if action == "right" : 
        puzzel[blankposition[0]][blankposition[1]+1] , puzzel[blankposition[0]][blankposition[1]] = puzzel[blankposition[0]][blankposition[1]] , puzzel[blankposition[0]][blankposition[1]+1]
        return puzzel


def GameNPuzzel(puzzel,goal,previousaction,Counterd,limit) :
    if puzzel == goal : 
        return 1
    if Counterd == limit : 
        return 0
    blankposition = (0,0)
    for i in range(4):
        for j in range(4):
            if puzzel[i][j] == 0 :
                blankposition = (i , j)

    IsDown = False
    IsUp = False
    IsRight = False
    IsLeft = False
    if blankposition[0] > 0 : 
        IsUp = True
    if blankposition[0] < 3 :
        IsDown = True
    if blankposition[1] > 0 : 
        IsLeft = True
    if blankposition[1] < 3 :
        IsRight = True

    puzzel1 = copy.deepcopy(puzzel)
    puzzel2 = copy.deepcopy(puzzel)
    puzzel3 = copy.deepcopy(puzzel)
    puzzel4 = copy.deepcopy(puzzel)

    if previousaction == "up" : 
        IsDown = False
    if previousaction == "down" :
        IsUp = False
    if previousaction == "left" : 
        IsRight = False
    if previousaction == "right" : 
        IsLeft = False

    if IsUp : 
        puzzel1 = ActionPuzzel(copy.deepcopy(puzzel),"up",blankposition)
        res = GameNPuzzel(puzzel1,goal,"up",Counterd + 1,limit)
        if res == 1 : 
            print(f'{puzzel1} , PrevAction : up')
            return 1
        else : 
            print(f'puzzel : {puzzel1} , prevAction : up')
    if IsDown : 
        puzzel2 = ActionPuzzel(copy.deepcopy(puzzel),"down",blankposition)
        res = GameNPuzzel(puzzel2,goal,"down",Counterd + 1,limit)
        if res == 1 : 
            print(f'{puzzel2} , PrevAction : down')
            return 1
        else : 
            print(f'puzzel : {puzzel2} , prevAction : down')
    if IsLeft : 
        puzzel3 = ActionPuzzel(copy.deepcopy(puzzel),"left",blankposition)
        res = GameNPuzzel(puzzel3,goal,"left",Counterd + 1,limit)
        if res == 1 : 
            print(f'{puzzel3} , PrevAction : left')
            return 1
        else : 
            print(f'puzzel : {puzzel3} , prevAction : left')
    if IsRight : 
        puzzel4 = ActionPuzzel(copy.deepcopy(puzzel),"right",blankposition)
        res = GameNPuzzel(puzzel4,goal,"right",Counterd + 1,limit)
        if res == 1 : 
            print(f'{puzzel4} , PrevAction : right')
            return 1
        else : 
            print(f'puzzel : {puzzel4} , prevAction : right')


GameNPuzzel([[5,1,2,4],[6,0,3,8],[9,11,7,12],[13,10,14,15]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]] , " ",0 , 10)
