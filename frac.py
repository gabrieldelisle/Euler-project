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
		return Frac(self.den, self.num)

	def simplifie(self) :
		p = pgcd(self.num, self.den)
		self.num//=p
		self.den//=p
		return self

	def copy(self) :
		return Frac(self.num, self.den)

	def __eq__(self, other) :
		if type(other)==Frac :
			return self.num*other.den == other.num*self.den
		elif type(other)== int :
			return self.num == other*self.den

	def __le__(self,other) :
		if type(other)==Frac :
			return self.num*other.den<=other.num*self.den
		elif type(other)== int :
			return self.num<=other*self.den

	def __lt__(self,other) :
		if type(other)==Frac :
			return self.num*other.den<other.num*self.den
		elif type(other)== int :
			return self.num<other*self.den

	def __add__(self,other) :
		if type(other)==Frac : 
			return Frac(self.num*other.den+other.num*self.den, self.den*other.den).simplifie()
		elif type(other)== int :
			return Frac(self.num+other*self.den, self.den).simplifie()

	def __sub__(self,other) :
		if type(other)==Frac : 
			return Frac(self.num*other.den-other.num*self.den, self.den*other.den).simplifie()
		elif type(other)== int :
			return Frac(self.num-other*self.den, self.den).simplifie()

	def __mul__(self,other) :
		if type(other)==Frac : 
			return Frac(self.num*other.num, self.den*other.den).simplifie()
		elif type(other)== int :
			return Frac(self.num*other, self.den).simplifie()

	def __truediv__(self,other) :
		if type(other)==Frac : 
			return Frac(self.num*other.den, self.den*other.num).simplifie()
		elif type(other) == int :
			return Frac(self.num, self.den*other).simplifie()

	def __str__(self) :
		return str(self.num)+"/"+str(self.den)

