

import numpy as np
import random


a = [["X", "X", "O", "X", "X", "X"], ["O", "O", "X", "O", "O", "O"], ["X", "X", "O", "X", "X", "P"]]

print("ok" if "." not in a else "pas ok")

for elem in a[-1]:
    print(elem)

print(not False and True)