import signal
from base import Base

class MultiVariateLinearRegression(Base):

    def __init__(self):
        self.cc = 0
        self.x = []
        self.y = []
        self.w = [5]
        self.alpha = 0.000001
        self.filename = 'multivariate_data-train.csv'
        self.convergenceCondition = 1e-6
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

    def findLine(self):
        ''' Find the line given the points loaded from csv file.
        '''
        self.w = self.w * len(self.x[0])
        hasConverged = False
        cc = 0
        while(hasConverged == False):    #convergence test
            hasConverged = True
#         while(cc < 1000000):
            for i in xrange(len(self.w)):
                curW = self.w[i] + (self.alpha * self.summ(i))
                if(abs(curW - self.w[i]) > self.convergenceCondition):
                    hasConverged = False
                self.w[i] = curW

            if(cc % 100000 == 0):
                print self.w
                print cc
            cc+=1
        print 'total iterations:',cc
        return self.w

    @classmethod
    def run(cls, mvlr=None):
        if(mvlr == None):
            mvlr = MultiVariateLinearRegression()
        mvlr.loadCSVFile('multivariate_data-train.csv')
#         mvlr.loadCSVFile('univariate_data-train.csv')
#         mvlr.loadCSVFile('test1.csv')
#         mvlr.loadCSVFile('test.csv')
#         mvlr.printValues()
#         ws = [-1]
        ws = mvlr.findLine()
        return ws

smvlr = None

def handler(signum, frame):
    print smvlr.w

def main():
    smvlr = MultiVariateLinearRegression()
    print MultiVariateLinearRegression.run(smvlr)
    print 'done'

signal.signal(signal.CTRL_C_EVENT, handler)  #windows only


main()