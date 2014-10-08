class Base(object):

    def loadCSVFile(self, filename=None):
        if filename is None or filename is '':
            filename = self.filename
        everything = []
        with open(filename) as f:
            for line in f.readlines():
                splitUp = line.split(',')
                self.y.append(float(splitUp[-1]))
                self.x.append([float(val) for val in splitUp[0:-1]])
                everything.extend([float(val) for val in splitUp[0:-1]])
        self.w[0] = sum(everything) / len(everything)


    def printValues(self):
        stri = ''
        for c in xrange(len(self.y)):
            for cc in xrange(len(self.x[c])):
                stri += str(self.x[c][cc])
                stri += ','
            stri += str(self.y[c])
            stri += '\n'
        print stri