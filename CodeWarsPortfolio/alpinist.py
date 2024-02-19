def path_finder (maze_str):
    def one_step_to (cell, open):
        remaining, node = cell
        x, y = node
        if remaining == 0:
            if node == goal:
                return True 
            opened.add (node)
            for child_x, child_y in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if 0 <= child_x < len (maze_arr) and 0 <= child_y < len (maze_arr [0]) and (child_x, child_y) not in opened:
                    child = [abs (int (maze_arr [x][y]) - int (maze_arr [child_x][child_y])), (child_x, child_y)]                   
                    open += [child]
                    success = one_step_to (child, open)
                    if success:
                        return True
            open.remove (cell)
            return False
        cell [0] -= common_distance
        return False

    
    
    maze_arr = list (map (list, maze_str.splitlines ()))
    goal = (len (maze_arr) - 1, len (maze_arr [0]) - 1)
    start = (0, 0)
    open = []
    open += [[0, (0, 0)]]
    opened = set ()
    opened.add (start)
    cost = 0
    while True:
        common_distance = min (open) [0]
        for cell in open [:]:
            success = one_step_to (cell, open)                  
            if success:
                return cost
        
        cost += common_distance


        pass