def rectangles(n,m) :
	s = 0
	for i in range(n) :
		for j in range(m) :
			s+=(n-i)*(m-j)
	return s

i=0
while rectangles(i,i)<2000000 :
	i+=1
print(i, rectangles(i,i))

nearest = 0,0
r_nearest = 0
for i in range(100) :
	for j in range(i) :
		r = rectangles(i,j)
		if abs(2000000-r)<abs(2000000-r_nearest) :
			nearest = i,j
			r_nearest = r

print(nearest, r_nearest)
