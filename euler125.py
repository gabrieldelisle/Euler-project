def palyndrome(n) :
	s =str(n)
	return all([s[i]==s[len(s)-i-1] for i in range(len(s)//2)])

def somme2(i,j) :
	k=i+j-1
	return (k*(k+1)*(2*k+1) - (j-1)*j*(2*j-1) )//6
	
def somme(i,j) :
	return sum([k*k for k in range(j, j+i)])


somme3 = [somme2(1,j) for j in range(0,10**4+5)]

s = 0
liste = []
for i in range(2,1000) :
	j=1
	n=0
	while n<10**8 :
		if palyndrome(n) and n not in liste:
			s+=n
			liste.append(n)
		print(j,i)
		n = somme3[i+j]-somme3[j-1]
		j+=1
print(s)
print(len(liste))