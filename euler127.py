from time import time
from math import gcd 




# def decomp(n) :
# 	if n<n_max and integers[n] :
# 		return [n]
# 	dec = []
# 	i=0
# 	while n!=1 :
# 		if n%primes[i]==0 :
# 			dec.append(primes[i])
# 			n//=primes[i]
# 		else :
# 			i+=1
# 	return dec


# radical = {}

# def rad(n) :
# 	try :
# 		return radical[n]
# 	except :
# 		dec = decomp(n)
# 		last = 1
# 		r = 1
# 		for u in dec :
# 			if u!=last :
# 				last = u
# 				r *= u
# 		radical[n] = r
# 		return r

# #
# def is_hit(a,b,c) :
# 	return a+b==c and a<b and gcd(a,b)==1 and gcd(a,c)==1 and gcd(b,c)==1 and rad(a*b*c)<c





t = time()


s = 0
nb = 0
N = 10000

integers = list(range(N))
integers[1]=0
i = 2
while i*i <= N :
	if integers[i]!=0 :
		for j in range(2,(N-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

rad = [1]*(N+1)
for p in primes :
	for i in range(1,N//p+1) :
		rad[i*p]*=p

def is_hit(a,b,c) :
	return rad[a]*rad[b]*rad[c]<c and gcd(a,b)==1


for a in range(1,N) :
	i=0
	while a%primes[i]==0 :
		i+=1
	j=i+1
	while a%primes[j]==0 :
		j+=1
	m = max(a+1,rad[a]*primes[i]*primes[j]-a)
	for b in range(m, N-a) :
		c = a+b
		# if is_hit(a,b,c) :
		# 	s+=c
		# 	nb+=1
		# 	print(a,b)

print(nb, s)
print(time()-t)