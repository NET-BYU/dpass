from gc import garbage
import os
import struct
from queue import Queue
import threading
import math
import time
import pickle
import signal

from numpy import average
from decoders import dynamic_decoder, Interval_Decoder
import matplotlib.pyplot as plt
import numpy as np
import sys


class Guts:
    def __init__(self, wireless_interface, interval, frequency, chip_sample_number):
        self.interval = interval
        self.frequency = frequency
        self.wireless_interface = wireless_interface
        self.scanner = Scanner(wireless_interface)
        print("Setting background mode")
        self.scanner.mode_background()
        # print("Setting frequency")
        # self.scanner.freqency_set(self.frequency)
        print("Setting sample count")
        self.scanner.set_sample_count()
        self.samples_per_chip = chip_sample_number
        self.decoder = dynamic_decoder(samples_per_chip=chip_sample_number)
        self.interval_decoder = Interval_Decoder(samples_per_chip=chip_sample_number)
        self.method_functions = {"auto_correlation": self.auto_correlation, "interval":self.interval_function}
        self.colors = {
            "0": "red",
            "1": "orange",
            "2": "green",
            "3": "blue",
            "4": "purple",
            "5": "pink",
            "-0": "maroon",
            "-1": "sandybrown",
            "-2": "lime",
            "-3": "navy",
            "-4": "violet",
            "-5": "deeppink",
        }
        self.colors_reversed = {
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

        self.dict_bandwidth = {"0":"10","1":"20","2":"40","3":"80","4":"160"}
        self.dict_duration = {"0":"0.5","1":"1","2":"2","3":"3","4":"4","5":"5","-0":"6","-1":"8","-2":"12","-3":"18","-5":"24"}
        self.dict_freq = {"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","-0":"6","-1":"7","-2":"8","-3":"9","-5":"10"}

    def active_decode(self, method, switch, count):
        captured = 0
        not_good = 0
        false_positive = 0
        captured_data = []
        def handler(signum, frame):
            print("Finished processing, closing up")
            self.scanner.stop()
            if count:
                for index,a in enumerate(captured_data):
                    print(index,a)
                print("Total captured:", captured, "Corrupted:",not_good, "False Positive:",false_positive)
            exit(0)

        signal.signal(signal.SIGINT, handler)

        print("Starting active decoding")
        first_time = True
        method_function = self.method_functions[method]
        self.scanner.trigger()
        self.scanner.file_reader.flush()
        prev_list = []
        counter = 0
        captured = 0
        while self.scanner.file_reader.sample_queue.empty():
            print("Trying to restart")
            self.scanner.stop()
            self.scanner = Scanner(self.wireless_interface)
            print("Setting background mode")
            self.scanner.mode_background()
            # print("Setting frequency")
            # self.scanner.freqency_set(self.frequency)
            print("Setting sample count")
            self.scanner.set_sample_count()
            self.scanner.trigger()
            self.scanner.file_reader.flush()
            time.sleep(0.5)
            continue
        print("actually started now")
        while True:
            try:
                if self.scanner.file_reader.sample_queue.empty():
                    counter +=1
                    if counter >= 200:
                        print("the thing has paused")
                        # while self.scanner.file_reader.sample_queue.empty():
                        #     time.sleep(0.01)
                        print("Trying to restart")
                        self.scanner.stop()
                        self.scanner = Scanner(self.wireless_interface)
                        print("Setting background mode")
                        self.scanner.mode_background()
                        # print("Setting frequency")
                        # self.scanner.freqency_set(self.frequency)
                        print("Setting sample count")
                        self.scanner.set_sample_count()
                        self.scanner.trigger()
                        self.scanner.file_reader.flush()
                        counter = 0
                        print("start collecting")
                        continue
                    time.sleep(0.01)
                    continue
                counter = 0
                for tsf, freq, noise, rssi, pwrs in SpectrumFileReader.decode(
                    (self.scanner.file_reader.sample_queue.get())
                ):
                    if first_time:  # add the fist sample and set up variables
                        first_time = False
                        prev_time = tsf
                        cum_time = prev_time
                        prev_measurement = rssi + noise
                        # measurements.append(prev_measurement)
                        method_function(prev_measurement)
                        continue
                    cum_time += (
                        tsf - prev_time
                    )  # get the interval between current sample and previous sample and add to cumalative time
                    prev_time = tsf

                    # print(cum_time)
                    if self.interval - 10 < cum_time:  # we have hit a interval

                        # print("interval found", cum_time)
                        cum_time -= (
                            self.interval
                        )  # take the interval time off of the cumalative time
                        if (
                            cum_time > self.interval * 100
                        ):  # to large of a gap, just start over, like way to large of gap
                            print("to large of a gap, starting over")
                            cum_time = 0
                            prev_list.clear()
                            # prev_measurement = rssi + noise
                            # measurements.append(prev_measurement)
                            continue
                        while (
                            cum_time > self.interval
                        ):  # we have overshot our interval so we need to interpolate, add a previous value then subtract the interval time to get back on track, iterate until back on track

                            # print("extra interval:", cum_time)
                            # measurements.append(prev_measurement)
                            # test = method_function(
                            #     prev_measurement
                            # )
                            #
                            # adding previous measurement, probably should reflect that actually wifi packet was sent
                            # measurements.append(-70)
                            test = method_function(-70)
                            if test is not None:  # we found a symbol
                                print(test)
                                try:
                                    print("Duration:", self.dict_duration[test[0][0]]+"Hrs")
                                    duration = self.dict_duration[test[0][0]]
                                    frequency = self.dict_freq[test[1][0]]+"."+self.dict_freq[test[2][0]]+self.dict_freq[test[3][0]]+self.dict_freq[test[4][0]]
                                    print("Frequency:", frequency+"GHz")
                                    print("Bandwidth:",self.dict_bandwidth[test[5][0]]+"MHz")
                                    bandwidth = self.dict_bandwidth[test[5][0]]
                                    captured_data.append([duration, frequency, bandwidth])
                                    if frequency == "2.437" and duration == "0.5" and bandwidth == "10":
                                            # Need to switch frequency
                                            if switch:
                                                print("switching to 5GHz")
                                                os.system("nmcli device wifi rescan")
                                                with open("network_config.txt", "r") as nc:
                                                    ssid = nc.readline().rstrip()
                                                    password = nc.readline().rstrip()
                                                os.system("nmcli dev wifi connect \"{ssid}\" password {password}")
                                                self.scanner.stop()
                                                sys.exit(0)
                                            if count:
                                                captured += 1
                                    else:
                                        false_positive += 1
                                    
                                            
                                    # if frequency == "5.765":
                                    #     # Need to switch frequency
                                    #     print("switching to 2.4GHz")
                                    #     os.system("nmcli device wifi rescan")
                                    #     os.system("nmcli dev wifi connect \"Cougar Lan\" password lanparty")
                                    #     self.scanner.stop()
                                    #     sys.exit(0)
                                except KeyError:
                                    print("wrong symbol detected")
                                    not_good += 1
                            # if test is not None:  # we found a symbol
                            #     location.append(
                            #         [
                            #             (
                            #                 len(measurements)
                            #                 - 63 * self.samples_per_chip,
                            #                 len(measurements),
                            #             ),
                            #             (-80, -80),
                            #             self.colors[test],
                            #         ]
                            #     )
                            cum_time -= self.interval
                        else:
                            prev_list.clear()
                        prev_list.append(rssi + noise)
                        past_avg = average(prev_list)
                        prev_list.clear()
                        # measurements.append(past_avg)
                        test = method_function(past_avg)
                        # measurements.append(rssi + noise)
                        # test = method_function(
                        #     rssi + noise
                        # )  # we are now back to our normal interval
                        if test is not None:  # we found a symbol
                            print(test)
                            try:
                                print("Duration:", self.dict_duration[test[0][0]]+"Hrs")
                                duration = self.dict_duration[test[0][0]]
                                frequency = self.dict_freq[test[1][0]]+"."+self.dict_freq[test[2][0]]+self.dict_freq[test[3][0]]+self.dict_freq[test[4][0]]
                                print("Frequency:", frequency+"GHz")
                                print("Bandwidth:",self.dict_bandwidth[test[5][0]]+"MHz")
                                bandwidth = self.dict_bandwidth[test[5][0]]
                                captured_data.append([duration, frequency, bandwidth])  
                                if frequency == "2.437" and duration == "0.5" and bandwidth == "10":
                                            # Need to switch frequency
                                            if switch:
                                                print("switching to 5GHz")
                                                os.system("nmcli device wifi rescan")
                                                with open("network_config.txt", "r") as nc:
                                                    ssid = nc.readline().rstrip()
                                                    password = nc.readline().rstrip()
                                                os.system("nmcli dev wifi connect \"{ssid}\" password {password}")
                                                self.scanner.stop()
                                                sys.exit(0)
                                            if count:
                                                captured += 1
                                else:
                                    false_positive += 1
                                
                                        
                                # if frequency == "5.765":
                                #     # Need to switch frequency
                                #     print("switching to 2.4GHz")
                                #     os.system("nmcli device wifi rescan")
                                #     os.system("nmcli dev wifi connect \"Cougar Lan\" password lanparty")
                                #     self.scanner.stop()
                                #     sys.exit(0)
                            except KeyError:
                                print("wrong symbol detected")
                                not_good += 1

                        #     location.append(
                        #         [
                        #             (
                        #                 len(measurements) - 63 * self.samples_per_chip,
                        #                 len(measurements),
                        #             ),
                        #             (-80, -80),
                        #             self.colors[test],
                        #         ]
                        #     )
                        continue
                    prev_list.append(rssi + noise)

            except EOFError:
                break

    def passive_capture(self, total_time, output_file):
        print(
            f"Starting passive dumping of wifi measurements for {total_time} second(s) at {output_file}"
        )
        start_time = time.time()
        dump_file = open(output_file, "wb+")
        self.scanner.trigger()
        self.scanner.file_reader.flush()
        while self.scanner.file_reader.sample_queue.empty():
            time.sleep(0.1)
            pass
        print("starting")
        start_time = time.time()
        self.scanner.file_reader.flush()
        while time.time() - start_time < total_time:
            if self.scanner.file_reader.sample_queue.empty():
                continue
            pickle.dump((self.scanner.file_reader.sample_queue.get()), dump_file)
        print("Finished collecting samples")
        self.scanner.stop()

    def pass_decode(self, sample_file, method, graph):
        print(
            f"Processing {sample_file} with an interval of {self.interval} microseconds"
        )
        f = open(sample_file, "rb")
        first_time = True
        method_function = self.method_functions[method]
        measurements = []
        location = []
        prev_list = []
        while True:
            try:
                sample_data = pickle.load(f)
                for tsf, freq, noise, rssi, pwrs in SpectrumFileReader.decode(
                    sample_data
                ):
                    if first_time:  # add the fist sample and set up variables
                        first_time = False
                        prev_time = tsf
                        cum_time = prev_time
                        prev_measurement = rssi + noise
                        measurements.append(prev_measurement)
                        method_function(prev_measurement)
                        continue
                    cum_time += (
                        tsf - prev_time
                    )  # get the interval between current sample and previous sample and add to cumalative time
                    prev_time = tsf

                    # print(cum_time)
                    if self.interval - 10 < cum_time:  # we have hit a interval

                        # print("interval found", cum_time)
                        cum_time -= (
                            self.interval
                        )  # take the interval time off of the cumalative time
                        if (
                            cum_time > self.interval * 100
                        ):  # to large of a gap, just start over, like way to large of gap
                            print("to large of a gap, starting over")
                            cum_time = 0
                            prev_list.clear()
                            # prev_measurement = rssi + noise
                            # measurements.append(prev_measurement)
                            continue
                        while (
                            cum_time > self.interval
                        ):  # we have overshot our interval so we need to interpolate, add a previous value then subtract the interval time to get back on track, iterate until back on track

                            # print("extra interval:", cum_time)
                            # measurements.append(prev_measurement)
                            # test = method_function(
                            #     prev_measurement
                            # )
                            #
                            # adding previous measurement, probably should reflect that actually wifi packet was sent
                            measurements.append(-75)
                            test = method_function(-75)
                            if test is not None:  # we found a symbol
                                location.append(
                                    [
                                        (
                                            len(measurements)
                                            - 63 * self.samples_per_chip,
                                            len(measurements),
                                        ),
                                        (-80, -80),
                                        self.colors[test],
                                    ]
                                )
                            cum_time -= self.interval
                        else:
                            prev_list.clear()
                        prev_list.append(rssi + noise)
                        past_avg = average(prev_list)
                        prev_list.clear()
                        measurements.append(past_avg)
                        test = method_function(past_avg)
                        # measurements.append(rssi + noise)
                        # test = method_function(
                        #     rssi + noise
                        # )  # we are now back to our normal interval
                        if test is not None:  # we found a symbol
                            location.append(
                                [
                                    (
                                        len(measurements) - 63 * self.samples_per_chip,
                                        len(measurements),
                                    ),
                                    (-80, -80),
                                    self.colors[test],
                                ]
                            )
                        continue
                    prev_list.append(rssi + noise)
                    # prev_measurement = rssi + noise
                    # prev_list.append(rssi + noise)
                    # measurements.append(prev_measurement)

            except EOFError:
                break
        print("Finished processing, closing up")
        self.scanner.stop()
        f.close()
        print("min:", min(measurements), "max:", max(measurements))
        m = np.array(measurements, dtype=np.float32)
        m.tofile("/tmp/float_wifi_data.f32")
        print(location)
        if graph:
            plt.figure(figsize=(10, 6))
            graphs = [plt.scatter(np.arange(0, len(measurements)), measurements, s=1)]
            graph_names = ["measurements"]
            # plt.scatter(location, [-80] * len(location), c=[[1, 0, 0]])
            # for line in location:
            #     graphs.append(
            #         plt.arrow(
            #             line[0][0],
            #             int(average([min(measurements), max(measurements)])),
            #             63 * self.samples_per_chip,
            #             0,
            #             color=line[2],
            #             width=1,
            #             length_includes_head=True,
            #         )
            #     )
            #     graph_names.append(self.colors_reversed[line[2]])
            # plt.title("Symbols found in transmision")
            plt.xlabel("Sample number")
            plt.ylabel("RSSI measurment (dBm)")
            graph_names, indexes = np.unique(graph_names,return_index=True)
            plt.legend(np.array(graphs)[indexes], graph_names, loc="upper right", bbox_to_anchor=(1.02, 1))
            plt.show()

    def auto_correlation(self, sample):
        return self.decoder.add_val(sample, 0)
    def interval_function(self, sample):
        return self.interval_decoder.add_val(sample)


class Scanner:
    def __init__(self, interface):
        self.interface = interface
        self.debugfs_dir = self._find_debugfs_dir()
        if not self.debugfs_dir:
            raise Exception(
                "Unable to access spectral_scan_ctl file for interface %s" % interface
            )
        self.ctl_file = "%s/spectral_scan_ctl" % self.debugfs_dir
        self.sample_count_file = "%s/spectral_count" % self.debugfs_dir
        self.file_reader = SpectrumFileReader("%s/spectral_scan0" % self.debugfs_dir)

    def dev_to_phy(self, dev):
        f = open("/sys/class/net/%s/phy80211/name" % dev)
        phy = f.read().strip()
        f.close()
        return phy

    def _find_debugfs_dir(self):
        """search debugfs for spectral_scan_ctl for this interface"""
        for dirname, subd, files in os.walk("/sys/kernel/debug/ieee80211"):
            if "spectral_scan_ctl" in files:
                phy = dirname.split(os.path.sep)[-2]
                if phy == self.dev_to_phy(self.interface):
                    self.phy = phy
                    return dirname
        return None

    def mode_background(self):

        f = open(self.ctl_file, "w")
        f.write("background")
        f.close()

    def trigger(self):
        f = open(self.ctl_file, "w")
        f.write("trigger")
        f.close()

    def set_sample_count(self):
        f = open(self.sample_count_file, "w")
        f.write("%s" % 0)
        f.close()

    def freqency_set(self, freq):
        # os.system("ifconfig %s down" % self.interface)
        # os.system("iw dev %s set type monitor" % self.interface)
        # os.system("ifconfig %s up" % self.interface)
        os.system("iw dev %s set freq %d %s" % (self.interface, freq, "HT20"))
        # os.system("ifconfig %s down" % self.interface)
        # os.system("iw dev %s set type managed" % self.interface)
        # os.system("ifconfig %s up" % self.interface)

    def stop(self):
        f = open(self.ctl_file, "w")
        f.write("disable")
        f.close()
        self.file_reader.stop()


class SpectrumFileReader(object):
    def __init__(self, path):
        self.fp = open(path, "rb")
        if not self.fp:
            print("Cant open file '%s'" % path)
            raise
        self.sample_queue = Queue()
        self.reader_thread = threading.Thread(target=self.read_samples_thread, args=())
        self.reader_thread_stop = False
        self.reader_thread_pause = False
        self.reader_thread.start()

    def stop(self):
        self.reader_thread_stop = True
        self.reader_thread.join()
        self.flush()

    def flush(self):  # flush queue and empty file / debugfs buffer (dirty)
        self.reader_thread_pause = True
        while not self.sample_queue.empty():
            self.sample_queue.get()
        self.fp.read()
        self.reader_thread_pause = False

    def read_samples_thread(self):
        while not self.reader_thread_stop:
            if self.reader_thread_pause:
                continue
            # ts = datetime.now()
            data = self.fp.read()
            if not data:
                # time.sleep(0.05)
                continue
            self.sample_queue.put((data))

    # spectral scan packet format constants
    hdrsize = 3
    type1_pktsize = 17 + 56
    type2_pktsize = 24 + 128
    type3_pktsize = 26 + 64

    # ieee 802.11 constants
    sc_wide = 0.3125  # in MHz

    @staticmethod
    def decode(data):
        """
        For information about the decoding of spectral samples see:
        https://wireless.wiki.kernel.org/en/users/drivers/ath9k/spectral_scan
        https://github.com/erikarn/ath_radar_stuff/tree/master/lib
        and your ath9k implementation in e.g.
        /drivers/net/wireless/ath/ath9k/common-spectral.c
        """
        pos = 0
        while pos < len(data) - SpectrumFileReader.hdrsize + 1:

            (stype, slen) = struct.unpack_from(">BH", data, pos)

            if not (
                (stype == 1 and slen == SpectrumFileReader.type1_pktsize)
                or (stype == 2 and slen == SpectrumFileReader.type2_pktsize)
                or (stype == 3 and slen == SpectrumFileReader.type3_pktsize)
            ):
                print("skip malformed packet")
                break  # header malformed, discard data. This event is very unlikely (once in ~3h)
                # On the other hand, if we buffer the sample in a primitive way, we consume to much cpu
                # for only one or too "rescued" samples every 2-3 hours

            # 20 MHz
            if stype == 1:
                if (
                    pos
                    >= len(data)
                    - SpectrumFileReader.hdrsize
                    - SpectrumFileReader.type1_pktsize
                    + 1
                ):
                    break
                pos += SpectrumFileReader.hdrsize
                (
                    max_exp,
                    freq,
                    rssi,
                    noise,
                    max_mag,
                    max_index,
                    hweight,
                    tsf,
                ) = struct.unpack_from(">BHbbHBBQ", data, pos)
                pos += 17

                sdata = struct.unpack_from("56B", data, pos)
                pos += 56

                # calculate power in dBm
                sumsq_sample = 0
                samples = []
                for raw_sample in sdata:
                    if raw_sample == 0:
                        sample = 1
                    else:
                        sample = raw_sample << max_exp
                    sumsq_sample += sample * sample
                    samples.append(sample)

                if sumsq_sample == 0:
                    sumsq_sample = 1
                sumsq_sample = 10 * math.log10(sumsq_sample)

                sc_total = 56  # HT20: 56 OFDM subcarrier, HT40: 128
                first_sc = freq - SpectrumFileReader.sc_wide * (sc_total / 2 + 0.5)
                pwr = {}
                for i, sample in enumerate(samples):
                    subcarrier_freq = first_sc + i * SpectrumFileReader.sc_wide
                    sigval = noise + rssi + 20 * math.log10(sample) - sumsq_sample
                    pwr[subcarrier_freq] = sigval

                yield (tsf, freq, noise, rssi, pwr)
