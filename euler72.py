from time import time

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

print('beginning')
t = time()
phis = [0, 1]
s = 0
for i in range(2, 1000001) :
    if is_prime(i) :
        phis.append(i-1)
    else :
        j = 0
        while i%primes[j]!=0 :
            j+=1
        d = primes[j] if (i//primes[j])%primes[j] == 0 else 1
        phis.append(phis[primes[j]] * phis[i//primes[j]] * d // phis[d])
    s+=phis[i]
print(s)
print(time() -t)