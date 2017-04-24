import matplotlib.pyplot as plt
import numpy as np

import time

f = plt.figure()
ax = f.gca()
f.show()

for i in range(10):
    ax.plot(i, i, 'ko')
    f.canvas.draw()
    print "drawn "+str(i)
    time.sleep(2)
    # raw_input('pause : press any key...')
# f.close()
