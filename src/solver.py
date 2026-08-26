#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    alive_count = 0 # i indicates ith row and j indicates jth column
    # TODO: Implement your neighbor-counting logic here!
    # Check all 8 surrounding neighbors
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue  # Skip the cell itself
            neighbor_row = (row + i) % rows # Ensures nothing is out of bounds
            neighbor_col = (col + j) % cols         
            if grid[neighbor_row][neighbor_col] == 1:
                alive_count += 1
                    
    return alive_count

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    Args:
        grid (list of lists): The current 2D state of the game.
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    nb = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)] # Creates a new blank grid of the same size, filled with 0s (dead cells)
    # TODO: Iterate through every cell in the `grid`.
    for i in range(rows):
        for j in range(cols):
            nb = count_neighbors(grid, i, j)
            # TODO: Apply the 4 Rules of Life to determine if it should be 1 (alive) or 0 (dead) in `next_grid`.
            if grid[i][j] == 1:
                if nb == 2 or nb == 3:
                    next_grid[i][j] += 1
                else:
                    next_grid[i][j] = 0
            else:
                if nb == 3:
                    next_grid[i][j] += 1
    return next_grid