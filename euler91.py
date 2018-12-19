from math import gcd
from time import time
t = time()


n = 500

#triangles with right angle at 0,0
s = n*n

#triangle with right angle at x,y
for x in range(n+1) :
	for y in range(x==0,n+1) :
		g = gcd(x,y)
		a = y//g
		b = -x//g
		m = 1
		while x+m*a<=n and x+m*a>=0 and y+m*b<=n and y+m*b>=0 :
			m+=1
			s+=1
		m = -1
		while x+m*a<=n and x+m*a>=0 and y+m*b<=n and y+m*b>=0 :
			m-=1
			s+=1
			
print(s)
print(time()-t)