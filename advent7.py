from functools import cmp_to_key

vals = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

#248782561
#249415701
#249666369
def mightySort(item1, item2):

    cardCount1 = {}
    cardCount2 = {}

    for c in item1[0]:
        if not cardCount1.get(c):
            cardCount1[c] = 1
        else:
            cardCount1[c] += 1
    
    for c in item2[0]:
        if not cardCount2.get(c):
            cardCount2[c] = 1
        else:
            cardCount2[c] += 1

    #print(cardCount1)

    cardCount1 = sorted(list(cardCount1.values()), reverse=True)
    cardCount2 = sorted(list(cardCount2.values()), reverse=True)

    for i in range(len(cardCount1)):
        if cardCount2[i] and cardCount1[i] > cardCount2[i]:
            return -1
        elif cardCount2[i] and cardCount1[i] < cardCount2[i]:
            return 1
        elif not cardCount2[i]:
            return -1
        
    og1 = item1[0]
    og2 = item2[0]

    for i in range(5):
        if item1[2][i] == 1:
            item1[0] = item1[0][:i] + 'J' + item1[0][i+1:]
    for i in range(5):
        if item2[2][i] == 1:
            item2[0] = item2[0][:i] + 'J' + item2[0][i+1:]
    for i in range(len(item1[0])):
        if vals.index(item1[0][i]) < vals.index(item2[0][i]):
            item1[0] = og1
            item2[0] = og2
            return -1
        elif vals.index(item1[0][i]) > vals.index(item2[0][i]):
            item1[0] = og1
            item2[0] = og2
            return 1
        
    item1[0] = og1
    item2[0] = og2
    return 0

with open("input7.txt") as file:
    data = file.readlines()

    sum = 0
    
    for i, thing in enumerate(data):
        if thing[-1] == '\n':
            data[i] = thing[:-1]
        data[i] = data[i].split(" ")

    cards = [x[0] for x in data]
    bids = [int(x[1]) for x in data]

    for i, card in enumerate(cards):
        cardCount = {}
        zeJokers = [0] * 5

        for k, c in enumerate(card):
            if c != 'J':
                if not cardCount.get(c):
                    cardCount[c] = 1
                else:
                    cardCount[c] += 1
            else:
                zeJokers[k] = 1
        
        cardCounty = sorted(list(cardCount.values()), reverse=True)

        if len([thing for thing in zeJokers if thing == 1]) > 0:
            bigBirds = []
            for ind, val in cardCount.items():
                if val == cardCounty[0]:
                    #print(cardCount)
                    #sprint(ind, val)
                    bigBirds.append(ind)
            if len(bigBirds) > 0:
                bigBirds.sort(key=lambda x: vals.index(x))
                for k, kk in enumerate(zeJokers):
                    if kk != 0:
                        cards[i] = cards[i][:k] + bigBirds[0] + cards[i][k+1:]
            else:
                cards[i] = 'AAAAA'
        cards[i] = [cards[i], bids[i], zeJokers]


    sortedCards = sorted(cards, key=cmp_to_key(mightySort))
    print(sortedCards)
    for i, thing in enumerate(sortedCards):
        #print(i)
        sum += sortedCards[i][1] * (len(cards) - i)
    print(sum)