import re
numList = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("input1-test.txt") as file:
    sum = 0
    data = file.readlines()
    for x in data:
        indicesNum = []
        for num in numList:
            appendThing = [[m.start(), numList.index(num)+1] for m in re.finditer(num, x)]
            if len(appendThing) > 0:
                indicesNum.extend(appendThing)
                
        for i in range(10):
            appendThing = [[m.start(), i] for m in re.finditer(str(i), x)]
            if len(appendThing) > 0:
                indicesNum.extend(appendThing)
        if len(indicesNum) > 0:

            minInd = min([ind[0] for ind in indicesNum])
            maxInd = max([ind[0] for ind in indicesNum])
            miny = str([numba[1] for numba in indicesNum if numba[0] == minInd][0])
            maxy = str([numba[1] for numba in indicesNum if numba[0] == maxInd][0])

            sum += int(miny + maxy)
        

    print(sum)
