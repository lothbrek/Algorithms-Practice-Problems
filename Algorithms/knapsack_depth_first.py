#classic knapsack program computed based on greedy algorithms
#using depth first searching
W = [2,5,10,5]
V = [40,30,50,10]
C = 16
N = len(W)
best = None

class Node:
	def __init__(self, i=-1, w=0, v=0, s=set()):
		self.index, self.weight, self.value, self.solution = i, w, v, s

	def Child(self, taken):
		c =  Node(self.index+1, self.weight, self.value, set(self.solution))
		if taken:
			c.weight += W[c.index]
			c.value += V[c.index]
			c.solution.add(c.index)
		return c

	def bound(self):
		best_possible = 0
		if self.weight <= C:
			l = self.index+1
			total_w = self.weight
			best_possible = self.value
			while l <= N-1 and total_w + W[l] <= C:
				total_w += W[l]
				best_possible += V[l]
				l += 1

			if l <= N-1:
				best_possible += (C-total_w) * float(V[l])/float(W[l])
		return best_possible

	def __str__(self):
		return "%d\tw=%d\tv=%d\t%s" % (self.index,self.weight,self.value,self.solution)



best = Node()
Solutions = [best]

while len(Solutions) > 0:
	s = Solutions.pop()
	if s.weight <= C and s.value > best.value:
		best = s
	print(s, "\t", s.bound(), best.value)

	if s.bound() > best.value and s.index < N-1:
		a =s.Child(True)
		Solutions.insert(0, a)

		b = s.Child(False)
		Solutions.insert(0, b)

print("BEST (DFS) IS", best)
