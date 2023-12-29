import re

red = 12
green = 13
blue = 14

with open("input2.txt") as file:
    sum = 0
    rowlist = file.readlines()
    for data in rowlist:
        columnind = data.index(":")
        id = int(data[5:columnind])
        data = data[columnind+1:]
        games = data.split("; ")
        minRed = 0
        minGreen = 0
        minBlue = 0
        for game in games:
            cubes = game.split(", ")
            for cube in cubes:
                if (cube.find("red") != -1):
                    if (int(re.findall(r"\d+", cube)[0])) > minRed:
                        minRed = int(re.findall(r"\d+", cube)[0])
                if (cube.find("green")!= -1):
                    if (int(re.findall(r"\d+", cube)[0])) > minGreen:
                        minGreen = int(re.findall(r"\d+", cube)[0])
                if (cube.find("blue")!= -1):
                    if (int(re.findall(r"\d+", cube)[0]) > minBlue):
                        minBlue = int(re.findall(r"\d+", cube)[0])
        sum += minRed*minBlue*minGreen
    print(sum)
