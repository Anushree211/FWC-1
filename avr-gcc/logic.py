import numpy as np
import matplotlib.pyplot as plt

A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

AND  = A & B
OR   = A | B
NOTA = 1 - A
XOR  = A ^ B
XNOR = 1 - XOR
NAND = 1 - (A & B)

print("A B AND OR NOT XOR XNOR NAND")

for i in range(4):
    print(A[i],B[i],AND[i],OR[i],NOTA[i],XOR[i],XNOR[i],NAND[i])

x = np.arange(4)

plt.plot(x,AND,label="AND")
plt.plot(x,OR,label="OR")
plt.plot(x,XOR,label="XOR")
plt.plot(x,NAND,label="NAND")

plt.xlabel("Input")
plt.ylabel("Output")
plt.legend()
plt.grid()
plt.show()
