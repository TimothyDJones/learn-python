# area_of_n-sided_polygon.py
# https://www.codewars.com/kata/5727500a20c7f837fc001869/train/python

# We use the "shoelace formula" to calculate the area.
# https://www.101computing.net/the-shoelace-algorithm/

def area_polygon(vertex):
    if len(vertex) < 3:
        return -1
    a = vertex[len(vertex) - 1][0]*vertex[0][1]
    b = vertex[len(vertex) - 1][1]*vertex[0][0]
    for i in range(len(vertex) - 1):
        a += vertex[i][0] * vertex[i + 1][1]
        b += vertex[i][1] * vertex[i + 1][0]
    
    return round((abs(a - b) / 2), 1)     # Round to nearest 1/10.

if __name__ == "__main__":
    print(area_polygon([(1, 1), (3, 4), (6, 1)]))
    print(area_polygon([(1, 3), (3, 3), (3, 1), (1, 1)]))
    print(area_polygon([(0, 5), (3, 3), (2, -3), (-2, -3), (-3, 3)]))
