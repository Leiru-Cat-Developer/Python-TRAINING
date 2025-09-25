from collections import deque

def silentHill(room):
    n = len(room)
    m = len(room[0])
    print(f"MATRIX SIZE: {n} , {m}")
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Define up, down, left, right
    start = target = None # Start undefined
    print(f"INIT PYRAMID: {start}, INIT TARGET: {target}")

    # Search for init position for 🔺 and "T"
    for i in range(n):
        for j in range(m):
            if room[i][j] == '🔺':
                start = (i, j) # Tuple
            elif room[i][j] == 'T':
                target = (i, j) # Tuple

    print(f"PYRAMID: {start}, TARGET: {target}")

    if not start or not target:
        raise ValueError("\nMatrix should content 🔺 and 'T' . . .")

    # BFS from 🔺 to T
    dq = deque([(start[0], start[1], 0)])  # (row, column, steps) = [(0,1,0)]
    visited = set() # set()
    visited.add(start) # {(0,1)}

    print(f"DEQUE: {dq}, VISITED SET: {visited}")

    while dq:
        print(f"DEQUE BEFORE POP: {dq}")
        x, y, steps = dq.popleft()
        print(f"X: {x}, Y: {y}, Steps: {steps} | DEQUE AFTER POP: {dq}")
        
        if (x, y) == target:
            return steps

        for dx, dy in directions:
            print(f"DX: {dx}, DY: {dy}")
            nx, ny = x + dx, y + dy
            print(f"NX: {nx}, NY: {ny}")
            if (0 <= nx < n 
                and 0 <= ny < m
                and room[nx][ny] in ['.', 'T']
                and (nx, ny) not in visited):
                print(f"VISITED BEFORE: {visited}")
                visited.add((nx, ny))
                print(f"VISITED AFTER: {visited}")
                print(f"DEQUE BEFORE: {dq}")
                dq.append((nx, ny, steps + 1))
                print(f"DEQUE AFTER: {dq}")
                print(f"CHARACTER IN POSITION: {room[nx][ny]}")
    return -1

room = [
    ['.', '🔺', '.', '.', '.'],
    ['#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#'],
    ['#', '#', '#', '.', '#'],
    ['#', '#', '#', '.', '#'],
    ['T', '.', '.', '.', '#']
]

print(f"\nRESULT -> {silentHill(room)}")