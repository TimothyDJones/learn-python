# polysum.py

import math # required for tan function and pi constant

def polysum(n, s):
    """
    n: int, the number of sides of a regular polygon
    s: float, the length of each side of the regular polygon
    Returns a float which is the sum of the area of the polygon
        and the square of the perimeter of the polygon, rounded to 4
        decimal places.
    """
    def polyarea(n, s):
        return ((0.25 * n * s * s)/math.tan(math.pi / n))
    def polyperim(n, s):
        return (n * s)
        
    return round((polyarea(n, s) + polyperim(n, s)**2), 4)
