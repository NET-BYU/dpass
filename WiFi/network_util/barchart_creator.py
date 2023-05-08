import json
import matplotlib.pyplot as plt
import numpy as np

import sys

# n = len(sys.argv)
# if n < 2:
#     print("Please provide a file")
#     sys.exit(1)
# if n > 2:
#     print("To many command line parameters")
#     sys.exit(1)

# t = ["1","10","25", "u"]
t = ["u","25","10"]
# x_names = ["1Mbps","10Mbps","25Mbps", "Unlimited"]
x_names=["Unlimited","25Mbps","10Mbps"]
def create_bench_name(number, throughput):
    return "utilization_b_"+str(number)+"_"+throughput+".json"
def create_name(number,throughput):
    return "utilization_"+str(number)+"_"+throughput+".json"
# extra the data from the json file
throughput_mean = []
throughput_std = []

try:
    for thr in t:
        data_points = []
        data_points2 = []
        for i in range(5):
            with open(create_name(i,thr),"r") as norm, open(create_bench_name(i,thr),"r") as bench:

    # fp = open(sys.argv[1], "r")
                iperf_norm = json.load(norm)
                
                for interval in iperf_norm["intervals"]:
                    data_points.append(interval["sum"]["bits_per_second"])
                iperf_bench = json.load(bench)
                
                for interval in iperf_bench["intervals"]:
                    data_points2.append(interval["sum"]["bits_per_second"])
        throughput_mean.append([np.average(data_points)/1000000,np.average(data_points2)/1000000])
        throughput_std.append([np.std(data_points)/1000000,np.std(data_points2)/1000000])
                # print("got the data points")

    print(throughput_mean)
    print(throughput_std)
    # # create the plot
    # time_stamps = np.arange(1,int(iperf["end"]["sum_sent"]["seconds"])+1,.25)
    # print("got the timestamps")
    # print(len(data_points),len(time_stamps))
    # print("points that are zero:",data_points.count(0),"->",data_points.count(0)*.25)
    x_axis = np.arange(len(x_names))
    throughput_mean = np.array(throughput_mean)
    throughput_std = np.array(throughput_std)
    fig, ax = plt.subplots()
    plt.bar(x_axis -0.2, throughput_mean[:,1], yerr=throughput_std[:,1],ecolor="black",width=0.4, label="Benchmark",capsize=10)
    plt.bar(x_axis +0.2, throughput_mean[:,0], yerr=throughput_std[:,0],ecolor="black",width=0.4, label = 'DPASS present',capsize=10)
    # Xticks

    plt.xticks(x_axis, x_names)
    plt.legend()
    plt.ylabel("Throughput (Mbps)")
    plt.xlabel("Throughput Limits")
    # plt.plot(time_stamps,np.array(data_points)/1000000)
    # plt.xlabel("Time (seconds)")
    # plt.ylabel("Throughput( Mbps)")
    # plt.ylim((0,250))
    # plt.xlim((0,60))
    # plt.grid()
    plt.tight_layout()
    plt.show()
    # print(time_stamps)
except Exception as e:
    print(e)
    print("Something went wrong")
    sys.exit(1)