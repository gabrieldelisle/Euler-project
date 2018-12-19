n_max = 100000
integers = list(range(n_max))
integers[1]=0
i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(2,(n_max-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

rad = [1]*(N+1)
for p in primes :
	for i in range(1,N//p+1) :
		rad[i*p]*=p

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
