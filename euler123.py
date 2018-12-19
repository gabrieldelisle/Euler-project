from time import time
t = time()

n_max = 300000
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
print(time()-t)


i=0
while ( (primes[i]-1)**(i+1) + (primes[i]+1)**(i+1) )%primes[i]**2 < 10**10:
	i+=1

print(i+1, primes[i])
print(time()-t)

