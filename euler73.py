from time import time
from math import gcd

def pgcd(a,b):
	if a>b :
		a,b = b,a
	while a>0 :
		a,b = b%a,a
	return b

t = time()
N = 12000
s = 0
for d in range(4, N+1) :
	for u in range(d//3+1, d//2+1) :
		if gcd(u,d)==1 :
			s+=1
print(s)
print(time()-t)