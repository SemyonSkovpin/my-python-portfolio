import random


class Cannon:
    def __init__(self, model, DMG, price):
        '''
        Make a cannon object with these attributes:
        :model: str 
        :DMG: int or float
        :price: int or float
        '''
        self.model = model
        self.DMG = DMG
        self.price = price

    def getModel(self):
        return self.model
    
    def getDMG(self):
        return self.DMG
    
    def getPrice(self):
        return self.price
    

def MakeCannonObjectsList (models, DMG, prices):
    '''
    Turn three list with info about cannons into a list of cannon objects

    :models: list with str names of cannons
    :DMG: list with int ot float damage scores
    :prices: list with str or float prices
    '''
    cannons = []
    for i in range(len(models)):
        cannons.append(Cannon(models[i], DMG[i], prices[i]))
    return cannons


def printCannons(cannons):
    """
    Take each cannon object from cannons list and print all info about it
    :cannons: list with cannon objects
    """
    for cannon in cannons:
        print (f'Cannon: {cannon.getModel()}\nDamage: {cannon.getDMG()}\nPrice: {cannon.getPrice()}\n')
    


dynamicFuncCount = 0
def getBestSubsetDynamic(availItems, availWeight, records={}):
    global dynamicFuncCount
    dynamicFuncCount += 1
    '''
    getBesSubset but using dynamic programming
    '''
    if (len(availItems), availWeight) in records:
        result = records[(len(availItems), availWeight)]
    else:
        if availItems == [] or availWeight == 0:
            result = (0, ())
        elif availItems[0].getPrice() > availWeight:
            result = getBestSubsetDynamic(availItems[1:], availWeight, records)
        else:
            valWith, subsetWith = getBestSubsetDynamic(availItems[1:], availWeight - availItems[0].getPrice(), records)
            valWith, subsetWith = valWith + availItems[0].getDMG(), subsetWith + (availItems[0],)

            valWithout, subsetWithout = getBestSubsetDynamic(availItems[1:], availWeight, records)

            if valWith > valWithout:
                result = (valWith, subsetWith)
            else: 
                result = (valWithout, subsetWithout)

    records[(len(availItems), availWeight)] = result
    return result


normalFuncCount = 0
def getBestSubset(availItems, availWeight):
    global normalFuncCount 
    normalFuncCount += 1
    '''
    Knapsack problem where you have set of items (each has value and weight) and avaliable weight.  Find 
    Two problems 
    '''
    if availItems == [] or availWeight == 0:
        result = (0, ())
    elif availItems[0].getPrice() > availWeight:
        result = getBestSubset(availItems[1:], availWeight)
    else:
        valWith, subsetWith = getBestSubset(availItems[1:], availWeight - availItems[0].getPrice())
        valWith, subsetWith = valWith + availItems[0].getDMG(), subsetWith + (availItems[0],)

        valWithout, subsetWithout = getBestSubset(availItems[1:], availWeight)

        if valWith > valWithout:
            result = (valWith, subsetWith)
        else: 
            result = (valWithout, subsetWithout)
        
    return result
    

n = 700
models = [i for i in range(n)]   
dmg = [random.randint(1, 10) * (i+1) for i in range(n)]
prices = [random.randint(1,10) * (i+1) for i in range(n)]


myCannons = MakeCannonObjectsList(models, dmg, prices)

solution = getBestSubset(myCannons, 9000)
solutionDynamic = getBestSubsetDynamic(myCannons, 9000)

printCannons (solution[1])
print(solution[0], normalFuncCount, '\n', dynamicFuncCount)





    

