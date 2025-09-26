import random

def generate_minesweeper_grid(rows, cols, num_mines):
    # Step 1: Initialize grid with zeros
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Step 2: Randomly place mines (value 9)
    mine_positions = set()
    while len(mine_positions) < num_mines:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if (r, c) not in mine_positions:
            mine_positions.add((r, c))
            grid[r][c] = 9

    # Step 3: Update adjacent counts
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for r, c in mine_positions:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 9:
                grid[nr][nc] += 1

    return grid

def reveal(grid, revealed, r, c):
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return
    if revealed[r][c]:
        return

    revealed[r][c] = True
    if grid[r][c] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    reveal(grid, revealed, r + dr, c + dc)


rows, cols, num_mines = 7, 5, 2
grid = generate_minesweeper_grid(rows, cols, num_mines)
revealed = [[False for _ in range(cols)] for _ in range(rows)]

# Simulate a click at (0, 4)
reveal(grid, revealed, 0, 4)

# Print revealed grid
for r in range(rows):
    print(' '.join(str(grid[r][c]) if revealed[r][c] else '-' for c in range(cols)))
