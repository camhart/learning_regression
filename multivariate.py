import signal, math
from base import Base

class MultiVariateLinearRegression(Base):

    def __init__(self):
        self.cc = 0
        self.x = []
        self.y = []
        self.w = [5]
        self.alpha = 0.000001
        self.filename = 'multivariate_data-train.csv'
        self.convergenceCondition = 1e-14
        self.ysum = None

    def loadCSVFile(self, filename=None):
        Base.loadCSVFile(self, filename=filename)
        for c in xrange(len(self.x)):
            self.x[c].insert(0, 1)

    def h(self, j):
        nlist = [self.w[i]*self.x[j][i] for i in xrange(len(self.w))]
        return sum(nlist)

    def summ(self, index):
        nlist = [self.x[j][index] * (self.y[j]-self.h(j)) for j in xrange(len(self.y))]
        return sum(nlist)

    def MSE(self):
        '''
        calculate the mean square error
        '''
        nlist = [ math.pow(self.y[i] - self.h(i), 2) for i in xrange(len(self.y))]
        self.msex.append(self.cc)
        self.msey.append(sum(nlist))

    def findLine(self):
        ''' Find the line given the points loaded from csv file.
        '''
        self.msex = []  #iteration count (x var on plot)
        self.msey = []  #mse (y variable on plot)

        self.w = self.w * len(self.x[0])
        hasConverged = False
        self.cc = 0
        while(hasConverged == False):    #convergence test
            hasConverged = True
            for i in xrange(len(self.w)):
                curW = self.w[i] + (self.alpha * self.summ(i))
                if(abs(curW - self.w[i]) > self.convergenceCondition):
                    hasConverged = False
                self.w[i] = curW
            if(self.cc % 10000 == 0):
                self.MSE()
            self.cc+=1
        print 'total iterations:',cc
        print 'mse:',self.mse
        return self.w

    @classmethod
    def run(cls, mvlr=None):
        if(mvlr == None):
            mvlr = MultiVariateLinearRegression()
        mvlr.loadCSVFile('multivariate_data-train.csv')
#         mvlr.loadCSVFile('univariate_data-train.csv')
        ws = mvlr.findLine()
        return ws

def main():
    smvlr = MultiVariateLinearRegression()

    def handler(signum, frame):
        print smvlr.w
        print 'iterations:',smvlr.cc
        print 'msex', smvlr.msex
        print 'msey', smvlr.msey

    print 'type ctrl+break or ctrl+pause to print current w and iteration count'
    # register ctrl+break to print values
    signal.signal(signal.SIGBREAK, handler)  #windows only

    print MultiVariateLinearRegression.run(smvlr)
    print 'done'

main()