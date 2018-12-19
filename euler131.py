from time import time
from math import sqrt
t=time()

N=100000

integers = list(range(N))
integers[1]=0
i = 2
while i*i <= N :
	if integers[i]!=0 :
		for j in range(2,(N-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

def is_prime(n) :
	if n<N :
		return integers[n]!=0
	else :
		i=0
		while primes[i]*primes[i]<=n :
			if n%primes[i]==0 :
				return False
			i+=1
		return True

def decomp(n) :
	if integers[n] :
		return [n]
	dec = []
	i=0
	while n!=1 :
		if n%primes[i]==0 :
			dec.append(primes[i])
			n//=primes[i]
		else :
			i+=1
	return dec

# print("primes generated")

# l = []
# for i in range(1,3) :
# 	if i%3!=0 :
# 		l.append(i)


# rad = [1]*(N+1)
# for a in l :
# 	for p in primes :
# 		for i in range(1,N//(p**a)+1) :
# 			rad[i*(p**a)]*=p

# print("start", time()-t)
# 

# for n in [] :
# 	estimated = n+int(n**(2/3))+1
# 	for k in range(estimated//rad[n]*rad[n],1+estimated,rad[n]) :
# 		
count = 0

i=1
p=0
while p<10**9 :
	n = i**3
	k = i**3+i**2
	if k**3%(n**2) == 0 :
		p = (k**3-n**3)//n**2
		if is_prime(p) :
			count+=1
	i+=1
print("count :", count)
print(time()-t)
