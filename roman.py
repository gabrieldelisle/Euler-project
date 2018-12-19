romans = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
['M'*i for i in range(10)]]

values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman(n) :
	n_chiffres = len(str(n))
	chiffres = []
	while n>0 :
		chiffres.append(n%10)
		n//=10

	s = ''
	for i in range(n_chiffres-1,-1,-1) :
		s+= romans[i][chiffres[i]]
	return s

def dec(s) :
	l = []
	for u in list(s) :
		l.append(values[u])
	for i in range(len(l)-1) :
		if l[i]<l[i+1] : 
			l[i]*=-1
	return sum(l)