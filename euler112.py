def decreasing(n) :
	c = 0
	while n :
		d=n%10
		n//=10
		if c>d :
			return False
		c = d
	return True

def increasing(n) :
	c = 9
	while n :
		d=n%10
		n//=10
		if c<d :
			return False
		c = d
	return True

def bouncing(n) :
	return not increasing(n) and not decreasing(n)

n=0
i=100
while 100*n!=99*i :
	i+=1
	if bouncing(i) :
		n+=1

print(i)
