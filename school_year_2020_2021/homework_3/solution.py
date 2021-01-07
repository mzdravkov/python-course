def neighbours_alive_count(grid, row, col):
    """ Takes a grid and a position and returns
    the number of living neighbour cells."""
    rows = range(max(0, row - 1), min(len(grid) - 1, row + 1) + 1)
    cols = range(max(0, col - 1), min(len(grid[0]) - 1, col + 1) + 1)
    return len([1 for x in cols for y in rows
        if grid[y][x] == 1 and (x, y) != (col, row)])

def next_cell_state(grid, row, col):
    cell = grid[row][col]
    living_neighbours = neighbours_alive_count(grid, row, col)
    if cell == 1 and living_neighbours in {2, 3}:
        return 1
    elif cell == 0 and living_neighbours == 3:
        return 1
    return 0

def next_generation(grid):
    return [[next_cell_state(grid, row, col) for col in range(len(grid[0]))]
            for row in range(len(grid))]
