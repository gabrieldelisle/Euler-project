from math import sqrt

l0 = list("123456789")

def pandigital(n) :
	l = list(str(n))
	l.sort()
	return l==l0

def pandigital2(n) :
	l = list(str(n))[:9]
	l.sort()
	return l==l0

def ordre(x) :
	i = 0
	while x>=1 :
		x//=10
		i+=1
	return i

phi = (1+sqrt(5))/2
phi2 = (1-sqrt(5))/2

a = 1
b = 1
c = 1
d = 1
e = 1
i=2
lastphi = phi**2
lastphi2 = phi2**2

while not pandigital2(d) or not pandigital(b):
	b,a = (a+b)%10**9, b
	d,c = c+d,d
	if c>10**15 :
		d//=10
		c//=10
	i+=1


print(i)


