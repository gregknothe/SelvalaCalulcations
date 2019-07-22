import random
import numpy as np

def manaProduction(landCount, deckCount):
    cardNum = random.randint(1,deckCount+1)
    mana = 0
    if cardNum > landCount:
        mana = mana + 1
    else:
        landCount = landCount-1
    deckCount = deckCount - 1
    return landCount, deckCount, mana


def selvalaLoop4(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, startingMana):
    mana = 3 + startingMana
    loopCount = 0
    while mana >= 3:
        mana = mana - 3
        landCount1, deckCount1, mana1 = manaProduction(landCount1, deckCount1)
        landCount2, deckCount2, mana2 = manaProduction(landCount2, deckCount2)
        landCount3, deckCount3, mana3 = manaProduction(landCount3, deckCount3)
        landCount4, deckCount4, mana4 = manaProduction(landCount4, deckCount4)
        mana = mana + mana1 + mana2 + mana3 + mana4
        #print "Mana Count: " + str(mana)
        loopCount = loopCount + 1
        if loopCount > 100:
            return 100
    return loopCount

def selvalaLoop5(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, landCount5, deckCount5, startingMana):
    mana = 3 + startingMana
    loopCount = 0
    while mana >= 3:
        mana = mana - 3
        landCount1, deckCount1, mana1 = manaProduction(landCount1, deckCount1)
        landCount2, deckCount2, mana2 = manaProduction(landCount2, deckCount2)
        landCount3, deckCount3, mana3 = manaProduction(landCount3, deckCount3)
        landCount4, deckCount4, mana4 = manaProduction(landCount4, deckCount4)
        landCount5, deckCount5, mana5 = manaProduction(landCount5, deckCount5)
        mana = mana + mana1 + mana2 + mana3 + mana4 + mana5
        #print "Mana Count: " + str(mana)
        loopCount = loopCount + 1
        if loopCount > 100:
            return 100
    return loopCount


def selvalaLoopAverage4(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, startingMana, numIter):
    results = []
    for x in range(1,numIter+1):
        results.append(selvalaLoop4(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, startingMana))
    return round(np.mean(results),2), round(np.std(results),2)

def selvalaLoopAverage5(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, landCount5, deckCount5, startingMana, numIter):
    results = []
    for x in range(1,numIter+1):
        results.append(selvalaLoop5(landCount1, deckCount1, landCount2, deckCount2, landCount3, deckCount3, landCount4, deckCount4, landCount5, deckCount5, startingMana))
    return round(np.mean(results),2), round(np.std(results),2)

#print selvalaLoopAverage4(39,100,39,100,39,100,39,100,x,100000)

#for x in range(0,11):
#    numbers = selvalaLoopAverage4(32,100,32,100,32,100,32,100,x,100000)
#    print str(numbers[0]) + " (" + str(numbers[1]) + ")"

LC = 40
for x in range(0,11):
    numbers = selvalaLoopAverage5(LC,100,LC,100,LC,100,LC,100,33,100,x,10000)
    print str(numbers[0]) + " (" + str(numbers[1]) + ")"