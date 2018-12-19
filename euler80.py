from frac import Frac
from math import sqrt, log2


def div(a,b,c) :
	u = a//b
	dec = []
	a-=u*b
	for i in range(c) :
		a*=10
		dec.append(a//b)
		a-=b*dec[i]
	return u, dec



n_dec = 103
n_dicho = int(n_dec*log2(10))+1
n_max = 99

s = 0
for i in range(n_max+1) :
	z = int(sqrt(i))
	if z*z!=i :
		a = Frac(z)
		b = Frac(z+1)
		for j in range(n_dicho) :
			c = (a+b)/2
			if c*c<i :
				a = c
			else :
				b = c
		u, dec = div(a.num,a.den,n_dec)
		#ent = [int(k) for k in list(str(u))]

		s+=u+sum(dec[:99])
print(s)


# 10**100 = 2**N
# N = 100*log2(10)