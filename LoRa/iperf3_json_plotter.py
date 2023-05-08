import json
import matplotlib.pyplot as plt
import numpy as np

import sys

n = len(sys.argv)
if n < 2:
    print("Please provide a file")
    sys.exit(1)
if n > 2:
    print("To many command line parameters")
    sys.exit(1)


# extra the data from the json file

try:
    fp = open(sys.argv[1], "r")
    iperf = json.load(fp)
    data_points = []
    for interval in iperf["intervals"]:
        data_points.append(interval["sum"]["bits_per_second"])
    print("got the data points")
    # create the plot
    time_stamps = np.arange(1,int(iperf["end"]["sum_sent"]["seconds"])+1)
    print("got the timestamps")
    print(len(data_points),len(time_stamps))
    plt.plot(time_stamps,np.array(data_points)/1000000)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Mbps")
    plt.ylim((0,40))
    plt.show()
    print(time_stamps)
except:
    print("Something went wrong")
    sys.exit(1)