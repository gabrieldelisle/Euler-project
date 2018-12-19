from time import time


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

rad = [1]*(n_max+1)
for p in primes :
	for i in range(1,n_max//p+1) :
		rad[i*p]*=p

t = time()

def A(n) :
	k=1
	rkmodn = 1
	m10 = 1
	while rkmodn!=0 :
		k+=1
		m10*=10
		m10%=n
		rkmodn+=m10
		rkmodn%=n
	return k

s=0

for p in primes[1:2]+primes[3:] :
	a = A(p)
	if rad[a] == 2 or rad[a] == 5 or rad[a] == 10 :
		print(p, a)
	else :
		s+=p

print(s)
