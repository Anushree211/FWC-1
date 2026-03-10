import numpy as np
import matplotlib.pyplot as plt

# Inputs
A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

# Outputs
Qa = (A ^ B) & (1 - B)
Qb = A & (1 - B)
Qc = A
Qd = (1 - A) | B

print("A B | Qa Qb Qc Qd")
print("------------------")

for i in range(4):
    print(A[i], B[i], "|", Qa[i], Qb[i], Qc[i], Qd[i])

x = np.arange(4)

plt.step(x, Qa, where='mid', label="Qa")
plt.step(x, Qb, where='mid', label="Qb")
plt.step(x, Qc, where='mid', label="Qc")
plt.step(x, Qd, where='mid', label="Qd")

plt.xticks(x, ["00","01","10","11"])
plt.xlabel("Inputs (A B)")
plt.ylabel("Output")
plt.title("Logic Outputs Graph")
plt.ylim(-0.2,1.2)

plt.legend()
plt.grid(True)

plt.show()
