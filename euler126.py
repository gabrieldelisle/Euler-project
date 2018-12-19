def cache(aire, somme, i) :
	return aire+4*i*(somme+i-1)

def aire(a,b,c) :
	return 2*(a*b+b*c+c*a)

wanted = 1000


limit = 2
inf=1
Cuboids = {}
while wanted not in Cuboids.values() :
	limit*=2
	Cuboids = {}
	a=1
	while 4*a+2<=limit:
		b=a
		while 2*(a+b+a*b)<=limit:
			c=b
			while aire(a,b,c)<=limit:
				A = aire(a,b,c)
				S = a+b+c
				i=0
				couche = cache(A, S, i)
				while couche<limit:
					if couche in Cuboids :
						Cuboids[couche]+=1
					else :
						Cuboids[couche]=1
					i+=1
					couche = cache(A, S, i)
				c+=1
			b+=1
		a+=1
	if Cuboids :
		print(limit, max(Cuboids.values()))

print(min(i for i in Cuboids if Cuboids[i]==wanted))
