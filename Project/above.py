import numpy as np
is_above = lambda p,a,b: np.cross(p-a, b-a) < 0
 
a = np.array([25.23,49.77]) # [x,y]
b = np.array([49.77,25.23]) # [x,y]

p1 = np.array([32,25])

if is_above(p1,a,b):
    print('Is above')
else:
    print('Is below')
