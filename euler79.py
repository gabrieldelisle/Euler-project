file = open('keylog.txt', 'r')
content = file.read()
file.close()
codes = content.split('\n')

# def sans_doublons(l) :
# 	a = []
# 	for u in l :
# 		if not u in a :
# 			a.append(u)
# 	return a

# codes = sans_doublons(codes)
# print(codes)

possibilities = [('',0)]
while possibilities :
	c,i = possibilities.pop()
	# 3 chiffres communs
	found = False
	for j in range(len(c)-2) :
		if codes[i]==c[j:j+3] :
			found = True
	if found :
		possibilities.append((c, i+1))
	else :
		#2 chiffres communs
		#1 et 2
		for j in range(len(c)-1) :
			if codes[i][0:2]==c[j:j+2] :
				for k in range(j, len(c))
					s = c[0:k]+codes[i][2:3]+c[k:len(c)]
					possibilities.append(s, i+1)

		#2 et 3

['319', '680', '180', '690', '129', '620', '762', '689', '318', '368', '710', '720', '629', '168', '160', '716', '731', '736', '729', '316', '769', '290', '719', '389', '162', '289', '718', '790', '890', '362', '760', '380', '728']
73162890