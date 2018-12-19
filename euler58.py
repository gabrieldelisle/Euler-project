n_max = 100000
integers = list(range(n_max))
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

print("primes generated")

def is_prime(n) :
	i=0
	while primes[i]*primes[i]<=n :
		if n%primes[i]==0 :
			return False
		i+=1
	return True

i = 1
s = 0
l = 1
r = 1
while r >= 0.1 : 
	l+=2
	for j in range(4) :
		i+=l-1
		if is_prime(i) :
			s+=1
	r = s/(2*l-1)
print(l, s, r)