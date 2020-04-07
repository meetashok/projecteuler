## Problem 91
## Right triangles with integer coordinates

import itertools

def right_triangle(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    
    a2 = x1**2 + y1**2
    b2 = x2**2 + y2**2
    c2 = (x2 - x1)**2 + (y2 - y1)**2

    return (a2 + b2 == c2) or (b2 + c2 == a2) or (c2 + a2 == b2)

def main():
    points = []

    for x in range(51):
        for y in range(51):
            points.append((x, y))
    
    count = 2500

    for comb in itertools.combinations(points, 2):
        point1, point2 = comb
        if point2[1]*point1[0] < point1[1]*point2[0]:
            if right_triangle(point1, point2):
                count += 1

    return count

if __name__ == "__main__":
    answer = main()
    print(answer)
