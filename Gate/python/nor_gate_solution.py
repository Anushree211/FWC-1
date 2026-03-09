import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

P = np.array([0,0,0,0,1,1,1,1])
Q = np.array([0,0,1,1,0,0,1,1])
R = np.array([0,1,0,1,0,1,0,1])

F = 1 - np.clip(P + Q + R,0,1)

table = pd.DataFrame({
    'P':P,
    'Q':Q,
    'R':R,
    'F':F
})

print("\nTruth Table\n")
print(table)

x = np.arange(len(F))

plt.step(x,F,where='mid')
plt.xlabel("Input Combination")
plt.ylabel("Output F")
plt.title("NOR Logic Output")
plt.grid()

plt.show()
