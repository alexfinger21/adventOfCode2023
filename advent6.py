import re

with open("input6.txt") as file:
    data = file.readlines()
    times = [x.group() for x in re.finditer(r"\d+", data[0])]
    records = [x.group() for x in re.finditer(r"\d+", data[1])]

    newTime = ""

    for i in times:
        newTime += i

    newRecord = ""
    
    for i in records:
        newRecord += i

    newTime = int(newTime)
    newRecord = int(newRecord)

    res = 0

    recordTimes = 0
    for waitTime in range(0, newTime):
        totalMove = (newTime-waitTime) * waitTime
        if totalMove > newRecord:
            recordTimes += 1
    if res != 0:
        res *= recordTimes
    else:
        res = recordTimes

    print(res)

