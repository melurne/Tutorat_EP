import matplotlib.pyplot as plt

with open("redresseur.txt", 'r') as f:
    lines = f.readlines()
    headerLine = lines[0]
    raw = lines[1:]

headers = [head for head in headerLine.split(" ") if head != "" and head != "\n"]
data = {key: [] for key in headers}

print(headers)

for line in raw:
    points = [float(point.split("E")[0]) * 10**(int(point.split("E")[1])) for point in line.split(" ") if point != "" and point != "\n"]
    for key, point in zip(headers, points):
        data[key].append(point)
print(data["Time"])

plt.plot([t for t in data["Time"] if t < 5], [V for i, V in enumerate(data["VP1"]) if data["Time"][i] < 5], "r", label="Tension redressée")
plt.plot([t for t in data["Time"] if t < 5], [320 for t in [t for t in data["Time"] if t < 5]], 'b--', label="Tension recherchée")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.legend(loc="best")
plt.show()

with open("commande_charge.txt", 'r') as f:
    lines = f.readlines()
    headerLine = lines[0]
    raw = lines[1:]

headers = [head for head in headerLine.split(" ") if head != "" and head != "\n"]
data = {key: [] for key in headers}

print(headers)

for line in raw:
    points = [float(point.split("E")[0]) * 10**(int(point.split("E")[1])) for point in line.split(" ") if point != "" and point != "\n"]
    for key, point in zip(headers, points):
        data[key].append(point)

plt.plot([t for t in data["Time"] if t < 10000], [V for i, V in enumerate(data["Vbat"]) if data["Time"][i] < 10000], "r", label="Tension batterie")
plt.plot([t for t in data["Time"] if t < 10000], [V for i, V in enumerate(data["Ibat"]) if data["Time"][i] < 10000], "b", label="Courant batterie")
#plt.plot([t for t in data["Time"] if t < 10000], [320 for t in [t for t in data["Time"] if t < 10000]], 'g--', label="Tension recherchée")
#plt.plot([t for t in data["Time"] if t < 10000], [200 for t in [t for t in data["Time"] if t < 10000]], 'k--', label="Courant limite")
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)\nCourant (A)")
plt.legend(loc="right")
plt.show()

plt.plot([t for t in data["Time"] if t < 10000], [V for i, V in enumerate(data["Vbat"]) if data["Time"][i] < 10000], "g--", label="Tension batterie")
plt.plot([t for t in data["Time"] if t < 10000], [V for i, V in enumerate(data["K1"]) if data["Time"][i] < 10000], "r", label="K1")
plt.plot([t for t in data["Time"] if t < 10000], [V for i, V in enumerate(data["K2"]) if data["Time"][i] < 10000], "b", label="K2")
plt.xlabel("Temps (s)")
plt.ylabel("Activation")
plt.legend(loc="right")
plt.show()
