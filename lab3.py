import matplotlib.pyplot as pp

class Base(object):

	def loadCSVFile(self, filename=None):
		if filename is None or filename is '':
			filename = self.filename

		with open(filename) as f:
			for line in f.readlines():
				splitUp = line.split(',')
				self.y.append(float(splitUp[-1]))
				self.x.append([float(val) for val in splitUp[0:-1]])


class UniVariateLinearRegression(Base):

	def __init__(self):
		self.x = []
		self.y = []
		self.w = [2]
		self.alpha = 0.001
		self.filename = 'univariate_data-train.csv'
		self.returnCondition = 0.0000001

	# def h(self):
	# 	return 1.0 * 

	# def findLine(self):
	# 	self.w = self.w * len(self.x)
	# 	print self.w

	# 	maxDistance = float('inf')

	# 	while maxDistance > self.returnCondition:	#convergence test
	# 		for c in xrange(len(self.w)):
	# 			w = self.w[c]

	# 			w = w - self.alpha

	# 	return self.w

	def xTimesYSum(self):
		val = 0
		for c in xrange(len(self.x)):
			val+= self.x[c] * self.y[c]
		return val

	def ySquaredSum(self):
		return sum([y*y for y in self.y])

	def xSquaredSum(self):
		return sum([x*x for x in self.x])

	def ySum(self):
		return sum(self.y)

	def xSum(self):
		return sum(self.x)

	def sum(self, alist):
		val = 0
		for x in alist:
			val+=x
		return val

	def findLine(self):
		self.w = self.w * 2
		N = len(self.y)
		self.w[1] = (N*self.xTimesYSum() - (self.xSum() * self.ySum())) / (N * self.xSquaredSum() - self.xSum()*self.xSum())
		self.w[0] = (self.ySum() - self.w[1] * self.xSum()) / N
		return self.w

	def printValues(self):
		stri = ''
		for c in xrange(len(self.y)):
			# stri = ''.join([stri, '{', str(self.x[c]), ',', str(self.y[c]), '},'])
			print self.x[c], ',', self.y[c]
		print stri

	@classmethod
	def run(cls):
		uvlr = UniVariateLinearRegression()
		uvlr.loadCSVFile()
		uvlr.x = [item for sublist in uvlr.x for item in sublist]
		ws = uvlr.findLine()
		print ws
		pp.scatter(uvlr.x, uvlr.y)


def main():
	UniVariateLinearRegression.run()

if __name__ == '__main__':
	main()
