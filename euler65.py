def pgcd(a,b):
    while a!=0 and b!=0 :
        if a>b :
            a=a%b
        else :
            b=b%a
    return a+b

class Frac:
	"""docstring for Frac"""
	def __init__(self, num, den=1):
		self.num = num
		self.den = den

	def inverse(self) :
		self.num, self.den = self.den, self.num

	def simplifie(self) :
		p = pgcd(self.num, self.den)
		self.num/=p
		self.den/=p

	def __iadd__(self, ent) :
		self.num += self.den*ent
		return self

	def __str__(self) :
		return str(self.num)+' / '+str(self.den)

def compute(ent, liste) :
	s = Frac(0)
	for i in range(len(liste)-1, -1, -1):
		s += liste[i]
		s.inverse()
	s+= ent
	return s

# generation of 
e = [1]
i = 0
while(i<98) :
	if i%3==0 :
		e.append(2*(1+i//3))
	else :
		e.append(1)
	i+=1

print(len(e))

a = list(str(compute(2, e).num))

print(sum([int(u) for u in a]))