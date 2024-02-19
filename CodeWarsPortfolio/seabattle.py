def validate_battlefield (field):
    # This queue will contain length of all yen registered ships. As the algorithm searches through the field, the lengths will be created if new ship is discovered, and updated if new part of thip is discovered
    queue = []
    # Go through each cell in field
    for x in range (len(field)):
        for y in range (len(field[0])):
            ship = field [x][y]  
            if ship == 0:
                continue      

            # It's important to check whether the current cell is touching top, right or left border
            top = y == 0
            left = x == 0
            right = x == len(field) - 1
            
            # If there's adjustent cells to north-west or north east, the field is not valid. Note, that Y approaches south as it increases, and X approaches east
            north_west = not left and not top and field[x - 1][y - 1] != 0
            north_east = not right and not top and field[x + 1][y - 1] != 0   
            if north_west or north_east:
                return False
                
            # Check if current cell has adjuscent ship part to the west. If so, updaate the queue by increasing one of legths in it. Keep track of new length of ship right inside field array. Replace item in the array, that corresponds to this ship part by the length int. 
            westee = field [x-1][y]
            west = not left and westee != 0
            if west:      
                field[x][y] = westee + 1
                queue.remove (westee)
                queue += [westee + 1]
           
            # Do same with north
            northee = field [x][y-1]
            north = not top and northee != 0
            if north:    
                field[x][y] = northee + 1
                queue.remove (northee)
                queue.append (northee + 1)

            # If this ship part has no  discovered neighbors, then its a new ship. Add it to queue
            if not west and not north:
                queue.append (1)

    # The queue must contain exactly this amount of these numbers for field to be valid
    for l, n in (1, 4), (2, 3), (3, 2), (4,1):
        if queue.count (l) != n:
            return False

    return True