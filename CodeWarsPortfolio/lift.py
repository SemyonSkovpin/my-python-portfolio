class Dinglemouse (object):
    def __init__(self, queues, capacity):
        self.queues = [list(floor) for floor in queues]
        self.capacity = capacity
        
    
    def sameDirection (self, floorPerson, floorInd, goingUp):
        return(floorPerson - floorInd > 0 and goingUp) or (floorPerson - floorInd < 0 and not goingUp)
                

    def theLift (self):
        queues = self.queues
        capacity = self.capacity
        currentFloor = 0
        goingUp = True
        visited = []
        onboard = []
        
        while True:
            # On arrival, add current floor to visited, but only if it wasn't added in previous iteration (i.e. if lift didn't change direction without changing floor)
            if len(visited) > 0:
                if visited[-1] != currentFloor:
                    visited.append(currentFloor)
            else:
                visited.append(currentFloor)

            # Drop arrived passangers
            while currentFloor in onboard:
                onboard.remove(currentFloor)

            # Fill lift with relevant passangers from floor
            for floorPerson in queues[currentFloor][:]:
                if len(onboard) == capacity:
                    break

                if self.sameDirection(floorPerson, currentFloor, goingUp):
                    onboard.append(floorPerson)
                    queues[currentFloor].remove(floorPerson)

            # Check if work is done you should stop adding visited floors and break from loop
            isEmpty = all(map(lambda x: [] == x, queues))
            if not onboard and isEmpty:
                if len(visited) > 0: 
                    if visited[-1] != 0:
                        visited.append(0)
                else:
                    visited.append(0)
                break

            
            # Find some floors in your direction you could visit to choose from later
            potentialFloors = onboard[:]

            if goingUp:
                path = range(currentFloor + 1, len(queues))
            else:
                path = range(currentFloor - 1, -1, -1)
            
            breakLoop = False
            for floorInd in path:
                for floorPerson in queues[floorInd]:
                    if self.sameDirection(floorPerson, floorInd, goingUp):
                        potentialFloors.append(floorInd)
                        breakLoop = True
                    if breakLoop: break
                if breakLoop: break

            # Change direction if there's nowhere to go in your current direction
            if not potentialFloors:
                goingUp = not goingUp
                if goingUp:
                    path = range(len(queues))
                else:
                    path = range(len(queues)-1,-1,-1)

                breakLoop = False
                for floorInd in path:
                    for floorPerson in queues[floorInd]:
                        if self.sameDirection(floorPerson, floorInd, goingUp):
                            currentFloor = floorInd
                            breakLoop = True
                        if breakLoop: break
                    if breakLoop: break
            
            # Set as current floor that one wich is nearest in your direction and has passanger going in same direction
            else:
                if goingUp:
                    currentFloor = min(potentialFloors)
                else:
                    currentFloor = max(potentialFloors)
        
        return visited
    

    