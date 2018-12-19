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


t = time()
t_max = 50000000
occ = {}
s = 0
i = 0
while primes[i]**4 <= t_max :
    j=0
    t2_max = t_max - primes[i]**4
    while primes[j]**3 <= t2_max : 
        k = 0
        t3_max = t2_max - primes[j]**3
        while primes[k]**2 <= t3_max : 
            p  = primes[k]**2+t_max-t3_max
            try : 
                occ[p] +=1
            except :
                occ[p] = 0
                s+=1
            k+=1
        j+=1
    i+=1
print(s)
print(time()-t)
