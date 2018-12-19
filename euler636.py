N = 10**6
integers = list(range(N))
integers[1]=0
i = 2
while i*i <= N :
	if integers[i]!=0 :
		for j in range(2,(N-1)//i+1) :
			integers[j*i] = 0

	i+=1
primes = [u for u in integers if u!=0]

#decomposition of N!

dec = [0]*len(primes)
for i,p in enumerate(primes) :
	j=1
	while p**j<=N :
		dec[i]+=N//(p**j)
		j+=1
print(len(dec))


occurences = [0]*(dec[0]+1)
for k in dec :
	occurences[k]+=1
