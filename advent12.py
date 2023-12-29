def strToArr(string):
    return [x for x in string]

def getAdjacentChars(x, arr, char, withQuestion):
    count = []
    ind = x
    
    while (ind >= 0 and (arr[ind] == char or (arr[ind] == "?" and withQuestion))):
        count.append(ind)
        ind -= 1
        
    ind = x
    while (ind != len(arr) and (arr[ind] == char or (arr[ind] == "?" and withQuestion))):
        count.append(ind)
        ind += 1

    return count

def getFirstAdjacentChars(x, arr, char):
    count = []
    x = arr.find(char, x)
    while (x < len(arr) and arr[x] == char):
        count.append(x)
        x+=1

    return count

with open("input12.txt") as file:
    data = file.readlines()
    sumy = 0

    for thing in data: 
        combs = set()
        thing = thing.split(" ")
        notFilled = strToArr(thing[0])
        dmgSprings = (int(x) for x in thing[1].split(","))

        lastInd = [[]*len(dmgSprings)]
        tags = getFirstAdjacentChars(lastInd, notFilled, "#")
        questions = getFirstAdjacentChars(lastInd, notFilled, "?")

        if len(tags) < dmgSprings[0] and len(questions) < dmgSprings[0]:
            if questions[-1] + 1 == tags[0]: #questions right behind, can also be in front
                if len(tags) == 0: #no tags at all
                    lastInd[0].extend([i for i in range(dmgSprings[0] + 1, len(notFilled))])
                else:
                    #finish later
            elif questions[0] -1 == tags[-1]: #questions right in front

            else: #questions disconnected... must be in front

        for i in range(len(dmgSprings)):
            


