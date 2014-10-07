class Base(object):

    def loadCSVFile(self, filename=None):
        if filename is None or filename is '':
            filename = self.filename

        with open(filename) as f:
            for line in f.readlines():
                splitUp = line.split(',')
                self.y.append(float(splitUp[-1]))
                self.x.append([float(val) for val in splitUp[0:-1]])