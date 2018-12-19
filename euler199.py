from math import pi, sqrt, cos, sin
import matplotlib.pyplot as plt
from time import time
t = time()

class Circle() :
	def __init__(self,x,y,r) :
		self.x = x
		self.y = y
		self.r = r

	def aire(self) :
		return pi*self.r**2

r0 = 1
r1 = 1/(1 + 2*sqrt(3)/3)
R = 1-r1

C0 = Circle(0,0,1)
C1 = [ Circle(R*cos(2*pi*i/3), R*sin(2*pi*i/3), r1) for i in range(3) ]


def show_circles(l) :
	ax=plt.gca()
	circle = plt.Circle((C0.x,C0.y), C0.r, fill=False, color='0')
	ax.add_patch(circle)

	n = len(l)
	colors = [[i/n,0, (n-i)/3/n] for i in range(n)]
	for i,u in enumerate(l) :
		for C in u :
			circle = plt.Circle((C.x,C.y), C.r, color=colors[i])
			ax.add_patch(circle)
	plt.axis('scaled')
	plt.show()


def between(a,b,c) :
	#linearisation
	alpha1 = 2*(a.x-b.x)
	beta1 = 2*(a.y-b.y)
	gamma1 = 2*(b.r-a.r)
	delta1 = a.x**2-b.x**2 + a.y**2-b.y**2 + b.r**2-a.r**2
	alpha2 = 2*(a.x-c.x)
	beta2 = 2*(a.y-c.y)
	gamma2 = 2*(c.r-a.r) if c.r<1 else -2*(c.r+a.r)
	delta2 = a.x**2-c.x**2 + a.y**2-c.y**2 + c.r**2-a.r**2

	#solution system 2x2
	det = alpha1*beta2-alpha2*beta1
	A = (beta2*gamma1 - beta1*gamma2) / det
	B = (beta2*delta1 - beta1*delta2) / det
	C = (alpha1*gamma2 - alpha2*gamma1) / det
	D = (alpha1*delta2 - alpha2*delta1) /det

	#reinjection
	E = A**2 + C**2 - 1
	F = A*(B-a.x) + C*(D-a.y) - a.r
	G = (B-a.x)**2 + (D-a.y)**2 - a.r**2

	#sol degree 2 equation
	delta = sqrt( F**2 - E*G )
	r1 = (-F - delta) / E
	r2 = (-F + delta) / E

	r = r1
	x = A*r + B
	y = C*r + D

	return Circle(x,y,r)
	
def steps(n) :
	a,b,c = C1
	holes = [C1, [a,b,C0], [b,c,C0], [a,c,C0]]
	draw = [C1]
	restant = C0.aire()-3*a.aire()
	for i in range(n) :
		draw.append([])
		tofill = holes.copy()
		holes = []
		for a,b,c in tofill :
			C = between(a,b,c)
			holes.append([C,a,b])
			holes.append([C,b,c])
			holes.append([C,a,c])
			draw[i+1].append(C)
			restant-=C.aire()
	print(restant/C0.aire())
	print(time()-t)
	show_circles(draw)

steps(7)
