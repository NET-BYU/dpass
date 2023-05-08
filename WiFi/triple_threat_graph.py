import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("triple_threat_data.csv", dtype=float, delimiter=',', names=True)
# print(data.dtype.names)
time_stamps = data["Time_seconds"]

# params = {
#    'axes.labelsize': 15,
#    'font.size': 8,
#    'legend.fontsize': 15,
#    'xtick.labelsize': 13,
#    'ytick.labelsize': 13,
#    'text.usetex': False,
#    'figure.figsize': [10, 6]
#    }
# plt.rcParams.update(params)
# plt.figure(figsize=(5,3))
plt.axvspan(45.7,48.7,color="red",alpha=0.25)
# plt.vlines(45.7,0,4,linestyles="dashed",label="915MHz UPSS", colors="red")
# plt.vlines(60,0,4,linestyles="dashed",label="2.4GHz UPSS", colors="black")
plt.axvspan(60,63,color="black",alpha=0.25)
plt.text(34.75,3.5,"915MHz DPASS Packet",fontsize="large")
plt.text(49.8,3.25,"2.4GHz DPASS Packet",fontsize="large")
plt.plot(time_stamps,np.where(data["WiFi"]==1,3,0),label="Wifi")
plt.plot(time_stamps,np.where(data["LoRa"]==1,2,0),label="LoRa")
plt.plot(time_stamps,data["LTE"],label="LTE")
plt.xlabel("Time (seconds)")
plt.ylabel("Connection")
plt.ylim((0,4))
plt.yticks(np.arange(1,4),["LTE","LoRa","WiFi"])
plt.xlim((0,120))
# plt.grid()
plt.legend( loc='upper right', borderaxespad=0.)
# plt.legend()
plt.tight_layout()
plt.show()