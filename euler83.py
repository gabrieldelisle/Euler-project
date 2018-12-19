from graph import Graph
from time import time

file = open("matrix81.txt", 'r')
content = file.read()
file.close()

lines = content.split('\n')
table = [l.split(',') for l in lines]
matrix = [[int(e) for e in l] for l in table]
m,n = len(matrix),len(matrix[0])

g = Graph()
for i in range(m) :
	for j in range(n) :
		g.add_node(i+100*j)
for i in range(1,m) :
	for j in range(n) :
		g.add_edge(i-1+100*j, i+100*j, matrix[i][j])
		g.add_edge(i+100*j, i-1+100*j, matrix[i-1][j])
		
for i in range(m) :
	for j in range(1,n) :
		g.add_edge(i+100*(j-1), i+100*j, matrix[i][j])
		g.add_edge(i+100*j, i+100*(j-1), matrix[i][j-1])


t = time()
d, p = g.dijsktra(0,m-1+100*(n-1))
print(time()-t)
print(p)
print(d+matrix[0][0])