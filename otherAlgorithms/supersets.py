def getSupersets (mySet):
    n = len(mySet)
    supersets = []
    for i in range(2**n):
        supersets.append([])
        for k in range(n):
            if (i >> k) % 2 == 1:
                supersets[-1].append(mySet[k])
    return supersets

print (getSupersets (['a', 'b', 'c']))