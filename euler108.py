from frac import Frac
from time import time

n_max = 100
integers = list(range(n_max))
integers[1]=0
i = 2
while i*i <= n_max :
    if integers[i]!=0 :
        for j in range(i+1,n_max) :
            if j%i==0 :
                integers[j] = 0
    i+=1
primes = []
for i in range(2,n_max) :
    if integers[i]!=0 :
        primes.append(i)


def solutions(n) :
	s = 0
	for i in range(n+1, 2*n+1) :
		if (Frac(1,n)- Frac(1,i)).num ==1 :
			s+=1
	return s

def higher(k) :
	n = 32
	i = 0
	s = 0
	while s<k :
		s = solutions(n)
		print(n, s)
		n*=primes[i]
		i+=1
	return 

t = time()
def greatest(n) :
	l = [1,2,4,6,8,12,16,24,32,36,48,64,72,96,128,144,192,216]
	p=1
	i= 0
	sol = 1
	while p<n :
		sol+=3**i
		p*=primes[i]
		i+=1
		j = 0
		while l[j]<primes[i] :
			yield p*l[j],sol
			j+=1

# i = 2*3*5*7*11*13*2*3
# print(i, solutions(i))

# print(higher(1000))

for i,s in greatest(10000) :
	sol = solutions(i)
	print(i, sol, s, (sol-s)/3)
print(time()-t)