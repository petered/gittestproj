
import classyfile


from matplotlib import *


reload(classyfile)


print 'start script running'

obj=classyfile.ClassyTime();

figure()


obj.plotme();