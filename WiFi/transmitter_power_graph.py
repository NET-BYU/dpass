import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("B200_mini_power.csv", dtype=float, delimiter=',', names=True)
# print(data)
plt.figure(figsize=(5,3))
for graph in data.dtype.names[1:]:
    if graph == '22db':
        continue
    plt.plot(data["FrequencyMHZ"], data[graph]+10, marker="o", label=graph,markersize=1)
    plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)

# plt.title("B210 Mini Transmit Power Spread")

plt.ylabel("Power in dBm")
plt.xlabel("Frequency in MHz")
plt.xlim((0,6000))
plt.xticks(np.arange(0,6000,500))
plt.xticks(rotation = -45)
plt.yticks(np.arange(-50,20,5))
plt.grid()
plt.tight_layout()
plt.show()
