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

MAX = 4*10**6


def test() :
	#*1
	p= 1
	s = 1
	i=0
	while s<MAX :
		print(p,s)
		s+=3**i
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*2 / *3
	p = 4
	s = 3
	i = 1
	while s<MAX :
		print(p,s)
		s+=3**(i-1)*5
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*4
	p = 8
	s = 4
	i = 1
	while s<MAX :
		print(p,s)
		s+=3**(i-1)*7
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*6
	p = 36
	s = 13
	i = 2
	while s<MAX :
		print(p,s)
		s+=3**(i-2)*25
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*8

	#*12
	p = 72
	s = 18
	i = 2
	while s<MAX :
		print(p,s)
		s+=3**(i-2)*5*7
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*16
	p = 32
	s = 6
	i = 1
	while s<MAX :
		print(p,s)
		s+=3**(i-1)*11
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*24

	#*30
	p = 900
	s = 63
	i = 3
	while s<MAX :
		print(p,s)
		s+=3**(i-3)*5*5*5
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*32
	p = 64
	s = 7
	i = 1
	while s<MAX :
		print(p,s)
		s+=3**(i-1)*13
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))

	#*36
	p = 216
	s = 25
	i = 2
	while s<MAX :
		print(p,s)
		s+=3**(i-2)*7*7
		p*=primes[i]
		i+=1
	print(i,s,p,len(str(p)))


# print(primes[13])



def greatest(n) :
	l = [1,2,4,6,8,12,16,24,32,36,48,64,72,96,128,144,192,216]
	p=1
	g = []
	i= 0
	while p<n :
		p*=primes[i]
		i+=1
		j = 0
		while l[j]<primes[i] :
			g.append(p*l[j])
			j+=1
	return g

print(greatest(10**17))
