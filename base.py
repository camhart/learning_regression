class Base(object):

    def loadCSVFile(self, filename=None):
        if filename is None or filename is '':
            filename = self.filename

        with open(filename) as f:
            for line in f.readlines():
                splitUp = line.split(',')
                self.y.append(float(splitUp[-1]))
                self.x.append([float(val) for val in splitUp[0:-1]])

    def printValues(self):
        stri = ''
        for c in xrange(len(self.y)):
            for cc in xrange(len(self.x[c])):
                stri += str(self.x[c][cc])
                stri += ','
            stri += str(self.y[c])
            stri += '\n'
        print stri