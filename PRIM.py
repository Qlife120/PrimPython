import sys




class Graph:
	# To initialize a graph 
	def __init__(self,vertices):
		self.V=vertices
		# initialize adjacency matrix with 0's
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]


	# function to print the constructed MST stored in parent

	def printMST(self,parent):
		print("Edge \tWeight")

		for i in range(1,self.V):
			print(parent[i],"-","\t",self.graph[i][parent[i]])


	# function to find the min distance value from the set of vertices not yet include in the setMST
	def minKey(self,key,mstSet):

		Min = sys.maxsize

		for v in range(self.V):
			if key[v]<Min and mstSet==False: # if the value is less than the min and v is not present in the mstSet
				Min = key[v]
				min_index = v 

		return min_index # return the index of the vertex with the smallest distance not yet included in the mstSet
			

	def printMST(self):

		key = [sys.maxsize]*self.V
		parent = [None] * self.V

		# Initialize a vertex with value 0 so that is picked at first.
		key[0]=0
		mstSet=[False]*self.V

		parent[0] = -1

		for cout in range(self.V):
			# the min weight vertex from vertices not yet processed
			# u is the source

			u = self.minKey(key,mstSet)
			mstSet[u] = True

			for v in range(self.V):
				# self.graph[u][v] > 0 means that there is a an edge between u and v, mstSet[v]==False means that v is not included in the MST tree 
				# then if the weight of the edge is less than key[v]
				if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v]=u

		self.printMST(parent)


if __name__=="__main__":

	g = Graph(5)
	g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]

	g.printMST()            





