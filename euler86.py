from math import sqrt, gcd
from time import time

t = time()
M_max = 2000
c_max = int(sqrt(5)*M_max)
primary = []
for m in range(1, int(sqrt(c_max))+1) :
	for n in range(1, min(m, int(sqrt(c_max-m))+1)) :
		if (m+n)%2==1 and gcd(n,m)==1 : 
			a = m*m-n*n
			b = 2*m*n
			c = m*m+n*n
			primary.append([a,b,c])

triplets = []
for u in primary :
	for q in range(1, int(M_max/min(u))+1) :
		a,b,c = q*u[0], q*u[1], q*u[2]
		if a>b :
			a,b = b,a
		if b<=2*a :
			triplets.append([a,b,c])
		triplets.append([b,a,c])
		
triplets.sort(key = lambda x: x[0])

s = 0
i = 0
while s<1000000 :
	a,b,c = triplets[i]
	if a<=b :
		s+=a-(b-b//2)+1
	else :
		s+=b//2
	i+=1
print(s, triplets[i-1][0])
print(time()-t)

# def d(a,b,c) :
# 	return sqrt(a**2+ (b+c)**2)
# def is_integer(n) :
# 	return n-int(n)==0

# test = []
# m=1
# s = 0
# s_max=2000
# while s<s_max : 
# 	a = m
# 	for b in range(1, a+1) :
# 		for c in range(1, b+1) :
# 			if is_integer(d(a,b,c)) :
# 				s+=1
# 	m+=1
# print(m-1,s)