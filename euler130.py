from primes import is_prime

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


count = 0
k = 3
s = 0


while count<25 :
	if k%5!=0 and not is_prime(k) and (k-1)%A(k)==0 :
		print(k)
		s+=k
		count+=1
	k+=2
print(s)
