def runoff(voters):
    voters_amount = len (voters)
    while True:
        dist = {}
        for c in voters[0]:
            dist[c] = 0
        for voter in voters:
            dist[voter[0]] += 1
        lead = max (dist.values())
        if lead > voters_amount // 2:
            return list(dist.keys())[list(dist.values()).index(lead)]
        least = min (dist.values())
        for voter in voters:
            twin = voter[:]
            for c in twin:
                try:
                    if dist[c] == least:
                        voter.remove(c)
                except:
                    continue
        if voters[0] == []:
            return None