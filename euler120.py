from math import gcd
from time import time
t = time()

def period(a,b) :
	i=1
	values = [1]
	while a**i%b != 1 :
		values.append(a**i%b)
		i+=1
	return i,values


s = 0
for a in range(3,1001) :
	i, vinf = period(a-1,a**2)
	j, vsup = period(a+1,a**2)
	s+= max([(vinf[k%i] + vsup[k%j])%a**2 for k in range(i*j//gcd(i,j))])
print(s)
print(time()-t)