from time import time
t = time()
known_powers = {}

def power(a, p, modulo) :
	if p == 0 :
		return 1
	elif p == 1 :
		return a
	else :
		try :
			return known_powers[p]
		except :
			p1 = p//2
			p2 = p - p1
			ans = power(a,p1,modulo)*power(a,p2,modulo)%modulo
			known_powers[p] = ans
			return ans


print((power(2,7830457,10**10)*28433+1)%10**10)
print(time()-t)
