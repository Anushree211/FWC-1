
A = [0,0,1,1]
B = [0,1,0,1]

print("A B | Qa Qb Qc Qd")

for i in range(4):

    a = A[i]
    b = B[i]

    Qa = (a ^ b) & (1-b)
    Qb = a & (1-b)
    Qc = a
    Qd = (1-a) | b

    print(a, b, "|", Qa, Qb, Qc, Qd)
