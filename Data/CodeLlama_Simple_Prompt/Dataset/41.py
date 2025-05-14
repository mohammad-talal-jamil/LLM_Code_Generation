def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions in a car race scenario.

    Args:
        n (int): The number of cars in each direction.

    Returns:
        int: The number of collisions.
    """
    # Calculate the number of collisions
    collisions = n * (n + 1) // 2

    return collisions
