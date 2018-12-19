from time import time

t = time()
ways = [[]]
N_max = 100
for i in range(1, N_max+1) :
	ways.append([0])
	for j in range(1,i) :
		ways[i].append(ways[i][j-1]+ways[i-j][min(i-j-1,j)]+(j>=i-j))

print(ways[N_max][N_max-1])
print(time()-t)