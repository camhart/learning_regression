import random, numpy, math, signal, matplotlib.pyplot
# numpy only used to get gaussian noise for mutation

from base import Base

class HiddenNodesManager(Base):

	def __init__(self):
		self.nodes = []
		self.x = []
		self.y = []
		self.w = [5]
		self.numNodes = 10
		self.filename = 'multivariate_data-train.csv'

	def createPopulation(self):
		if(len(self.w) != len(self.x[0])):
			self.w = self.w * len(self.x[0])
		self.nodes = []
		for i in xrange(self.numNodes):
			self.nodes.append(GANode(self.w, self))

	def mutate(self):
		for node in self.nodes:
			node.mutate()

	def crossover(self):
		# instead of random use fitness
		tnodes = self.nodes  # copy necessary?
		self.nodes = []
		while(len(tnodes) > 0):
			i1 = random.randint(0, len(tnodes)-1)
			i2 = random.randint(0, len(tnodes)-1)
			n1 = tnodes[i1]
			n2 = tnodes[i2]
			l = tnodes[i1].crossover(tnodes[i2])
			tnodes.remove(n1)
			if(n1 != n2):
				tnodes.remove(n2)
				self.nodes.append(GANode(l[1], self))
			self.nodes.append(GANode(l[0], self))

	def loadCSVFile(self, filename=None):
		Base.loadCSVFile(self, filename=filename)
		for c in xrange(len(self.x)):
			self.x[c].insert(0, 1)

	def calcMse(self):
		self.fitnesses = [n.fitness() for n in self.nodes]
		self.totalMse = sum(self.fitnesses) #calculates n.mse value
		# self.maxw = max(self.fitnesses)

		# # self.pvalues = [100.0 / float((float(self.fitnesses[n])/float(self.totalMse)) * 100.0) for n in xrange(len(self.fitnesses))]
		# self.pvalues = []
		# for c in xrange(len(self.fitnesses)):
		# 	fitVal = self.fitnesses[c]
		# 	percent = fitVal / self.totalMse
		# 	nVal = 100.0 / (float(percent) * 100.0)
		# 	self.pvalues.append(nVal)

		# self.pmax = float(sum(self.pvalues))

		# self.probs = []
		# for c in xrange(len(self.fitnesses)):
		# 	self.probs.append((self.pvalues[c] / self.pmax) * 100.0)
		# print self.probs[c]
		# print sum(self.probs)
		# exit()


	def select(self):
		self.calcMse()
		tnodes = []
		# while(len(tnodes) < self.numNodes):
		# 	val = random.randint(0, 99)
		# 	summ = 0
		# 	c = random.randint(0, len(self.nodes) - 1)
			# for c in xrange(len(self.nodes)):

				# probability = (self.pvalues[c] / self.pmax) * 100.0
			# summ+=self.probs[c]


			# print self.probs[c]
			# if(val <= self.probs[c]):
			# 	tnodes.append(self.nodes[c])
			# 	# print "selected %f out of %f" % (self.probs[c], sum(self.probs))
			# 	if(len(tnodes) == self.numNodes):
			# 		break;
					# return self.nodes[c]
			# print 'summ:',summ

		minn = 0
		index = -1
		for c in xrange(len(self.fitnesses)):
			if(self.fitnesses[c] < minn):
				minn = self.fitnesses[c]
				index = c
		while(len(tnodes) < self.numNodes):
			tnodes.append(self.nodes[index])
		self.nodes = tnodes
		# print len(self.nodes)


class GANode(object):

	def __init__(self, weights, manager):
		self.w = weights
		self.mutateProbability = 50.0
		self.mutateScale = 0.000001
		self.manager = manager

	def mutate(self):
		self.manager.calcMse()
		for i in xrange(len(self.w)):
			if(random.randint(0, 99) <= self.mutateProbability):
				self.w[i] += numpy.random.normal(self.mutateScale / 2, self.mutateScale, 1)[0]

	def crossover(self, other_node):
		splitindex =  random.randint(0, len(self.w))
		cuta0 = self.w[:splitindex]
		cuta1 = self.w[splitindex:]
		cutb0 = other_node.w[:splitindex]
		cutb1 = other_node.w[splitindex:]
		return [(cuta0 + cutb1), (cutb0 + cuta1)]


	def _h(self, j):
		nlist = [self.w[i]*self.manager.x[j][i] for i in xrange(len(self.w))]
		return sum(nlist)

	def getMse(self):
		nlist = [ math.pow(self.manager.y[i] - self._h(i), 2) for i in xrange(len(self.manager.y))]
		self.mse = sum(nlist)
		# self.mse = 
		return self.mse

	def fitness(self):
		return self.getMse()


def main():
	hnm = HiddenNodesManager()
	mses = []
	iterations = []
	iteration = 0

	def printstuff():
		matplotlib.pyplot.plot(iterations, mses)
		matplotlib.pyplot.ylabel("Mean Square Error")
		matplotlib.pyplot.xlabel("Iterations")
		matplotlib.pyplot.savefig("ga_%s.png" % (hnm.filename, ))
		matplotlib.pyplot.clf()
		print len(hnm.nodes)
		print 'image saved to ga_%s.png' % (hnm.filename, )
		print 'iteration', iteration

	def handler(signum, frame):
		printstuff()

	print 'type ctrl+break or ctrl+pause to print current w and iteration count'
	# register ctrl+break to print values
	signal.signal(signal.SIGBREAK, handler)  #windows only
	# hnm.filename = 'nonlinear_data-train.csv'
	hnm.filename = 'univariate_data-train.csv'
	hnm.loadCSVFile()
	hnm.createPopulation()
	while(iteration < 10000):
		# hnm.createPopulation()
		hnm.mutate()
		hnm.crossover()
		# selectedNode = hnm.select()
		# hnm.w = selectedNode.w
		hnm.select()
		if(iteration % 50 == 0):
			# mses.append(selectedNode.getMse())

			mses.append(min([hnm.nodes[i].getMse() for i in xrange(len(hnm.nodes))]))
			iterations.append(iteration)
		iteration+=1
	printstuff()


if __name__ == '__main__':
	main()