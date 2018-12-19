from graph import Graph

file = open('network.txt', 'r')
# file = open('test107.txt', 'r')
lines = file.read().split('\n')
file.close()

g = Graph()
for i in range(len(lines)) :
	g.add_node(i)

for i in range(len(lines)) :
 	elements = lines[i].split(',')
 	for j in range(len(elements)) :
 		if elements[j]!='-' :
 			g.add_edge(i,j,int(elements[j]))

w = g.prim()[0]

print(sum(g.distances.values())//2-w)