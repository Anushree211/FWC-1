import numpy as np
import matplotlib.pyplot as plt

# Inputs
A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

# Outputs
Q1 = A * (1-B)      # A B̅
Q2 = (1-A) + B      # A̅ + B

# Limit output to 0 or 1
Q2 = np.clip(Q2,0,1)

x = np.arange(4)

plt.plot(x,Q1,'o-',label='A B̅')
plt.plot(x,Q2,'s-',label='A̅ + B')

plt.xticks(x,['00','01','10','11'])
plt.xlabel('Inputs (A,B)')
plt.ylabel('Output')
plt.title('Logic Output Comparison')
plt.grid()
plt.legend()

plt.savefig('graph.jpg')
plt.show()

