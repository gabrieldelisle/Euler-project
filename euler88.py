from time import time

n_max = 25000
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

def smallest_divisor(n) :
    for p in primes :
        if n%p==0 :
            return p

def without_doubles(l) :
    a = []
    for u in l :
        u.sort()
        if u not in a :
            a.append(u)
    return a

def part(l) : 
    if len(l) == 0 :
        return [[]]
    else :
        ps = []
        p = part(l[1:])
        i=0
        u_old = 0
        for u in l[1:] : 
            if u!=u_old :
                li = l[1:].copy()
                li[i]*=l[0]
                pi = part(li)
                ps+=pi
                i+=1
                u_old = u
        ps+=[u+[l[0]] for u in p]
        return ps


t = time()
k_max = 12

N = [0,0]
k = 2
i = 2
while k<=k_max :
    d = smallest_divisor(i)
    if i - d - i//d == k-2 :
        N.append(i)
        k+=1
    i+=1


i = 2
for i in range(2,N[k_max]) :
    if i not in primes :
        dec = decomp(i)
        k = i - sum(dec) + len(dec) 
        for p in without_doubles(part(dec)) :
            k = i - sum(p) + len(p) 
            if k<=k_max and N[k]>i :
                N[k] = i


print(len(without_doubles(part(decomp(2*3*5*7*11)))))
print(N[2:30])
a = []
for u in N[2:] :
    if u not in a :
        a.append(u)
print(sum(a))
print(time()-t)