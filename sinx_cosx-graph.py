import matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)  # use full 0..4π
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, x, z)
plt.xlabel('x values from 0 to 4*pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin(x) and cos(x) from 0 to 4π')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
plt.savefig('sinx_cosx_graph.png')  # save the figure to a file
