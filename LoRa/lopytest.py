import numpy as np
import time as t
from scipy.signal import max_len_seq
import serial

class dynamic_decoder:
    def __init__(self, samples_per_chip=1):
        self.values = []
        self.bits = [0]
        six_stage = [[5], [1], [5, 4, 1], [5, 2, 1], [5, 3, 2], [4, 3, 1]]

        seq = []

        for tap in six_stage:
            msg = max_len_seq(6, taps=tap)[0]
            interpolated_msg = []
            for chip in msg:
                for i in range(samples_per_chip):
                    if chip == 0:
                        interpolated_msg.append(chip)
                    else:
                        interpolated_msg.append(2)
            seq.append(interpolated_msg)
        
        self.message_array = np.array(seq)
        self.intp_val = samples_per_chip
        self.max_len = len(self.message_array[0])
        self.data_array = []
        self.transformed_data = []
        self.the_symbol = [None, 0, 0, False]
        self.the_sample = 0

        self.mean = -100
        self.standard_deviation = 2

        self.abs_max = -100

    def add_val(self, new_data, sample=''):
        if new_data > self.abs_max:
            self.abs_max = new_data
        self.mean = (new_data + self.mean * (self.max_len - 1)) / self.max_len
        self.data_array.append(new_data)
        if len(self.data_array) > self.max_len:
            self.data_array.pop(0)
            d_ra = np.array(self.data_array)
            min_data = np.min(d_ra)
            self.transformed_data = (d_ra - self.mean) / (np.max(d_ra) - min_data)
            corr_data = []
            for msg in self.message_array:
                corr_data.append(np.correlate(msg - np.ones(self.max_len), self.transformed_data)[0])
            curr_max = np.argmax(np.abs(corr_data))
            if np.abs(corr_data[curr_max]) > np.abs(self.the_symbol[1]):
                if corr_data[curr_max] > 0:
                    is_pos = True
                    self.the_symbol = [curr_max, corr_data[curr_max], sample, is_pos]
                else:
                    is_pos = False
                    self.the_symbol = [curr_max + len(self.message_array), corr_data[curr_max], sample, is_pos]
            if sample > (self.the_sample + self.max_len):
                self.the_sample = sample
                if np.abs(self.the_symbol[1]) > 8 * self.intp_val:
                    x = self.the_symbol
                    print(self.the_symbol)
                    self.the_symbol = [None, 0, 0, True]
                    self.the_sample = sample
                    return x
                self.the_symbol = [None, 0, 0, True]
            return None

# if __name__ == "__main__":
#     decoder = dynamic_decoder(samples_per_chip=2)
#     # d1 = dynamic_decoder(samples_per_chip=2)

#     # f = open("./loratestfullsystembuffertest-100dBm.txt", 'w')

#     ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200)
#     # s1 = serial.Serial(port='/dev/ttyACM1', baudrate=115200)

#     durations = [0.5, 1, 2, 3, 4, 5, 6, 8, 12, 24]

#     PILOT_SYMBOL = 11

#     symbols = []
#     symbol1s = []
#     samples = []
#     sample1s = []
#     sample_num = 0
#     sample1_num = 0

#     lora_sleep = False

#     sleep_time = 0.5

#     last_symbol_time = t.time()
#     last_symbol1_time = t.time()

#     while True:
#         while not lora_sleep:
#             line = ser.readline()
#             # l1 = s1.readline()
#             try:
#                 line = line.decode()
#                 # l1 = l1.decode()
#                 if (len(line) > 10):
#                     print(line)
#                 # if (len(l1) > 10):
#                 #     print(l1)
#                 else:
#                     val = int(line)
#                     # v1 = int(l1)

#                     # if val > -10:
#                     #     continue
#                     # if v1 > -10:
#                     #     continue

#                     samples.append(val)
#                     # sample1s.append(v1)

#                     sample_num += 1
#                     sample1_num += 1

#                     # f.write("%f\n" % val)
#                     symbol = decoder.add_val(val, sample_num)
#                     # symbol1 = d1.add_val(v1, sample1_num)

#                     if symbol is not None:
#                         if symbol[0] is not None:
#                             if t.time() - last_symbol_time > 20:
#                                 symbols.clear()
#                                 print("Clearing received symbols")
#                             symbols.append(symbol[0])
#                             print("Appending " + str(symbol))
#                             print(decoder.abs_max)
#                             if len(symbols) > 2:
#                                 if symbols[-3] == PILOT_SYMBOL and symbols[-2] == PILOT_SYMBOL:
#                                     sleep_time = durations[symbols[-1]] * 3600 / 100
#                                     # ser.write(str(symbol[0]).encode('utf-8'))
#                                     ser.write("lora.power_mode(LoRa.SLEEP)\r\n".encode('utf-8'))
#                                     print("Going to sleep for " + str(sleep_time) + " seconds")
#                                     lora_sleep = True
#                                     symbols.clear()
#                             last_symbol_time = t.time()

#                     # if symbol1 is not None:
#                     #     if symbol1[0] is not None:
#                     #         if t.time() - last_symbol1_time > 20:
#                     #             symbol1s.clear()
#                     #             print("Clearing received 1 symbols")
#                     #         symbol1s.append(symbol[0])
#                     #         print("Appending " + str(symbol1))
#                     #         print(d1.abs_max)
#                     #         if len(symbol1s) > 2:
#                     #             if symbol1s[-3] == PILOT_SYMBOL and symbol1s[-2] == PILOT_SYMBOL:
#                     #                 sleep_time = durations[symbol1s[-1]] * 3600 / 100
#                     #                 # ser.write(str(symbol[0]).encode('utf-8'))
#                     #                 s1.write("lora.power_mode(LoRa.SLEEP)\r\n".encode('utf-8'))
#                     #                 print("Going to sleep for " + str(sleep_time) + " seconds")
#                     #                 lora_sleep = True
#                     #                 symbol1s.clear()
#                     #         last_symbol1_time = t.time()

#             except:
#                 # print("Error detected. Passing")
#                 print(line[:-2])

#         if t.time() > last_symbol_time + sleep_time:
#             ser.write("lora.power_mode(LoRa.ALWAYS_ON)\r\n".encode('utf-8'))
#             print("Returning to activity")
#             lora_sleep = False
#         else:
#             ser.readline()



if __name__ == "__main__":
    decoder = dynamic_decoder(samples_per_chip=5)

    # f = np.fromfile(open("./onpc_remake_live/rx_test_5801_long.f32"), dtype=np.float32)
    myfile = open("./lorasystemtest2_4_5ms.txt", 'r')

    colors = {
            "0": "red",
            "1": "orange",
            "2": "green",
            "3": "blue",
            "4": "purple",
            "5": "pink",
            "6": "maroon",
            "7": "sandybrown",
            "8": "lime",
            "9": "navy",
            "10": "violet",
            "11": "deeppink",
        }
    colors_reversed = {
            "red": "0",
            "orange": "1",
            "green": "2",
            "blue": "3",
            "purple": "4",
            "pink": "5",
            "maroon": "-0",
            "sandybrown": "-1",
            "lime": "-2",
            "navy": "-3",
            "violet": "-4",
            "deeppink": "-5",
        }

    # # print(len(f))
    symbols = []
    num_symbols = 0
    location = []
    stt = t.time()
    samples = []
    start_samp = 000
    for element in myfile.readlines():
        element = float(element[0:6])
        if element > -10:
            element = -100
        if element < -157:
            element = -100
        samples.append(element)
        if len(samples) > start_samp:
            try:
                symbol = decoder.add_val(element, sample=len(samples[start_samp:]))
                symbols.append(symbol)
                if symbol is not None:
                    if symbol[0] is not None:
                        num_symbols += 1
                        location.append(
                            [
                                (
                                    len(samples[start_samp:]) - 63 * decoder.intp_val,
                                    len(samples[start_samp:]),
                                ),
                                (-80, -80),
                                colors[str(symbol[0])],
                            ]
                        )
                # samples.append(float(element[0:6]))
            except:
                print("Error")
    end = t.time()
    print(end - stt)
    print(str(len(samples)) + " samples")
    print(str(num_symbols) + " symbols")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    graphs = [plt.scatter(np.arange(0, len(samples[start_samp:])), samples[start_samp:], s=1)]
    graph_names = ['']

    for line in location:
        graphs.append(
            plt.arrow(
                line[0][0],
                int(np.average([min(samples[start_samp:]), max(samples[start_samp:])])),
                63 * decoder.intp_val,
                0,
                color=line[2],
                width=1,
                length_includes_head=True,
            )
        )
        graph_names.append(colors_reversed[line[2]])
    plt.title("Symbols found in transmision")
    plt.xlabel("Sample number")
    plt.ylabel("Channel power measurment")
    graph_names, indexes = np.unique(graph_names,return_index=True)
    plt.legend(np.array(graphs)[indexes], graph_names, loc="upper right", bbox_to_anchor=(1, 1))
    plt.show()

    # sample_rate = 1000
    # plt.plot([i / sample_rate for i in range(len(symbols))], samples, 'k-')
    # f = samples

    # for i in range(len(symbols)):
    #     if symbols[i] is not None:
    #         if symbols[i][0] is not None:
    #             if symbols[i][0] == 0:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'p', color='tab:blue', markersize=8)
    #             elif symbols[i][0] == 1:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], '^', color='tab:orange', markersize=8)
    #             elif symbols[i][0] == 2:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'o', color='tab:green', markersize=8)
    #             elif symbols[i][0] == 3:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'X', color='tab:red', markersize=8)
    #             elif symbols[i][0] == 4:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'P', color='tab:purple', markersize=8)
    #             elif symbols[i][0] == 5:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'd', color='tab:olive', markersize=8)
    #             elif symbols[i][0] == 6:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'd', color='tab:blue', markersize=8)
    #             elif symbols[i][0] == 7:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'P', color='tab:orange', markersize=8)
    #             elif symbols[i][0] == 8:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'X', color='tab:green', markersize=8)
    #             elif symbols[i][0] == 9:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'o', color='tab:red', markersize=8)
    #             elif symbols[i][0] == 10:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], '^', color='tab:purple', markersize=8)
    #             elif symbols[i][0] == 11:
    #                 plt.plot(symbols[i][2] / sample_rate, f[symbols[i][2]], 'p', color='tab:olive', markersize=8)

    # plt.ylabel('Signal Strength Indicator')
    # # plt.ylim(ymax=-50, ymin=-120)
    # plt.xlabel('Time (s)')
    # plt.show()