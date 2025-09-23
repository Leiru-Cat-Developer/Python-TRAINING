from collections import deque

def silentHill(room):
    n = len(room)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Define up, down, left, right
    start = target = None # Start undefined

    # Search for init position for 🔺 and "T"
    for i in range(n):
        for j in range(n):
            if room[i][j] == '🔺':
                start = (i, j) # Tuple
            elif room[i][j] == 'T':
                target = (i, j) # Tuple

    if not start or not target:
        raise ValueError("\nMatrix should content 🔺 and 'T' . . .")

    # BFS from 🔺 to T
    queue = deque([(start[0], start[1], 0)])  # (row, column, steps) = [(0,1,0)]
    visited = set() # set()
    visited.add(start) # {(0,1)}

    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == target:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n 
                and 0 <= ny < n 
                and room[nx][ny] in ['.', 'T'] 
                and (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1

room = [
    ['.', '🔺', '.', '.', '.'],
    ['#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#'],
    ['T', '.', '.', '.', '#']
]

print(f"\nRESULT -> {silentHill(room)}")