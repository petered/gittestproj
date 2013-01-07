
from numpy import array
from matplotlib import pyplot

class ClassyTime:
    x=array(range(0,99));
    
    def plotme(self):
        pyplot.plot(self.x^2)
