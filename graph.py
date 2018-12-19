from collections import deque
from heapq import heappush, heappop


class Graph:
	def __init__(self):
		self.nodes = []
		self.edges = {}
		self.distances = {}

	def add_node(self, value):
		self.nodes.append(value)
		self.edges[value] = []

	def add_edge(self, from_node, to_node, distance=1):
		self.edges[from_node].append(to_node)
		self.distances[(from_node, to_node)] = distance


	def dijsktra(self, initial, final=None):
		colors = {}
		distances = {}
		prec = {}
		for n in self.nodes :
			colors[n] = 0
			distances[n] = float('inf')

		heap = [(0,initial)]
		distances[initial] = 0
		prec[initial] = None

		while heap : 
			a, node = heappop(heap)
			if node == final :
				path = [node]
				while prec[node] :
					node = prec[node]
					path.append(node)
				path.reverse()
				return distances[final], path
			if colors[node] == 0 : 
				colors[node] = 1
				for neighbour in self.edges[node] :
					d = distances[node]+self.distances[node, neighbour]
					if d < distances[neighbour]  :
						prec[neighbour] = node
						heappush(heap, (d,neighbour))
						distances[neighbour] = d
		if final==None :
			return distances, prec
		return float('inf'), []

	def bfs(self, initial, final) :
		colors = {}
		distances = {}
		for n in self.nodes :
			colors[n] = 0
			distances[n] = float('inf')

		queue = deque([initial])
		distances[initial] = 0
		colors[initial] = 1

		while queue : 
			node = queue.popleft()
			if node == final :
				return distances[final]
			for neighbour in self.edges[node] :
				distances[neighbour] = min(distances[neighbour], distances[node]+self.distances[node, neighbour])
				if colors[neighbour] == 0 :
					colors[neighbour] = 1
					queue.append(neighbour)
		return float('inf')


	def floyd_warshall(self) :
		for i in self.nodes :
			for j in self.nodes : 
				try : 
					self.distances[i,j]
				except :
					self.distances[i,j] = float('inf')

		for k in self.nodes :
			for i in self.nodes :
				for j in self.nodes : 
					if self.distances[i,j]>self.distances[i,k]+self.distances[k,j] :
						self.distances[i,j]=self.distances[i,k]+self.distances[k,j]

	def prim(self) :
		g = Graph() 
		colors = {}
		for node in self.nodes :
			g.add_node(node)
		heap = [(0,None,node)]

		for n in self.nodes :
			colors[n] = 0

		total = 0
		while heap :
			d, prec, node = heappop(heap)
			if not colors[node] :
				colors[node]=1
				if prec!=None :
					g.add_edge(prec,node,d)
					g.add_edge(node,prec,d)
					total+=d
				for neighbour in self.edges[node] :
					heappush(heap, (self.distances[node, neighbour], node, neighbour))
		return total, g