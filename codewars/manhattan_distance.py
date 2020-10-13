# manhattan_distance.py
# https://www.codewars.com/kata/52998bf8caa22d98b800003a/train/python

def manhattan_distance(pointA, pointB):
    return (abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1]))

if __name__ == "__main__":
    print(manhattan_distance([1,1],[1,1]))
    print(manhattan_distance([5,4],[3,2]))
    print(manhattan_distance([1,1],[0,3]))
    print(manhattan_distance([-1,-7],[-4,3]))
