from sudoku import *
from time import time

t = time()
file = open('sudoku.txt', 'r')
content = file.read()
file.close()
s = 0
for u in content.split('\n') :
	sudoku = to_grille(u)
	sol = solve(sudoku)
	print(sol)
	s+=sum([sol[0][i]*10**(2-i) for i in range(3)])
print(time()-t)
print(s)