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


def GameNPuzzel(puzzel,goal,previousaction) : 
    Queue = [[puzzel,previousaction]]
    Graph = defaultdict(list)
    Counterd = 0
    while True : 
        if Queue : 
            puzzel , previousaction = Queue.pop(0)
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
                
            if IsDown : 
                puzzel2 = ActionPuzzel(copy.deepcopy(puzzel),"down",blankposition)
                
            if IsLeft : 
                puzzel3 = ActionPuzzel(copy.deepcopy(puzzel),"left",blankposition)
                
            if IsRight : 
                puzzel4 = ActionPuzzel(copy.deepcopy(puzzel),"right",blankposition)
                
            Counterd += 1
            if IsUp : 
                if puzzel1 == goal : 
                    print("up")
                    print(f'find goal : {puzzel1} Action : up')
                    print(f'puzzel : {puzzel} , action : {previousaction}')
                    while previousaction != " " : 
                        for puzzel , previousaction in Graph[str(puzzel) + str(Counterd - 1)] :
                            print(f'puzzel : {puzzel} , action : {previousaction}')
                        Counterd -= 1
                    break
                else : 
                    print("up")
                    print(puzzel1)
                    Queue.append([puzzel1 , "up"])
                    Graph[str(puzzel1) + str(Counterd)].append([puzzel,previousaction])
            if IsDown : 
                if puzzel2 == goal : 
                    print("down")
                    print(f'find goal : {puzzel2} action : down')
                    print(f'puzzel : {puzzel} , action : {previousaction}')
                    while previousaction != " " : 
                        for puzzel , previousaction in Graph[str(puzzel) + str(Counterd - 1)] :
                            print(f'puzzel : {puzzel} , action : {previousaction}')
                        Counterd -= 1
                    break
                else : 
                    print("down")
                    print(puzzel2)
                    Queue.append([puzzel2,"down"])
                    Graph[str(puzzel2) + str(Counterd)].append([puzzel,previousaction])
            if IsLeft : 
                if puzzel3 == goal :
                    print("left")
                    print(f'find goal : {puzzel3} , action : left')
                    print(f'puzzel : {puzzel} , action : {previousaction}')
                    while previousaction != " " : 
                        for puzzel , previousaction in Graph[str(puzzel) + str(Counterd - 1)] :
                            print(f'puzzel : {puzzel} , action : {previousaction}')
                        Counterd -= 1
                    break
                else : 
                    print("left")                    
                    print(puzzel3)
                    Queue.append([puzzel3,"left"])
                    Graph[str(puzzel3) + str(Counterd)].append([puzzel,previousaction])
            if IsRight : 
                if puzzel4 == goal :
                    print("right")
                    #return puzzel4
                    print(f'find goal : {puzzel4} action : right')
                    print(f'puzzel : {puzzel} , action : {previousaction}')
                    while previousaction != " " : 
                        for puzzel , previousaction in Graph[str(puzzel) + str(Counterd - 1)] :
                            print(f'puzzel : {puzzel} , action : {previousaction}')
                        Counterd -= 1
                    break
                else : 
                    print("right")
                    print(puzzel4)
                    Queue.append([puzzel4,"right"])
                    Graph[str(puzzel4) + str(Counterd)].append([puzzel,previousaction])

    


GameNPuzzel([[5,1,2,4],[6,0,3,8],[9,11,7,12],[13,10,14,15]],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]], " ")
    