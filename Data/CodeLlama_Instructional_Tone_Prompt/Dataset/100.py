def make_a_pile(n):
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(stones[-1] + 2)
        else:
            stones.append(stones[-1] + 1)
    return stones
