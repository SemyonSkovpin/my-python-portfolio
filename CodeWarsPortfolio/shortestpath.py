def path_finder(maze):
    maze = list (map(list,maze.splitlines()))
    stack = [[(0,0)]]
    while True:        
        stack += [ [] ]
        for x,y in stack[-2]:
            con1 = x in range(len(maze))
            con2 = y in range(len(maze[0]))
            if con1 and con2:
                if maze[x][y] == ".":
                    if (x,y) == (len(maze)-1,len(maze[0])-1):
                        return len (stack) - 2
                    maze [x][y] = "x"
                    stack [-1] += [(x+1,y), (x,y+1), (x-1, y), (x, y-1)]            
        if stack [-1] == []:
                    return False  