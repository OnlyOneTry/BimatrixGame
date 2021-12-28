import numpy as np
import nashpy as nash

P1 = np.array([[3, 0], [4, 1]])
P2 = np.array([[3, 4], [0, 1]])
prisoner_dilemma = nash.Game(P1, P2)

p1_sigma = [1, 0]
p2_sigma = [0, 1]
array1 = prisoner_dilemma[p1_sigma, p2_sigma]

eqs = prisoner_dilemma.support_enumeration()
array2 = list(eqs)

print(array1)
print(array2)
