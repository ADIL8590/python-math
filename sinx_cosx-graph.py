import numpy as np
from matplotlib import pyplot as plt

"""x=np.arange(0, 4*np.pi, 0.1)
y=np.cos(x)
plt.plot(x,y)
plt.show()"""

x=np.arange(0, 4*np.pi-1, 0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4*pi')
plt.ylabel('sin(x) and cos (x) ')
plt.title(' Plot of sin(x) and cos(x) from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()


plt.show()
