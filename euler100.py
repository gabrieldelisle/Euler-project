from math import sqrt

def test(a,b) : 
	return 2*a*(a-1) - b*(b-1) == 0

def solve(a,b,c) :
	delta = b*b-4*a*c
	return (-b+sqrt(delta))/2/a

def nearest(n) :
	#return solve(2,-2,-n*(n-1))
	return (1+sqrt(1+2*n*(n-1)))/2

for j in range(10**12, 2*10**12,1000000) :
	for i in range(j,j+1000000,4) :
		p = nearest(i)
		if p==int(p) and test(int(p),i): 
			print(p,i)
		p = nearest(i+1)
		if p==int(p) and test(int(p),i+1): 
			print(p,i+1)
	print(i)

5*3 	2*7 *2
3*7 	2*2*5

2*a*(a-1) - b*(b-1) == 0
(1.4*a-1.4/2)**2 - (b-1/2)**2 = 1/4
