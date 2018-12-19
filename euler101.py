from polynome import *

P = X**10-X**9+X**8-X**7+X**6-X**5+X**4-X**3+X**2-X+1
l = [P.evaluer(i) for i in range(1,11)]
print(l)

def OP(k,n,liste) :
	p = lagrange(list(range(1,k+1)), liste[:k])
	for i in range(len(p.liste)) :
		if p[i]-int(p[i])>0.5 :
			p[i] = int(p[i])+1
		elif p[i]-int(p[i])<-0.5 :
			p[i] = int(p[i])-1
		else :
			p[i] = int(p[i])
	return p.evaluer(n)


s=0
for i in range(1,11) :
	print(OP(i,i,l)==l[i-1])
	o = OP(i,i+1,l)
	s+=o
print(s)