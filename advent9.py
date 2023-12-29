import re

def mightySum(arg):
    sumy = 0
    lilSum = 0
    bigSum = 0
    for thing in arg:
        if thing.levels[0][-1] < 0:
            lilSum += abs(thing.levels[0][-1])
            for level in thing.levels:
                print(level)
        else:
            bigSum += thing.levels[0][-1]
        sumy += thing.levels[0][-1]
    print(bigSum)
    print(lilSum)
    return sumy

class superNode:
    
    def __init__(self, history):
        self.levels = []
        self.levels.append([int(j) for j in re.findall(r'-?\d+', history)])
    def staircase(self):
        while len([x for x in self.levels[-1] if x != 0]) != 0:
            new_arr = []
            for i in range(0, len(self.levels[-1])-1):
                new_arr.append(self.levels[-1][i+1]-self.levels[-1][i])
            self.levels.append(new_arr)
    def yung_extrapolate(self):
        self.levels[-1] = [0] * 1 + self.levels[-1]
        for i in range(len(self.levels)-2, -1, -1):
            # print(self.levels[i+1][-1], self.levels[i][-1])
            self.levels[i] = [-1*self.levels[i+1][0]+self.levels[i][0]] + self.levels[i]
            
with open("input9.txt") as file:
    data = file.readlines()

    masterNodes = []

    for i, h in enumerate(data):
        mightyNode = superNode(h)
        mightyNode.staircase()
        mightyNode.yung_extrapolate()
        masterNodes.append(mightyNode)
        print(mightyNode.levels)

    # for master in masterNodes:
    #     print(master.levels)
    print(sum(x.levels[0][0] for x in masterNodes))