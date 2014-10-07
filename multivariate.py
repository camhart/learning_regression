import math
from base import Base

class MultiVariateLinearRegression(Base):

    def __init__(self):
        self.cc = 0
        self.x = []
        self.y = []
        self.w = [2]
        self.alpha = 0.001
        self.filename = 'multivariate_data-train.csv'
        self.returnCondition = 10e-6
        self.ysum = None

#     def h(self, index1, index2):#         self.cc+=1
#         print self.cc
#         return self.w[index2] * self.x[index1][index2]
    def h(self, index):
        sum = 0
        for i in xrange(len(self.w)):
            sum+= self.w[i]*self.x[index][i]
        return sum

    def isConverged(self):
        max = 0
        for i in xrange(len(self.y)):
            xs = self.x[i]
            sum = 0
            for j in xrange(len(xs)):
                sum += xs[j] * self.w[j]
            if(abs(self.y[i] - sum) > self.returnCondition):
                return False

#             if(abs(self.y[i] - sum) > max):
#                 max = abs(self.y[i] - sum)
        return True

    def findLine(self):

        for c in xrange(len(self.x)):
            self.x[c].insert(0, 1)

        self.w = self.w * len(self.x[0])

        dist = float('inf')

        while(self.isConverged() == False):    #convergence test
            for i in xrange(len(self.w)):
                summ = 0
                h = 0
                for j in xrange(len(self.y)):
                    h = self.h(j)
                    summ += self.x[j][i] * (self.y[j]-h)
                self.w[i] = self.w[i] + self.alpha * summ

        return self.w

    def printValues(self):
        stri = ''
        for c in xrange(len(self.y)):
            for cc in xrange(len(self.x[c])):
                stri += str(self.x[c][cc])
                stri += ','
            stri += str(self.y[c])
            stri += '\n'
        print stri

    @classmethod
    def run(cls):
        mvlr = MultiVariateLinearRegression()
        mvlr.loadCSVFile('multivariate_data-train.csv')
        mvlr.printValues()
        ws = [-1]
#         ws = mvlr.findLine()
        return ws