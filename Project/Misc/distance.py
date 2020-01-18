import numpy
from numpy import arccos, array, dot, pi, cross
from numpy.linalg import det, norm
a1 = array([-5,0])
a2 = array([5,0])

# def distance(x,y):
#     p = numpy.array([x,y])
#     d = norm(numpy.cross(a2-a1, a1-p))/norm(a2-a1)
#     return d

def distance(x,y):
    p = array([x,y])
    if all(a1 == p) or all(a2 == p):
        return 0
    if arccos(dot((p - a1) / norm(p - a1), (a2 - a1) / norm(a2 - a1))) > pi / 2:
        return norm(p - a1)
    if arccos(dot((p - a2) / norm(p - a2), (a1 - a2) / norm(a1 - a2))) > pi / 2:
        return norm(p - a2)
    return norm(cross(a1-a2, a1-p))/norm(a2-a1)

print(distance(9,4))
