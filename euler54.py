import time 
t = time.time()
class Carte:
	"""docstring for Carte"""
	def __init__(self, name):
		self.value = name[0]
		self.color = name[1]
		self.name = name
		try :
			self.value = int(self.value)
		except :
			if self.value == 'T' :
				self.value = 10
			elif self.value == 'J' : 
				self.value = 11
			elif self.value == 'Q' :
				self.value = 12 
			elif self.value == 'K' :
				self.value = 13
			elif self.value == 'A' : 
				self.value = 14
			else : 
				print('error: unvalid card value (',self.value,')')

	def copy(self) :
		return Carte(self.name)

def display(hand) : 
	s = ''
	for u in hand : 
		s+=u.name+' '
	print(s)

def putfront(j, liste) :
	z = liste[j].copy()
	for i in range(j, 0, -1) :
		liste[i]=liste[i-1].copy()
	liste[0] = z.copy()

def is_flush(hand) : 
	c = hand[0].color
	for u in hand : 
		if u.color != c :
			return False
	return True

def is_straight(hand) : 
	for i in range(5) : 
		if hand[i].value != hand[0].value-i :
			return False
	return True

def is_pair(hand) : 
	for i in range(5) :
		for j in range(i+1, 5) :
			if hand[i].value == hand[j].value :
				putfront(i, hand)
				putfront(j, hand)
				return True
	return False

def is_brelan(hand) :
	for i in range(5) :
		for j in range(i+1, 5) :
			if hand[i].value == hand[j].value :
				for k in range(j+1, 5) :
					if hand[i].value == hand[k].value :
						putfront(i, hand)
						putfront(j, hand)
						putfront(k, hand)
						return True
	return False

def is_square(hand) :
	for i in range(5) :
		for j in range(i+1, 5) :
			if hand[i].value == hand[j].value :
				for k in range(j+1, 5) :
					if hand[i].value == hand[k].value :
						for l in range(k+1, 5) :
							if hand[i].value == hand[l].value :
								putfront(i, hand)
								putfront(j, hand)
								putfront(k, hand)
								putfront(l, hand)
								return True
	return False

def is_double(hand) :
	v = 0
	for i in range(5) :
		for j in range(i+1, 5) :
			if hand[i].value == hand[j].value :
				v = hand[i].value
				putfront(i, hand)
				putfront(j, hand)
	if v :
		for i in range(5) :
			for j in range(i+1, 5) :
				if hand[i].value == hand[j].value and hand[i].value != v :
					putfront(i, hand)
					putfront(j, hand)
					if v>hand[i].value :
						putfront(2, hand)
						putfront(3, hand)
					return True
	return False

def is_full(hand) :
	brelan = False
	for i in range(5) :
		for j in range(i+1, 5) :
			if hand[i].value == hand[j].value :
				for k in range(j+1, 5) :
					if hand[i].value == hand[k].value :
						brelan = True
						putfront(i, hand)
						putfront(j, hand)
						putfront(k, hand)
	if brelan and hand[3].value == hand[4].value :
					return True
	return False

def win(hands) :
	rank = [0,0]
	for i in range(2) : 
		hands[i].sort(key= lambda x: -x.value)
		if is_straight(hands[i]) and is_flush(hands[i]) : 
			rank[i]=8
		elif is_square(hands[i]) :
			rank[i]=7
		elif is_full(hands[i]) :
			rank[i]=6
		elif is_flush(hands[i]) :
			rank[i]=5
		elif is_straight(hands[i]) :
			rank[i]=4
		elif is_straight(hands[i]) :
			rank[i]=4
		elif is_brelan(hands[i]) :
			rank[i]=3
		elif is_double(hands[i]) :
			rank[i]=2
		elif is_pair(hands[i]) :
			rank[i]=1
			

	if rank[0]>rank[1] : 
		return 1
	elif rank[0]<rank[1] :
		return 0
	else : 
		for i in range(5) :
			if hands[0][i].value>hands[1][i].value : 
				return 1
			elif hands[0][i].value<hands[1][i].value :
				return 0
	print('error: equality')
	return 0




fichier = open('poker.txt', 'r')
file = fichier.read()
fichier.close()


turns = file.split('\n')
for i in range(len(turns)) : 
	turns[i] = turns[i].split(' ')
	for j in range(10) :
		turns[i][j] = Carte(turns[i][j])
	turns[i] = [turns[i][0:5], turns[i][5:10]]

s = 0
for i in range(len(turns)) : 
	s+= win(turns[i])

print(s)
print(time.time()-t)