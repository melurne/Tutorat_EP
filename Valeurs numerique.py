import math
# Modele batterie
# E = 1/2 * C * V²
V = 320  # V
E = 115_200  # kJ = 32 kwh = 100Ah
# =>
C = (2 * E) / V**2  # = 2250 F

# Redresseur
f = 20
Cr = 1e-3
Lr = 1 / ((2 * f * math.pi)**2 * Cr)
fc = 1 / (2 * math.pi * math.sqrt(Lr * Cr))
# print(Lr)
# print(fc)


# Hasheur boost
Vs = 320
Ve = 230
# on veut DV = 0.1% de 320 V
DV = Vs * 0.001

Is = 200  # A
# on veut DI = 0.1% de 200 A
DI = Is * 0.001

fhash = 500  # Hz
T = 1 / fhash
alpha = 1 - Ve / Vs  # ~ 0.28
#alpha = 31 / 360
Lboost = (Vs - Ve) / (DI / ((1 - alpha) * T))  # ~ 0.647
Cboost = (Is * alpha * T) / DV  # ~ 0.35

print(Lboost)
print(Cboost)
