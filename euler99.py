from math import gcd, log
from time import time
t=time()

n_max = 1000
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

def decomp(n) :
    dec = []
    i=0
    while n!=1 :
        if n%primes[i]==0 :
            dec.append(primes[i])
            n//=primes[i]
        else :
            i+=1
    return dec


def compare2(a,pa,b,pb) :
	chiffres(a)
	g = gcd(a,b)
	pg = gcd(pa,pb)

	pa2 = pa//pg
	pb2 = pb//pg

	a2 = a//g
	b2 = b//g

	return pa2*log(a2) + (pa2-pb2)*log(g) > pb2*log(b2)


def compare(a,b,c,d) :
	return b*log(a)>d*log(c)

def compare3(a,b,c,d) :
	return a > c**(d/b)

file = open('base_exp.txt', 'r')
content = file.read()
file.close()

lines = content.split('\n')
pairs = [l.split(',') for l in lines]
pairs = [(int(p[0]), int(p[1])) for p in pairs]

a_max = 1
p_max = 1
i_max = 0
i=0
for a,p in pairs :
	i+=1
	if compare3(a,p,a_max,p_max) :
		a_max, p_max, i_max = a,p,i
print(i_max)
print(time()-t)