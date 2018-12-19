from graph import Graph

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
for i in range(m) :
	for j in range(1,n) :
		g.add_edge(i+100*(j-1), i+100*j, matrix[i][j])

d = g.bfs(0,m-1+100*(n-1))
print(d+matrix[0][0])


# queue = [(0,0,0)]
# s_min = (m+n-1)*10000
# rejected = 0
# while queue :
#  i,j,s = queue.pop()
#  s+=matrix[i][j]
#  if s<s_min :
#     print("accepted : ", len(queue))
#     if i==m-1 and j==n-1 :
#        s_min = s
#        print(s)
#     elif i==m-1 :
#        queue.append((i, j+1, s))
#     elif j==n-1 :
#        queue.append((i+1, j, s))
#     else :
#        if matrix[i+1][j]>matrix[i][j+1] :
#           queue.append((i+1, j, s))
#           queue.append((i, j+1, s))
#        else :
#           queue.append((i, j+1, s))
#           queue.append((i+1, j, s))
#  else : 
#     rejected += 1
#     print("rejected : ",  rejected)
# print(s_min)
