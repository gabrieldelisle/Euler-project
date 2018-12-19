class Polynome(object) :
	def __init__(self, s) :
		if type(s) ==list :
			self.liste = s
		elif type(s) == str :
			i=0
			n=False
			p=[]
			while i<len(s) :
				if s[i]=='-' :
					n=True
					i=i+1
				elif s[i]=='+' :
					n=False
					i=i+1
				elif s[i]==' ' :
					i=i+1
				c=0
				while i<len(s) and ord(s[i])>=ord('0') and ord(s[i])<=ord('9') :
					c=10*c+ord(s[i])-ord('0')
					i=i+1
				ixe=False
				if(i<len(s) and(s[i] == 'X' or s[i] == 'x')) :
					ixe = True
					i=i+1
				if ixe and c==0 :
					c=1
				e=0
				while i<len(s) and ord(s[i])>=ord('0') and ord(s[i])<=ord('9') :
					e=10*e+ord(s[i])-ord('0')
					i=i+1
				if ixe and e==0 :
					e=1
				while len(p)<e+1 :
					p.append(0)
				if n :
					p[e]=p[e]-c
				else :
					p[e]=p[e]+c
			while p!=[] and p[len(p)-1]==0 :
				del(p[len(p)-1])
			self.liste = p
		elif type(s) == Polynome :
			self.liste = []
			for i in range(len(s.liste)) :
				self.liste.append(s.liste[i])
		elif type(s) == int :
			if s==0 :
				self.liste=[]
			else :
				self.liste = [s]
		 
	
	def __repr__(self) :
		s=""
		if self.degre()<0 :
			s='0'
		else :
			for i in range (len(self.liste)-1,-1,-1) :
				if self.liste[i]!=0 :
					if self.liste[i]>0 and i<len(self.liste):
						s+='+'
					elif self.liste[i]<0 :
						s+='-'
					if i==0 or abs(self.liste[i]) !=1 :
						s+=str(abs(self.liste[i]))
					if i>0 :
						s+='X'
					if i>1 :
						s+="**"
						s+=str(i)
			if s[0]=='+' :
				s=s[1:]
		return s

	def __getitem__(self, index):
		return self.liste[index]

	def __setitem__(self, index, valeur):
		self.liste[index] = valeur

	def copy(self) :
		return Polynome(self)

	def simplifier(self) :
		while self.liste!=[] and self[len(self.liste)-1]==0 :
			del(self.liste[len(self.liste)-1])
		return self

	def degre(self) :
		self.simplifier()
		return len(self.liste)-1

	def __add__(self,b) :
		if type(b) == int or type(b) == float :
			return self+Polynome(str(b))
		la=len(self.liste)
		lb=len(b.liste)
		poly=Polynome(0)
		for i in range(min(la,lb)) :
			poly.liste.append(self[i])
			poly.liste[i] += b.liste[i]
		if lb>la :
			for i in range(la,lb) :
				poly.liste.append(b[i])
		else :
			for i in range(lb,la) :
				poly.liste.append(self[i])
		return poly.simplifier()

	def __sub__(self,b) :
		if type(b) == int or type(b) == float :
			return self-Polynome(str(b))
		else :
			la=len(self.liste)
			lb=len(b.liste)
			poly=Polynome(0)
			for i in range(min(la,lb)) :
				poly.liste.append(self[i])
				poly[i] -= b[i]
			if lb>la :
				for i in range(la,lb) :
					poly.liste.append(-b[i])
			else :
				for i in range(lb,la) :
					poly.liste.append(self[i])
			return poly.simplifier()

	def __eq__(self, b) :
		if b==0 :
			return self.degre()==-1
		elif type(b)==Polynome :
			return self-b==0
		else :
			return False

	def __mul__(self, b) :
		if type(b) == int or type(b) == float :
			poly = self.copy()
			for i in range(len(self.liste)) :
				poly[i] = poly[i]*b
			return poly
		else :
			poly = Polynome(0)
			for i in range(len(self.liste)) :
				p=Polynome(0)
				p.liste = i*[0]+(self[i]*b).liste
				poly = poly+p
			return poly.simplifier()
		
	def __rmul__(self,b) :
		return(self*b)

	def __truediv__(self,b) :
		return 1/b*self
	
	def __floordiv__(self,b) :
		q=Polynome(0)
		r=self.copy()
		while r.degre() >= b.degre() :
			q = q + r[r.degre()]/b[b.degre()]*X**(r.degre()-b.degre())
			r = self - b*q
		return q.simplifier()

	def __mod__(self,b) :
		q=Polynome(0)
		r=self.copy()
		while r.degre() >= b.degre() :
			q = q + r[r.degre()]/b[b.degre()]*X**(r.degre()-b.degre())
			r = self - b*q
		return r.simplifier()

	def __pow__(self, n) :
		if n == 1 :
			return self
		elif n==0 :
			return Polynome(1)
		elif self==X :
			return Polynome(n*[0]+[1])
		else :
			return (self**(n//2))*(self**(n-n//2))
								  
	def evaluer(self,t) :
		s=0
		for i in range(len(self.liste)) :
			s=t*s+self.liste[len(self.liste)-1-i]
		return s

	def deriver(self, n=1) :
		poly=self.copy()
		for j in range(n) :
			for i in range(len(self.liste)) :
				poly[i] = poly[i+1]*(i+1)
		return poly

	def primitiver(self, n=1) :
		poly=self.copy()
		for j in range(n) :
			for i in range(len(self.liste)) :
				poly[i] = poly[i+1]/(i+1)
		return poly

	def pgcd(a,b) :
		if a.degre()>b.degre():
			p=a.copy()
			q=b.copy()
		else :
			q=a.copy()
			p=b.copy()
		while q!=0:
			print(p)
			p,q = q,p%q
		p.simplifier()
		return 1/p[p.degre()]*p

def lagrange(x,y) :
	s=Polynome(0)
	for j in range(len(x)) :
		t=Polynome(1)
		for k in range(len(x)) :
			if k!=j :
				t*=(X-x[k])/(x[j]-x[k])
		s+=y[j]*t
	return s


X = Polynome([0,1])