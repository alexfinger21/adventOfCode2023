import re

with open("input4.txt") as file:
    sumy = 0
    data = file.readlines()
    def doCard(j):
        global sumy
        card = data[j]
        cardNum = [int(x.group()) for x in re.finditer(r"\d+", card)][0]
        card = card[card.index(":")+1:].split(" | ")
        winning = [int(x.group()) for x in re.finditer(r"\d+", card[0])]
        urs = [int(x.group()) for x in re.finditer(r"\d+", card[1])]
        count = 0
        for cardy in urs:
            #print(cardy)
            if cardy in winning:
                count += 1
        sumy += 1
        for i in range(cardNum+1, cardNum+count+1):
            doCard(i-1)
    for i, thing in enumerate(data):
        if thing[-1] == "\n":
            data[i] = thing[:-1]
    for i, card in enumerate(data):
        doCard(i)
    print(sumy)