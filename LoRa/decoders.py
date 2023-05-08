import numpy as np
import time as t
from scipy.signal import max_len_seq


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
                    interpolated_msg.append(chip)
            seq.append(interpolated_msg)

        self.message_array = np.array(seq)
        self.intp_val = samples_per_chip
        self.max_len = len(self.message_array[0])
        self.data_array = []
        self.transformed_data = []

        self.mean = -80
        self.standard_deviation = 2
        self.threshold = 9*samples_per_chip*.6
        self.count = 0

    def saturate(self, val, mid, max_diff):
        if val < mid - max_diff:
            return mid - max_diff
        elif val > mid + max_diff:
            return mid + max_diff
        else:
            return val

    def add_val(self, new_data, sample=""):
        self.count += 1
        # new_data = self.saturate(new_data, -85, 30)
        self.mean = (new_data + self.mean * (self.max_len - 1)) / (self.max_len)
        # self.standard_deviation = (abs(new_data - self.mean) + self.standard_deviation * (self.max_len - 1)) / (self.max_len * 2)
        self.data_array.append(new_data)
        if len(self.data_array) > self.max_len:
            self.data_array.pop(0)
            min_data = np.min(self.data_array)
            d_ra = np.array(self.data_array)
            self.transformed_data = (d_ra - self.mean) / (
                np.max(self.data_array) - min_data
            )
            corr_data = []
            for msg in self.message_array:
                corr_data.append(
                    np.correlate(
                        msg - 0.5 * np.ones(self.max_len), self.transformed_data
                    )[0]
                )
            if np.max(np.abs(corr_data)) > 2.9 * np.mean(np.abs(corr_data)):
                if np.max(corr_data) > self.threshold:
                    print(str(np.argmax(corr_data)) + " at " + str(max(corr_data)) + " space: " + str(self.count))
                    # print(corr_data)
                    # print(self.transformed_data)
                    # return [str(np.argmax(corr_data)), sample]
                    self.count = 0
                    return str(np.argmax(corr_data))
                elif np.abs(np.min(corr_data)) > self.threshold:
                    print(
                        " - " + str(np.argmin(corr_data)) + " at " + str(min(corr_data))+" space: " +  str(self.count))
                    
                    # print(corr_data)
                    # print(self.transformed_data)
                    # return [np.argmin(corr_data) + len(self.message_array), sample]
                    self.count = 0
                    return "-" + str(np.argmin(corr_data))


class Interval_Decoder:
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
                    interpolated_msg.append(chip)
            seq.append(interpolated_msg)

        self.message_array = np.array(seq)
        self.intp_val = samples_per_chip
        self.max_len = len(self.message_array[0])
        self.data_array = []
        self.transformed_data = []

        self.mean = -80
        self.standard_deviation = 2
        self.threshold = 9*samples_per_chip*.35
        self.pilot = False
        self.second_pilot = False
        self.symbols_caught = []
        self.count = 0
        self.samples_per_chip = samples_per_chip
        self.first_values = []
        self.second_values = []
        self.protocol_accept = False
        self.get_samples_first = False
        self.get_samples_second = False

    def add_val(self, new_data):
        if len(self.symbols_caught) == 6:
            self.symbols_caught.clear()
        self.count += 1
        # new_data = self.saturate(new_data, -85, 30)
        self.mean = (new_data + self.mean * (self.max_len - 1)) / (self.max_len)
        # self.standard_deviation = (abs(new_data - self.mean) + self.standard_deviation * (self.max_len - 1)) / (self.max_len * 2)
        self.data_array.append(new_data)
        if len(self.data_array) > self.max_len:
            self.data_array.pop(0)
            min_data = np.min(self.data_array)
            d_ra = np.array(self.data_array)
            self.transformed_data = (d_ra - self.mean) / (
                np.max(self.data_array) - min_data
            )
            corr_data = []
            for msg in self.message_array:
                corr_data.append(
                    np.correlate(
                        msg - 0.5 * np.ones(self.max_len), self.transformed_data
                    )[0]
                )


            # check for first pilot and get readings afterwards
            
            if np.argmin(corr_data) == 4 and (np.min(corr_data)) < -1*self.threshold  and not self.get_samples_first:
                print("got first hit")
                self.get_samples_first = True
                self.count = 0
            if self.get_samples_first and not self.get_samples_second:
                # print("appending firsts")
                self.first_values.append(corr_data[4])
                if self.count >= 2*self.samples_per_chip:
                    self.get_samples_second = True
            if self.get_samples_second and self.count >= self.samples_per_chip*64 and not self.protocol_accept:
                # print("appending seconds")
                self.second_values.append(corr_data[4])
                if self.count >= self.samples_per_chip*64 + 2*self.samples_per_chip:
                    print("\n")
                    # print(self.first_values)
                    # print(self.second_values)
                    added = np.add(np.array(self.first_values), np.array(self.second_values))
                    print(added)
                    min_spot = np.argmin(added)
                    if np.abs(added[min_spot]) < self.threshold*1.5:
                        self.get_samples_first = False
                        self.get_samples_second = False
                        self.protocol_accept = False
                        self.first_values.clear()
                        self.second_values.clear()
                        print("false alarm")
                        return
                    print("Min index is:",min_spot)
                    self.count = 0 + (len(added)-min_spot-1)
                    print("new count:",self.count)
                    self.protocol_accept = True
            if self.protocol_accept and self.count == 64*self.samples_per_chip:
                index  =np.argmax(np.abs(corr_data))
                self.symbols_caught.append((str(index),corr_data[index]) if corr_data[index] > 0 else ("-"+str(index),corr_data[index]))
                self.count = 0
            if len(self.symbols_caught) == 6:
                # print(self.symbols_caught)
                # self.symbols_caught.clear()
                self.get_samples_first = False
                self.get_samples_second = False
                self.protocol_accept = False
                self.first_values.clear()
                self.second_values.clear()
                return self.symbols_caught
            if self.count > 300 and self.pilot:
                self.pilot = False
                self.second_pilot = False
            return
        # if len(self.symbols_caught) == 6:
        #     self.symbols_caught.clear()
        # self.count += 1
        # # new_data = self.saturate(new_data, -85, 30)
        # self.mean = (new_data + self.mean * (self.max_len - 1)) / (self.max_len)
        # # self.standard_deviation = (abs(new_data - self.mean) + self.standard_deviation * (self.max_len - 1)) / (self.max_len * 2)
        # self.data_array.append(new_data)
        # if len(self.data_array) > self.max_len:
        #     self.data_array.pop(0)
        #     min_data = np.min(self.data_array)
        #     d_ra = np.array(self.data_array)
        #     self.transformed_data = (d_ra - self.mean) / (
        #         np.max(self.data_array) - min_data
        #     )
        #     corr_data = []
        #     for msg in self.message_array:
        #         corr_data.append(
        #             np.correlate(
        #                 msg - 0.5 * np.ones(self.max_len), self.transformed_data
        #             )[0]
        #         )
        #     # check for the pilot symbols
        #     if np.abs(np.min(corr_data)) > self.threshold and np.argmin(corr_data) == 4:
        #         if self.pilot == True and 63*self.samples_per_chip <= self.count <= 65*self.samples_per_chip:
        #             print("second pilot found",self.count)
        #             self.second_pilot = True
        #             # temp_count = self.count
        #             self.count = 0
        #             # self.count -= 64*self.samples_per_chip-temp_count
        #             return
        #         self.count = 0
        #         print("first pilot found")
        #         self.pilot = True
        #     if self.second_pilot and self.count == 64*self.samples_per_chip:
        #         index  =np.argmax(np.abs(corr_data))
        #         self.symbols_caught.append((str(index),corr_data[index]) if corr_data[index] > 0 else ("-"+str(index),corr_data[index]))
        #         self.count = 0
        #     if len(self.symbols_caught) == 6:
        #         # print(self.symbols_caught)
        #         # self.symbols_caught.clear()
        #         self.pilot = False
        #         self.second_pilot = False
        #         return self.symbols_caught
        #     if self.count > 300 and self.pilot:
        #         self.pilot = False
        #         self.second_pilot = False

            # if np.max(np.abs(corr_data)) > 2.9 * np.mean(np.abs(corr_data)):
            #     if np.max(corr_data) > self.threshold:
            #         print(str(np.argmax(corr_data)) + " at " + str(max(corr_data)))
            #         # print(corr_data)
            #         # print(self.transformed_data)
            #         # return [str(np.argmax(corr_data)), sample]
            #         return str(np.argmax(corr_data))
            #     elif np.abs(np.min(corr_data)) > self.threshold:
            #         print(
            #             " - " + str(np.argmin(corr_data)) + " at " + str(min(corr_data))
            #         )
            #         # print(corr_data)
            #         # print(self.transformed_data)
            #         # return [np.argmin(corr_data) + len(self.message_array), sample]
            #         return "-" + str(np.argmin(corr_data))
