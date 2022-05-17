import sys

def compute(s: str, bound: int) -> int:
    coords = set()
    min_x, min_y = sys.maxsize, sys.maxsize
    max_x, max_y = 0, 0

    for line in s.splitlines():
        xs, ys = line.split(',')
        x, y = int(xs), int(ys)
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)
        coords.add((x, y))

    total_in_bounds = 0

    adj = bound // len(coords)
    for x in range(min_x - adj, max_x + adj):
        for y in range(min_y - adj, max_y + adj):
            total_distance = 0
            for coord_x, coord_y in coords:
                total_distance += abs(coord_x - x) + abs(coord_y - y)

            if total_distance < bound:
                total_in_bounds += 1

    return total_in_bounds

with open('2018/d6-input.txt', 'r')as f:
    s= f.read()

print(compute(s,10000))