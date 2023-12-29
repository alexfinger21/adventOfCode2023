import re 

with open("input3.txt") as file:
    data = file.readlines()
    digitsArr = {}
    sumgr = 0
    for i, line in enumerate(data):
        if line[-1] == '\n':
            data[i] = line[:-1]
    for i, line in enumerate(data):
        for n in re.finditer(r"\d+", line):
            for c in range(n.start(), n.end()):
                digitsArr[(i, c)] = int(n.group())
    for i, line in enumerate(data): 
        for m in re.finditer(r'\*', line):
            stars = {(r, c) for r in range(i-1, i+2) for c in range(m.start() - 1, m.end() + 1)}
            prevOverlap = []
            prevOverlapNums = []
            for o in stars & digitsArr.keys():
                if o not in prevOverlap:
                    counter = 1
                    prevOverlapNums.append(digitsArr[o])
                    while o[1]+counter < len(data[o[0]]) and data[o[0]][o[1]+counter].isdecimal():
                        prevOverlap.append((o[0], o[1]+counter))
                        counter += 1
                    counter = 1
                    while o[1]-counter > 0 and data[o[0]][o[1]-counter].isdecimal():
                        prevOverlap.append((o[0], o[1]-counter))
                        counter += 1
            if len(prevOverlapNums) == 2:
                print(data[prevOverlap[0][0]][prevOverlap[0][1]])
                sumgr += prevOverlapNums[0] * prevOverlapNums[1]

    print(sumgr)
