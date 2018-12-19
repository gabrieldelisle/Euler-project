from frac import Frac


F = Frac(3,7)

def nearest_left(den) :
	a = 0
	b = den
	while b-a>1 :
		c = (a+b)//2
		if Frac(c,den)<F :
			a = c 
		else :
			b = c
	return Frac(a,den)

f_near = Frac(0,1)
for i in range(1, 1000001) :
	f = nearest_left(i)
	if F-f<F-f_near :
		f_near = f.copy()

print(f_near)