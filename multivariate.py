from base import Base

class MultiVariateLinearRegression(Base):

    def __init__(self):
        self.cc = 0
        self.x = []
        self.y = []
        self.w = [5]
        self.alpha = 0.001
        self.filename = 'multivariate_data-train.csv'
        self.convergenceCondition = 10e-6
        self.ysum = None

    def loadCSVFile(self, filename=None):
        Base.loadCSVFile(self, filename=filename)
        for c in xrange(len(self.x)):
            self.x[c].insert(0, 1)

    def h(self, index):
        ssum = 0
        for i in xrange(len(self.w)):
            ssum+= self.w[i]*self.x[index][i]
        return ssum

    def summ(self, index):
        summ = 0
        for j in xrange(len(self.y)):
            summ += self.x[j][index] * (self.y[j]-self.h(j))
#             summ += (self.y[j]-self.h(j))
        return summ

    def findLine(self):

        self.w = self.w * len(self.x[0])

        hasConverged = False
        while(hasConverged == False):    #convergence test
            hasConverged = True
            for i in xrange(len(self.w)):
#                 print 'grew:[',i,'] ',(self.alpha * self.summ(i))
                curW = self.w[i] + (self.alpha * self.summ(i))
                if(abs(curW - self.w[i]) > self.convergenceCondition):
                    hasConverged = False
                self.w[i] = curW
            print self.w

        return self.w

    @classmethod
    def run(cls):
        mvlr = MultiVariateLinearRegression()
#         mvlr.loadCSVFile('multivariate_data-train.csv')
#         mvlr.loadCSVFile('univariate_data-train.csv')
        mvlr.loadCSVFile('test.csv')
#         mvlr.printValues()
#         ws = [-1]
        ws = mvlr.findLine()
        return ws