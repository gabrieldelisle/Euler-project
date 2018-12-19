from math import gcd, sqrt

primary = []
for m in range(1, 1000 ) :
	for n in range(1, m) :
		if (m+n)%2==1 and gcd(n,m)==1 : 
			primary.append([m*m-n*n, 2*m*n, m*m+n*n])