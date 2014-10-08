import matplotlib.pyplot

from base import Base

class UniVariateLinearRegression(Base):

    def __init__(self):
        self.x = []
        self.y = []
        self.w = [2]
        self.alpha = 0.001
        self.filename = 'univariate_data-train.csv'
        self.convergenceCondition = 0.0000001

    # def h(self):
    #     return 1.0 *

    # def findLine(self):
    #     self.w = self.w * len(self.x)
    #     print self.w

    #     maxDistance = float('inf')

    #     while maxDistance > self.convergenceCondition:    #convergence test
    #         for c in xrange(len(self.w)):
    #             w = self.w[c]

    #             w = w - self.alpha

    #     return self.w

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
            print self.x[c], ',', self.y[c]
        print stri

    @classmethod
    def run(cls):
        uvlr = UniVariateLinearRegression()
        uvlr.filename = 'univariate_data-test.csv'
        uvlr.loadCSVFile()
        uvlr.x = [item for sublist in uvlr.x for item in sublist]
        ws = uvlr.findLine()
        matplotlib.pyplot.scatter(uvlr.x, uvlr.y)
        linex = uvlr.x
        linex.extend([0, max(uvlr.y)])
        line = [uvlr.w[0]+uvlr.w[1]*myx for myx in linex]
        matplotlib.pyplot.plot(uvlr.x, line)
        matplotlib.pyplot.ylabel("y")
        matplotlib.pyplot.xlabel("x")
        matplotlib.pyplot.xlim(-1, 9)
        matplotlib.pyplot.ylim(0, 15)
        matplotlib.pyplot.savefig("univariate_%s.png" % (uvlr.filename, ))
#         uvlr.printValues()
        return ws

print UniVariateLinearRegression.run()