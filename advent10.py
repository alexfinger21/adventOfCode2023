from time import sleep

South = {'L': 1, 'J': -1, '|': 0}
North = {'F': 1, '7': -1, '|': 0}
East = {'J': -1, '7': 1, '-': 0}
West = {'F': 1, 'L': -1, '-': 0}
#right is 1, left is -1, straight is 0
#down is 1, up is -1
with open("input10.txt", "r") as file:
    data = file.readlines()
    sLocation = {}
    laLoop = []

    for i, g in enumerate(data):
        if data[i][-1] == "\n":
            print("shalom?")
            data[i] = data[i][:-1]
        if data[i].find("S") != -1:
            sLocation[i] = data[i].find("S")
    
    index = list((sLocation.keys()))[0]
    i = index#row
    j = sLocation[index]#col
    prevI = i
    prevJ = j
    i -= 1

    def doDeed():
        global laLoop

        path1 = []
        path2 = []

        i = index#row
        j = sLocation[index]#col
        steps = 0

        for k in range(len(laLoop) - 1, -1, -1):
            steps += abs(i - laLoop[k][0]) + abs(j - laLoop[k][1])
            path1 = [steps] + path1
            i = laLoop[k][0]
            j = laLoop[k][1]

        i = index#row
        j = sLocation[index]#col
        steps = 0

        for k in range(len(laLoop)):
            steps += abs(i - laLoop[k][0]) + abs(j - laLoop[k][1])
            path2.append(steps)
            i = laLoop[k][0]
            j = laLoop[k][1]

        print(path1)
        print(path2)

        return max(min(path1[i], path2[i]) for i in range(len(laLoop)))


    def traverse():
        global index, sLocation, i, j, data, prevI, prevJ, laLoop
        isValid = True

        while isValid:
            print(data[i][j])
            #print(prevI, prevJ)
            #print(i, j)
            #print(laLoop)
            if prevI - i == 1 and [i, j] not in laLoop: #North
                print("north tis")
                prevI = i
                prevJ = j
                if data[i][j] in North:
                    if North[data[i][j]] == 0:
                        i-=1
                        laLoop.append([prevI, prevJ])
                    else:
                        #print(i, j)
                        #print(i, j+North[data[i][j]])
                        j += North[data[i][j]]
                        laLoop.append([prevI, prevJ])
                else:
                    if (data[i][j] != "S"):
                        laLoop = []
                    isValid = False

            elif prevI - i == -1 and [i, j] not in laLoop: #South
                print("south tis")
                prevI = i
                prevJ = j
                if data[i][j] in South:
                    if South[data[i][j]] == 0:
                        i+=1
                        laLoop.append([prevI, prevJ])
                    else:
                        j += South[data[i][j]]
                        laLoop.append([prevI, prevJ])
                else:
                    if (data[i][j] != "S"):
                        laLoop = []
                    isValid = False
            elif prevJ - j == 1 and [i, j] not in laLoop: #West
                print("west tis")
                prevI = i
                prevJ = j
                if data[i][j] in West:
                    if West[data[i][j]] == 0:
                        j-=1
                        laLoop.append([prevI, prevJ])
                    else:
                        i += West[data[i][j]]
                        laLoop.append([prevI, prevJ])
                else:
                    if (data[i][j] != "S"):
                        laLoop = []
                    isValid = False
            elif prevJ - j == -1 and [i, j] not in laLoop: #East
                print("east tis")
                prevI = i
                prevJ = j
                if data[i][j] in East:
                    if East[data[i][j]] == 0:
                        j+=1
                        laLoop.append([prevI, prevJ])
                    else:
                        i += East[data[i][j]]
                        laLoop.append([prevI, prevJ])
                else:
                    if (data[i][j] != "S"):
                        laLoop = []
                    isValid = False
            else:
                print("ye")
                #print(i, j)
                #print(data[i][j])
                #print(data[i][j])
                #print(i, j)
                isValid = False
                laLoop = []
        #print(i, j)
        #print(data[i][j])

    traverse()
    print(laLoop)

    if len(laLoop) > 0:
        sumy = doDeed()
        print(sumy)

    i = index#row
    j = sLocation[index]#col
    prevI = i
    prevJ = j
    i += 1
    traverse()
    print(laLoop)

    if len(laLoop) > 0:
        sumy = doDeed()
        print(sumy)

   