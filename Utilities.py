import numpy as np

def getMines(quantity, max_x, max_y):
    if quantity > max_x * max_y:
        return []
    
    max_index = max_x * max_y
    rng = np.random.default_rng()
    
    numbers = rng.integers(low=0, high=max_index, size=quantity*2)

    existent = set()
    uniques = [n for n in numbers if n not in existent and not (existent.add(n) or False)]
    uniques = uniques[:quantity]

    return list(map(lambda c: [c % max_x, c // max_x], uniques))


def getNeighbors(coords, max_x, max_y):
    res = []

    if coords[1] > 0:
        res.append([coords[0], coords[1] - 1])
    if coords[1] < max_y - 1:
        res.append([coords[0], coords[1] + 1])

    if coords[0] > 0:
        res.append([coords[0] - 1, coords[1]])
        if coords[1] > 0:
            res.append([coords[0] - 1, coords[1] - 1])
        if coords[1] < max_y - 1:
            res.append([coords[0] - 1, coords[1] + 1])

    if coords[0] < max_x - 1:
        res.append([coords[0] + 1, coords[1]])
        if coords[1] > 0:
            res.append([coords[0] + 1, coords[1] - 1])
        if coords[1] < max_y - 1:
            res.append([coords[0] + 1, coords[1] + 1])

    return res