from time import time

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

print("beginning")
t = time()
ways = [[], [0]]
N_max = 5000

i=1
while ways[i][i-1]<N_max :
	i+=1
	ways.append([0])
	for j in range(1,i) :
		if is_prime(j) :
			ways[i].append(ways[i][j-1]+ways[i-j][min(i-j-1,j)]+(j>=i-j and is_prime(i-j)))
		else :
			ways[i].append(ways[i][j-1])

print(i)
print(time()-t)