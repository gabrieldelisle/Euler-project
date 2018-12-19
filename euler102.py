import numpy as np
from math import sqrt


def norm(a) :
	return sqrt(a.dot(a)) 

def inside(points) :
	A = np.array([points[0], points[1], 0])
	B = np.array([points[2], points[3], 0])
	C = np.array([points[4], points[5], 0])
	zero = np.array([0,0,0])

	return np.cross(B-A,zero-A).dot(np.cross(zero-A,C-A))>=0 and np.cross(C-B,zero-B).dot(np.cross(zero-B,A-B))>=0

file = open('triangles.txt', 'r')
content = file.read()
file.close()
triangles = content.split('\n')
s = 0
for t in triangles :
	points = [int(u) for u in t.split(',')]
	if inside(points) :
		s+=1
print(s)