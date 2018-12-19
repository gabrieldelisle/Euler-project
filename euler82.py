from graph import Graph

file = open("matrix81.txt", 'r')
content = file.read()
file.close()

lines = content.split('\n')
table = [l.split(',') for l in lines]
matrix = [[int(e) for e in l] for l in table]
m,n = len(matrix),len(matrix[0])
print(matrix[:2])

g = Graph()
for i in range(m) :
	for j in range(n) :
		g.add_node((i,j))
for i in range(1,m) :
	for j in range(n) :
		g.add_edge((i-1,j), (i,j), matrix[i][j])
		g.add_edge((i,j), (i-1,j), matrix[i-1][j])
		
		
for i in range(m) :
	for j in range(1,n) :
		g.add_edge((i,j-1), (i,j), matrix[i][j])
		

d = [g.dijsktra((i,0))[0] for i in range(n)]

print(min([d[i][(j,m-1)] + matrix[i][0] for j in range(n) for i in range(n)]))