import matplotlib.pyplot as plt

X, Y = [], []
for line in open("graphdata.txt", 'r'):
    values = [float(s) for s in line.split()]
    X.append(values[0])
    Y.append(values[1])

plt.plot(Y, X)
plt.title("Execution Time")
plt.xlabel("Run Count")
plt.ylabel("Time(s)")
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.show()