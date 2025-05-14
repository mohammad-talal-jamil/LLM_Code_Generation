def min_path(grid, k):
    """
    Find the minimum path of length k in the grid.

    Parameters
    ----------
    grid : list of list of int
        The grid with values.
    k : int
        The length of the path to find.

    Returns
    -------
    list of int
        The ordered list of values on the cells that the minimum path goes through.
    """
    # Initialize the starting cell
    start_cell = (0, 0)

    # Initialize the queue with the starting cell
    queue = [start_cell]

    # Initialize the visited set
    visited = set()

    # Loop until the queue is empty or the path length is reached
    while queue and len(queue) < k:
        # Get the current cell from the queue
        current_cell = queue.pop(0)

        # If the current cell has not been visited, mark it as visited and add its neighbors to the queue
        if current_cell not in visited:
            visited.add(current_cell)
            queue.extend([(current_cell[0] + 1, current_cell[1]), (current_cell[0] - 1, current_cell[1]),
                          (current_cell[0], current_cell[1] + 1), (current_cell[0], current_cell[1] - 1)])

    # Return the ordered list of values on the cells that the minimum path goes through
    return [grid[cell[0]][cell[1]] for cell in queue]