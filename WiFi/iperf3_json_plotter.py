from cProfile import label
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
    time_stamps = np.arange(1,int(iperf["end"]["sum_sent"]["seconds"])+1,.25)
    print("got the timestamps")
    print(len(data_points),len(time_stamps))
    print("points that are zero:",data_points.count(0),"->",data_points.count(0))
    # plt.figure(figsize=(5,3))
    # plt.vlines(26,0,250,linestyles="dashed",label="UPSS", colors="red")
    plt.axvspan(26,29,color="red",alpha=0.25)
    plt.plot(time_stamps,np.array(data_points)/1000000,label="Throughput")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Throughput (Mbps)")
    plt.ylim((0,250))
    plt.xlim((0,60))
    plt.text(22,220,"DPASS Packet",fontsize="large")
    plt.grid()
    # plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', borderaxespad=0.)
    # plt.legend()
    plt.tight_layout()
    plt.show()
    # print(time_stamps)
except:
    print("Something went wrong")
    sys.exit(1)