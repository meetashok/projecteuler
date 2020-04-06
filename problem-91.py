## Problem 91
## Right triangles with integer coordinates

import itertools

def right_angle(slope1, slope2):
    if (slope1 == -1) & (slope2 == 0):
        return True
    elif (slope1 == 0) & (slope2 == -1):
        return True
    elif slope1*slope2 == -1:
        return True
    else:
        return False

def right_triangle(coor1, coor2):
    x1, y1 = coor1
    x2, y2 = coor2
    
    s1 = (y2 - y1) / (x2 - x1) if x2 != x1 else -1
    s2 = y1 / x1 if x1 != 0 else -1
    s3 = y2 / x2 if x2 != 0 else -1

    if right_angle(s1, s2) or right_angle(s2, s3) or right_angle(s3, s1):
        return True    
    return False


def main():
    xpoints = list(range(0, 51))
    ypoints = list(range(0, 51))

    points = []

    for x in xpoints:
        for y in ypoints:
            points.append((x, y))
    
    count = 0

    for comb in itertools.combinations(points, 2):
        point1, point2 = comb
        if right_triangle(point1, point2):
            count += 1
            print(point1, point2)

    return count

if __name__ == "__main__":
    answer = main()
    print(answer)
