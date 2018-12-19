# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:54:31 2015

@author: gabrieldelisle
"""
import random as rd


def groupe(i,j) :
	i0=i//3*3
	j0=j//3*3
	l=[]
	for k in range(9) :
		if k!=j :
			l.append([i,k])
	for k in range(9) :
		if k!=i :
			l.append([k,j])
	for m in range(3) :
		for n in range(3) :
			if i0+m!=i and j0+n!=j :
				l.append([i0+m,j0+n])
	return l

Groupes=[]
for i in range(9) :
	Groupes.append([])
	for j in range(9) :
		Groupes[i].append(groupe(i,j))
							 

def to_grille(line) :
	g = []
	for i in range(9) :
		g.append([])
		for j in range(9) :
			g[i].append(int(line[9*i+j]))
	return g


def copie2(grille) :
	b=[]
	for u in grille :
		b.append(u.copy())
	return b

def fini(grille) :
	for i in range(9) :
		for j in range(9) :
			if grille[i][j]==0 :
				return False
	return True


def possibilities(grille,i,j) :
	if grille[i][j] :
		return[]
	else :
		p = list(range(1,10))
		for x,y in Groupes[i][j] :
			a = grille[x][y]
			if a!=0 :
				p[a-1] = 0
		p2 = []
		for u in p :
			if u!=0 :
				p2.append(u)
		return p2

def solve(grille) :
	pile = [(grille,0,0)]
	while pile:
		g,i,j = pile.pop()
		if j==9 :
			i+=1
			j=0
		if i==9 :
			return g	

		if g[i][j]==0 :
			for k in possibilities(g,i,j):
				g[i][j] = k
				pile.append((copie2(g), i,j+1))
		else :
			pile.append((g,i,j+1))
	return "error"