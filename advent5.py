import re
import sys

def clamp(x, num1, num2):
    return min(num2, max(num1, x))

def inRange(arr1, arr2):
        if (arr1[0] <= arr2[0]):
            return [arr2[0], clamp(arr1[0] + arr1[1] - arr2[0] - 1, 0, arr2[1])]
        else:
            return [arr1[0], clamp(arr2[0] + arr2[1] - arr1[0] - 1, 0, arr1[1])]
        
def notInRange(arr1, arr2):
    if (arr1[0] <= arr2[0] and arr1[0]+arr1[1] < arr2[0] + arr2[1]):
            return [arr1[0], clamp(arr1[0] + arr1[1] - (arr1[0] + arr1[1] - arr2[0] - 1), 0, arr2[0]-arr1[0])]
    elif (arr1[0] <= arr2[0] and arr1[0]+arr1[1] >= arr2[0] + arr2[1]):
        return [0, [arr1[0], clamp(arr1[0] + arr1[1] - arr2[0] - 1, 0, arr2[0]-arr1[0])], [arr1[0]+arr1[1], clamp(arr1[0]+arr1[1] - arr2[0] - arr2[1], 0, float('inf'))]]
    elif arr1[0] >= arr2[0] and arr1[0] < arr2[0] + arr2[1]:
        return [arr2[0] + arr2[1], clamp(arr1[0] + arr1[1] - arr2[1] - arr2[0], 0, arr2[0] + arr2[1] - arr1[1])]
    else:
        return False
    
print(inRange([16, 5], [11, 10]))
print(notInRange([9, 2], [11, 10]))

with open("input5.txt") as file:
    data = file.readlines()
    for i, thing in enumerate(data):
        numbas = [int(x.group()) for x in re.finditer(r"\d+", thing)]

        if len(numbas) == 0:
            data[i] = "s"
        else:
            data[i] = numbas

    seeds = []

    for i in range(0, len(data[0]) - 1,2):
        seeds.append([data[0][i], data[0][i+1]])

    print(seeds)

    data[0] = seeds

    changed = {False}

    for i in range(1, len(data)):
        if data[i] == "s":
            changed = [[float("inf"), float("inf")]]
            continue
        destination = data[i][0]
        source = data[i][1]
        rangey = data[i][2]

        for d, dd in enumerate(data[0]):
            print(data[0])
            rangething = inRange(dd, [source, rangey])
            notrangething = notInRange(dd, [source, rangey])
            if rangething[1] > 0 and len([word for word in changed if word[0] == rangething[0] and word[1] == rangething[1]]) == 0:
                #print(rangething)
                rangething[0] = destination
                data[0][d] = rangething
                changed.append(rangething)

            if notrangething and len(notrangething) == 2 and notrangething[1] > 0 and len([word for word in changed if word[0] == notrangething[0] and word[1] == notrangething[1]]) == 0:
                data[0].append(notrangething)
            elif notrangething and len(notrangething) == 3:
                for x in notrangething:
                    if x != 0 and x[1] > 0 and len([word for word in changed if word[0] == x[0] and word[1] == x[1]]) == 0:
                        data[0].append(x)

            


    print(min([x[0] for x in data[0]]))