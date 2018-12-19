from time import time
t = time()
n_max = 100000
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

def is_prime(n) :
    if n<n_max :
        return integers[n]!=0
    else :
        i=0
        while primes[i]*primes[i]<=n :
            if n%primes[i]==0 :
                return False
            i+=1
        return True

print(time()-t)

fact=[1]

s = 1
for i in range(1,10) :
	s*=i
	fact.append(s)

def count(beginning, available) :
	last = len(beginning)-1
	if not available :
		if is_prime(beginning[last]) :
			return 1/fact[len(beginning)]
		else:
			return 0

	s = 0
	for i,u in enumerate(available) :
		#new number
		if last==-1 or is_prime(beginning[last]) :
			new = beginning+[u]
			s+= count(new, available[:i]+available[i+1:])
		
		#continue last
		if last>=0 :
			new = beginning.copy()
			new[last]*=10
			new[last]+=u
			s+= count(new, available[:i]+available[i+1:])
	return s

print(count([], list(range(1,10)) ))
print(time()-t)