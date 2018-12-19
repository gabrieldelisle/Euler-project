from time import time


n_max = 1000000
integers = list(range(n_max))
integers[1]=0
i = 2
while i*i <= n_max :
	if integers[i]!=0 :
		for j in range(2,(n_max-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

t = time()


def Rmod(k,n) :
	m = 0
	m10 = 1
	for i in range(k) :
		m+=m10
		m10*=10
		m10%=n
		if m10==1:
			return (k//(i+1)*m+Rmod(k%(i+1),n))%n
	return m%n


N=10**9
s=0
count = 0
for p in primes[1:2]+primes[3:] :
	if Rmod(N,p)==0 :
		s+=p
		count+=1
		print(count,":",p)
		if count==40 :
			break
print(s)
print(time()-t)

