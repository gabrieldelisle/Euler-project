from frac import Frac

def payout(p) :
	return (int(1/p))

def winning(n) :
	proba = [0]*(n+1)
	def next(p, success, turn) :
		if turn == n :
			proba[success]+= p
		else :
			win = 1/(turn+2)
			next(p*win, success+1, turn+1)
			next(p*(1-win), success, turn+1)
	next(1,0,0)
	print(proba)
	return sum(proba[n//2+1:])

print(payout(winning(15)))