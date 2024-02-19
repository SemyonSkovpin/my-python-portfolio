def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.am
    """
    n = len(items)
    # Each of the combinations is represented by a number from 0 to 3^n
    print(n)
    for i in range(3**n):
        combo = ([],[])
        # Go through each item and check what is its place in this combination
        for k in range(n):
            # 'convert' i into trinary number and extract its digit corresponding to the j-th item
            itemState = (i // 3**k) % 3
            if itemState == 1:
                combo[0].append(items[k])
            elif itemState == 2:
                combo[1].append(items[k])
        yield combo


allCombos = yieldAllCombos(['a','b'])
while True:
    print(next(allCombos))
    input()


