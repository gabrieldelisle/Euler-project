from time import time
from math import gcd, sqrt

t = time()
L=1500000

primary = []
for m in range(1, int(sqrt(L/2))+1 ) :
	for n in range(1, m) :
		if (m+n)%2==1 and gcd(n,m)==1 : 
			primary.append([m*m-n*n, 2*m*n, m*m+n*n])


length = []
for i in range(len(primary)) :
	l = sum(primary[i])
	if l<=L :
		length.append(l)

occ = {}
for u in length :
	q = 1
	while q*u<=L :
		try :
			occ[q*u]+=1
		except :
			occ[q*u] = 1
		q+=1

s = 0
for u in occ.keys() :
	if occ[u]==1 :
		s+=1

print(s)
print(time()-t)