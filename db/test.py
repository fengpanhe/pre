
import numpy as np

aa = [np.array([1, 2, 3]), np.array([4, 5, 6])]
bb = [[2, 2, 2], [3, 3, 3]]

for a, b in zip(aa, bb):
    print(type(a))
    print(type(b))